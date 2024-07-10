

import os



def readFileLocation(confPath):
    import os
    value2=""
    value3=""


    inputTex_FilePath = confPath + "/2_downloadingLocal1.txt"
    if os.path.exists(inputTex_FilePath):
        with open(inputTex_FilePath, 'r') as file:
            for line in file:
                variable_name, value2 = line.split('=')
                value2 = value2.strip()

    inputTex_FilePath = confPath + "/2_downloadingLocal2.txt"
    if os.path.exists(inputTex_FilePath):
        with open(inputTex_FilePath, 'r') as file:
            for line in file:
                variable_name, value3 = line.split('=')
                value3 = value3.strip()

    return value2, value3


def rename_first_excel_file(directory, new_name):
    # Iterate through each file in the directory
    for file in os.listdir(directory):
        if file.endswith(".xlsx"):  # Check if the file is an Excel file
            old_file_path = os.path.join(directory, file)
            new_file_path = os.path.join(directory, new_name)

            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed '{file}' to '{new_name}'")
            return  # Exit after renaming the first Excel file found

    print("No Excel file found in the directory.")



