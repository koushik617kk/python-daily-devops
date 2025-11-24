import pandas as pd
import os
CSV_FILE = 'mock.csv'

def display_raw_csv(csv_file):
 
    if os.path.exists(csv_file):
        print(f"{csv_file} Exists")
        df = pd.read_csv(csv_file)
        print(df.head())
    else:
        return

def filtering_based_on_dptype(csv_file):
    
    try:

        df = pd.read_csv(csv_file) 
        filtered = df[(df['deployment_type'] == 'rolling') | (df['environment']=="prod") ]
        if filtered.empty:
            print("Now row found with deployment type = rolling")
        else:
            print(f"Filtered Rows:")
            print(f"{filtered}")

    except FileNotFoundError:
        print("File Not FOund")
    except pd.errors.EmptyDataError:
        print("CSV file is empty")
    except Exception as e:
        print(f"{e}")


    


display_raw_csv(CSV_FILE)
print("-"*30)
filtering_based_on_dptype(CSV_FILE)
