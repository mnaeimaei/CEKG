import os


#Remove Txt file for configuration

confDirectory = "../Data/0_Conf"
confPath = os.path.realpath(confDirectory)
#print(confPath)

for filename in os.listdir(confPath):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        # Construct the full path to the file
        file_path = os.path.join(confPath, filename)
        # Remove the file
        os.remove(file_path)
        print(f'Removed: {file_path}')


#Remove Txt file for Q

confDirectory  = "../Data/0_qRelationship"
confPath = os.path.realpath(confDirectory)
#print(confPath)

for filename in os.listdir(confPath):
    # Check if the file is a .txt file
    if filename.endswith('.txt'):
        # Construct the full path to the file
        file_path = os.path.join(confPath, filename)
        # Remove the file
        os.remove(file_path)
        print(f'Removed: {file_path}')


#Remove Txt file for Q

confDirectory = '../../media/uploads/0_Data'
confPath = os.path.realpath(confDirectory)
#print(confPath)

for filename in os.listdir(confPath):
    # Check if the file is a .txt file
    if filename.endswith('.csv'):
        # Construct the full path to the file
        file_path = os.path.join(confPath, filename)
        # Remove the file
        os.remove(file_path)
        print(f'Removed: {file_path}')


for filename in os.listdir(confPath):
    if filename.endswith('.xlsx'):
        # Construct the full path to the file
        file_path = os.path.join(confPath, filename)
        # Remove the file
        os.remove(file_path)
        print(f'Removed: {file_path}')


import os
downloadDir = "../../media/download/dfgTool"
new_directory_path = os.path.realpath(downloadDir)
if not os.path.exists(new_directory_path):
    os.mkdir(new_directory_path)


