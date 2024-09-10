import dicom_to_nifti_convertor
import nifti_json_parser

# Converts all DICOM files in one directory into JSON and relevant .csv DataFrame in another.

in_path = input("Enter the file path containing DICOM files: ")
out_path = input("Enter the designated output folder: ")

dicom_to_nifti_convertor.dicom_to_nifti(in_path, out_path)
nifti_json_parser.parse_all_JSON_info(out_path)
