import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings

warnings.filterwarnings("ignore")
import pandas as pd 

# class PeakHoursFinder:
#     def __init__(self, file_path):
#         self.file_path = file_path
    
#     def read_location_data(self):
#         try:
#             #reading dataset 
#             data = pd.read_csv(self.file_path)
#             # Check if the DataFrame has neccesary columns for latitude, longitude, and timestamp
#             required_columns = ['latitude', 'longitude', 'timestamp']

#             if all(col in data.columns for col in required_columns):
#                 location_data = data[required_columns]
#             else:
#                 # manage other names of columns available columns
#                 possible_columns = ['lat', 'lon', 'time', 'latitudes', 'longitudes', 'timestamps']
#                 common_columns = list(set(possible_columns) & set(data.columns))

#                 if len(common_columns) >= len(required_columns):
#                     location_data = data[common_columns]
#                     location_data.columns = required_columns
#                 else:
#                     raise ValueError("Location data should have required columns ('longitude','latitude','timestamp').")
                
#             # Convert 'timestamp' to datetime format
#             location_data['timestamp'] = pd.to_datetime(location_data['timestamp'])         

#             return location_data

#         except pd.errors.EmptyDataError:
#             print("The provided file is empty.")
#             return None
#         except pd.errors.ParserError:
#             print("Error parsing the file.")
#             return None
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")
#             return None

#     def find_peak_hours(self):
#         location_data = self.read_location_data()

#         if location_data is not None:
#             # Add your peak hours detection logic here based on the timestamp column
#             # For example, you can calculate the frequency of data points for each hour

#             # Assuming 'timestamp' is in datetime format
#             location_data['hour'] = location_data['timestamp'].dt.hour

#             peak_hours = location_data['hour'].value_counts().sort_values(ascending=False).index
#             return peak_hours
#         else:
#             return None
        
#     def create_peak_hours_plot(self):
#         peak_hours = self.find_peak_hours()
#         location_data = self.read_location_data()
#         if peak_hours is not None:
#             plt.figure(figsize=(10, 6))
#             plt.bar(peak_hours, height=location_data['hour'].value_counts().loc[peak_hours].sort_index().values)
#             plt.xlabel('Hour of Day')
#             plt.ylabel('Frequency')
#             plt.title('Peak Hours Distribution')
#             plt.show()
#         else:
#             print("No peak hours found or error in data.")

# # Example Usage:
# file_path = '/Users/shokoufehhosseini/Documents/AutoTelCarParked/cars.csv'
# peak_hours_finder = PeakHoursFinder(file_path)
# peak_hours_finder.read_location_data()
# peak_hours_finder.create_peak_hours_plot()
        
    # def peak_hours_plot(self):
    #     location_data = self.read_location_data()

    #     location_data['timestamp'] = location_data['timestamp'].apply(pd.Timestamp)
    #     location_data.set_index('timestamp').sort_index().rolling('60min').mean().plot(figsize=(20,6), c='salmon', lw=1.6)
    #     plt.grid()
    #     plt.show()
    #     return None

# # Example Usage:
# file_path = '/Users/shokoufehhosseini/Documents/AutoTelCarParked/cars.csv'
# peak_hours_finder = PeakHours(file_path)
# result = peak_hours_finder.find_peak_hours()

# if result is not None:
#     print("Peak Hours:")
#     print(result)
        

        
# import pandas as pd

# class PeakHoursFinder:
#     def __init__(self, file_path):
#         self.file_path = file_path

#     def read_location_data(self):
#         try:
#             # Read the data into a pandas DataFrame
#             data = pd.read_csv(self.file_path)

#             # Check if the DataFrame has at least columns for latitude, longitude, and timestamp
#             required_columns = ['latitude', 'longitude', 'timestamp']

#             if all(col in data.columns for col in required_columns):
#                 location_data = data[required_columns]
#             else:
#                 # Handle other scenarios based on the available columns
#                 possible_columns = ['lat', 'lon', 'time', 'latitudes', 'longitudes', 'timestamps']
#                 common_columns = list(set(possible_columns) & set(data.columns))

#                 if len(common_columns) >= len(required_columns):
#                     location_data = data[common_columns]
#                     location_data.columns = required_columns
#                 else:
#                     raise ValueError("Unable to identify required columns.")

#             # Convert 'timestamp' to datetime format
#             location_data['timestamp'] = pd.to_datetime(location_data['timestamp'])

#             return location_data

#         except pd.errors.EmptyDataError:
#             print("The provided file is empty.")
#             return None
#         except pd.errors.ParserError:
#             print("Error parsing the file. Please check the file format.")
#             return None
#         except Exception as e:
#             print(f"An error occurred: {str(e)}")
#             return None

#     def find_peak_hours(self):
#         location_data = self.read_location_data()

#         if location_data is not None:
#             # Add your peak hours detection logic here based on the timestamp column
#             # For example, you can calculate the frequency of data points for each hour

#             # Assuming 'timestamp' is now in datetime format
#             location_data['hour'] = location_data['timestamp'].dt.hour

#             peak_hours = location_data['hour'].value_counts().sort_values(ascending=False).index
#             return peak_hours
#         else:
#             return None
        
        # def peak_hours_plot(self):
        #     location_data = self.read_location_data()

        #     location_data['timestamp'] = location_data['timestamp'].apply(pd.Timestamp)
        #     location_data.set_index('timestamp').sort_index().rolling('60min').mean().plot(figsize=(20,6), c='salmon', lw=1.6)
        #     plt.grid()
        #     plt.show()


import pandas as pd
import matplotlib.pyplot as plt

class PeakHoursFinder:
    def __init__(self, file_path):
        self.file_path = file_path
        self.location_data = None  # Initialize location_data as an instance variable

    def read_location_data(self):
        try:
            # Reading dataset
            data = pd.read_csv(self.file_path)
            # Check if the DataFrame has necessary columns for latitude, longitude, and timestamp
            required_columns = ['latitude', 'longitude', 'timestamp']

            if all(col in data.columns for col in required_columns):
                location_data = data[required_columns]
            else:
                # Manage other names of columns available columns
                possible_columns = ['lat', 'lon', 'time', 'latitudes', 'longitudes', 'timestamps']
                common_columns = list(set(possible_columns) & set(data.columns))

                if len(common_columns) >= len(required_columns):
                    location_data = data[common_columns]
                    location_data.columns = required_columns
                else:
                    raise ValueError("Location data should have required columns ('longitude','latitude','timestamp').")

            # Convert 'timestamp' to datetime format
            location_data['timestamp'] = pd.to_datetime(location_data['timestamp'])

            self.location_data = location_data  # Save location_data as an instance variable
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
            # Assuming 'timestamp' is in datetime format
            location_data['hour'] = location_data['timestamp'].dt.hour

            peak_hours = location_data['hour'].value_counts().sort_values(ascending=False).index
            return location_data, peak_hours
        else:
            return None, None

    def create_peak_hours_plot(self):
        location_data, peak_hours = self.find_peak_hours()

        if peak_hours is not None:
            plt.figure(figsize=(10, 6))
            plt.bar(peak_hours, height=location_data['hour'].value_counts().loc[peak_hours].sort_index().values)
            plt.xlabel('Hour of Day')
            plt.ylabel('Frequency')
            plt.title('Peak Hours Distribution')
            plt.show()
        else:
            print("No peak hours found or error in data.")
            return None, None
    

#     # Example Usage:
# file_path = '/Users/shokoufehhosseini/Documents/AutoTelCarParked/cars.csv'
# peak_hours_finder = PeakHoursFinder(file_path)
# peak_hours_finder.create_peak_hours_plot()



