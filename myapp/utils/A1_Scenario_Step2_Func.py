

def returnSelection():
    import os
    confDirectory  = "../Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)
    inputTex_FilePath = confPath + "/" + "0_Selection.txt"

    with open(inputTex_FilePath, 'r') as file:
        # Read the file line by line
        ListEnDFSHow = []
        for line in file:
            variable_name, value = line.split('=')
            variable_name = variable_name.strip()
            value = int(value.strip())
            if variable_name == 'DFG_Selection':
                DFG_Selection=value
            if variable_name == 'Input_Selection':
                Input_Selection=value
            if variable_name == 'Activity_Selection':
                Activity_Selection=value

    return DFG_Selection,Input_Selection,Activity_Selection
