import pandas as pd
import os
import time

def readfile():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, 'data')
    currCount = 0
    while True:
        # List all CSV files in the data directory
        csv_files = [file for file in os.listdir(data_dir) if file.endswith('.csv')]
        newCount = len(csv_files)

        if (newCount > currCount):
            # Sort files by modification time to get the latest file
            latest_file = max(csv_files, key=lambda x: os.path.getmtime(os.path.join(data_dir, x)))

            # Construct the full path to the latest CSV file
            csv_path = os.path.join(data_dir, latest_file)

            # Read the CSV file
            df = pd.read_csv(csv_path)

            # Extract data for each channel
            channel1_data = df["Channel1"]
            channel2_data = df['Channel2']
            channel3_data = df['Channel3']
            channel4_data = df['Channel4']
            
            return newCount, channel1_data, channel2_data, channel3_data, channel4_data

        else:
            print("No CSV files found in the data directory.")
            return None

        # Wait for 30 seconds before checking for new files again
        time.sleep(10)

# Call the function to start reading files
readfile()
