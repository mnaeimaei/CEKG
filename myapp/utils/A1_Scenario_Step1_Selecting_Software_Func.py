

def readFile():
    import json
    import os
    confDirectory  = "../Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)
    inputTex_FilePath = confPath + "/" + "0_preSelection.txt"
    with open(inputTex_FilePath, 'r') as file:
        for line in file:
            data = json.loads(line)

            if 'mainDfgMode' in data:
                mainDfgMode = data['mainDfgMode']
                print(mainDfgMode)

            if mainDfgMode in data:
                DFG_Selection=data[mainDfgMode]
                print("DFG_Selection=",DFG_Selection)

            if "inputMode" in data:
                Input_Selection=data["inputMode"]
                if Input_Selection =="":
                    Input_Selection=1
                print("Input_Selection=", Input_Selection)

            if "activityMode" in data:
                Activity_Selection=data["activityMode"]
                if Activity_Selection =="":
                    Activity_Selection=1
                print("Activity_Selection=", Activity_Selection)

    inputTex_FilePath2 = confPath + "/" + "0_Selection.txt"
    with open(inputTex_FilePath2, 'w') as file:
        file.write(f'''DFG_Selection={DFG_Selection}''' + "\n")
        file.write(f'''Input_Selection={Input_Selection}''' + "\n")
        file.write(f'''Activity_Selection={Activity_Selection}''' + "\n")





########################################################################################
########################################################################################
########################################################################################

