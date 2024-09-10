FILES:

dicom_to_nifti_convertor.py : converts all DICOM files to NifTI
nifti_json_parser.py : Parses JSON files after conversion to retrieve .csv file and DataFrame of relevant information
dicom_to_csv.py : All-in-one script that does both processes above

==================================================================================================

README:

- DICOM files converted into NifTI files with naming format: "protocol_seriesnumber_time.nii"
- Acquisition time based off JSON data, not NIFTI (it is slightly different)
- Unable to find patient age/PHI, set it to NaN
- Assumes that pandas, dcm2niix, python are installed

==================================================================================================

EXAMPLE USAGE: 

The following converts DICOM files into NifTI/JSON and a .csv file.

- Make an input folder of your DICOM files (e.g. C:\Users\Bob\Downloads\test)
- Make an output folder (e.g. C:\Users\Bob\Downloads\output)
- Place all .py files in your output folder
- Change to your output folder directory in command-line (cd C:\Users\Bob\Downloads\output)

- run the command "python dicom_to_csv.py", and paste in your input and output folders when the prompt asks you to. 

"Enter the file path containing DICOM files: C:\Users\Bob\Downloads\test"
"Enter the designated output folder: C:\Users\Bob\Downloads\output"
