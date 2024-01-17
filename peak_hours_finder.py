import pandas as pd
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
import folium
from folium.plugins import HeatMap
warnings.filterwarnings("ignore")


class PeakHoursFinder:
    def __init__(self,path):
        self.path = path

    def read_data(self):
        data = pd.read_csv(self.path)
        return data
    def read_location_data(self):
        try:
            #reading dataset 
            data = pd.read_csv(self.path)
            # Check if the DataFrame has neccesary columns for latitude, longitude, and timestamp
            required_columns = ['latitude', 'longitude', 'timestamp']

            if all(col in data.columns for col in required_columns):
                location_data = data[required_columns]
            else:
                # manage other names of columns available columns
                possible_columns = ['lat', 'lon', 'time', 'latitudes', 'longitudes', 'timestamps']
                common_columns = list(set(possible_columns) & set(data.columns))

                if len(common_columns) >= len(required_columns):
                    location_data = data[common_columns]
                    location_data.columns = required_columns
                else:
                    raise ValueError("Location data should have required columns ('longitude','latitude','timestamp').")
                
            # Convert 'timestamp' to datetime format
            location_data['timestamp'] = pd.to_datetime(location_data['timestamp'])         

            return location_data

        except pd.errors.EmptyDataError:
            print("The provided file is empty.")
            return None
        except pd.errors.ParserError:
            print("Error parsing the file.")
            return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
        
        
    def find_peak_hours(self):
        location_data = self.read_location_data()

        if location_data is not None:
            # Add your peak hours detection logic here based on the timestamp column
            # For example, you can calculate the frequency of data points for each hour

            # Assuming 'timestamp' is in datetime format
            location_data['hour'] = location_data['timestamp'].dt.hour

            peak_hours = location_data['hour'].value_counts().sort_values(ascending=False).index
            return peak_hours
        else:
            return None
        
    
    def create_peak_hours_plot(self):
        location_data = self.read_location_data()

        if location_data is not None:
            # Assuming 'timestamp' is in datetime format
            location_data['timestamp'] = pd.to_datetime(location_data['timestamp']) 
            location_data['hour'] = location_data['timestamp'].dt.hour

            peak_hours = location_data['hour'].value_counts().sort_values(ascending=False).index

            if peak_hours is not None:
                plt.figure(figsize=(10, 6))
                plt.bar(peak_hours, height=location_data['hour'].value_counts().loc[peak_hours].sort_index().values)
                plt.xlabel('Hour of Day')
                plt.ylabel('Frequency')
                plt.title('Peak Hours Distribution')
                plt.show()
            else:
                print("No peak hours found or error in data.")
        else:
            print("No data available.")
        
    def create_map(self):
        location_data = self.read_location_data()
        locations = location_data.groupby(['latitude', 'longitude', 'timestamp']).sum().reset_index()

        m = folium.Map([locations.latitude.mean(), locations.longitude.mean()], zoom_start=11)
        for index, row in locations.iterrows():
            folium.CircleMarker([row['latitude'], row['longitude']],
                                radius=row['total_cars'] * 6,
                                fill_color="#3db7e4", 
                            ).add_to(m)
            
        points = locations[['latitude', 'longitude']].as_matrix()
        m.add_children(HeatMap(points, radius=15)) # plot heatmap
        
        return m