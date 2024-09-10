import json, os
import pandas as pd
import numpy as np

def parse_all_JSON_info(input_path):
    """Parse all MRI scan JSON files in the input directory, returning a DataFrame of format:

    [file_name, mfs, acquisition_date, acquisition_time, age, series_desc].

    Returns .csv file of this DataFrame
    """
    if not os.path.exists(input_path):
        print("Path does not exist")
        return
    
    json_files = [pos_json for pos_json in os.listdir(input_path) if pos_json.endswith('.json')]
    if len(json_files) == 0:
        print("There are no JSON files to read.")
        return
    
    # This determines the fields that you want to look at
    json_data = pd.DataFrame(columns = ['file', 'mfs', 'acquisition_date', 'acquisition_time', 'age', 'series_desc'])

    for i, file_name in enumerate(json_files):
        with open(os.path.join(input_path, file_name)) as json_file: # get true file name 
            json_text = json.load(json_file)

            mfs = json_text['MagneticFieldStrength']

            acquisition_date = file_name.split('_')[-1]
            acquisition_date = acquisition_date[:8] # Get the first 8 numbers
            acquisition_date = pd.to_datetime(acquisition_date, format='%Y%m%d')
            formatted_acq_date = acquisition_date.strftime('%m/%d/%Y')

            acquisition_time = json_text['AcquisitionTime']
            formatted_time = acquisition_time.split('.')[0] # Get the HH:MM:SS form of time

            patient_age = np.NaN # There was no key-field for this so I set this as NULL
            series_desc = json_text['SeriesDescription']

            json_data.loc[i] = [file_name, mfs, formatted_acq_date, formatted_time, patient_age, series_desc]

    print(json_data)

    json_data.to_csv('patient_JSON_info.csv', index=False)
    
    print("Successfully created .csv file of MRI JSON files.")

    return

def main():
    in_path = input("Enter your directory containing JSON files: ")
    parse_all_JSON_info(in_path)

if __name__ == "__main__":
    main()