import os

confDirectory  = "../../media/uploads/0_Data"
confPath = os.path.realpath(confDirectory)

print("confPath =", confPath)



def remove_files_in_directory(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Directory does not exist:", directory)
        return

    # Iterate over each entry in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            # Remove the file
            os.remove(file_path)
            print(f"Removed file: {file_path}")



directory_path = confPath
remove_files_in_directory(directory_path)