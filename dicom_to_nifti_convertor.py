import os
import subprocess

def dicom_to_nifti(input_path, output_path):
    """
    Convert all DICOM files found in the input_path into the NifTI format in the output_path.

        - Uses the dcm2niix repository.

    input_path (str) : Directory path containing DICOM files 
    output_path (str) : Directory path to save NifTI files into
    """

    if not os.path.exists(input_path):
        print("Input path does not exist. Please retry with an existing directory. ")
        return

    if not os.path.exists(output_path):
        print("Output path does not exist. Please retry with an existing directory. ")
        return
    else:
        try: 
            subprocess.run(["dcm2niix", "-f", "%p_%s_%t", "-o", output_path, input_path]) # %p_%s_t argument determines file naming order
            print("Converted files into directory: ", output_path)
        except FileNotFoundError:
            print("dcm2niix is not installed or could not be found in the systme's PATH")
            print("Please install dcm2niix or check your PATH environmental variables.")
        except: 
            print("Failed to convert files.")
            
    return

def main():
    in_path = input("Enter the file path containing DICOM files: ")
    out_path = input("Enter the designated output folder: ")

    dicom_to_nifti(in_path, out_path)  

if __name__ == "__main__":
    main()