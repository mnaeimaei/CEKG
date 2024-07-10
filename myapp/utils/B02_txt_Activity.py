
def txt_activity():
    import os
    import A1_Scenario_Step2 as clN

    Activity=clN.Activity

    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    print(confPath)

    FilePath = confPath + "/" + Activity + ".txt"
    print("FilePath=", FilePath)
    print("Activity=", Activity)

    if Activity == "Activity_Label" or Activity == "Concept_Label":
        pass

    if Activity == "Concept_Label_Level":
        with open(FilePath, 'w') as file:
            pass

        while True:
            try:
                distanceFrom_ActConc = int(input("Enter the distance from SCT Activity? "))
                break
            except ValueError:
                print("Only integer input is acceptable. Please try again.")
        with open(FilePath, 'a') as file:
            file.write(f'''distanceFrom_ActConc=''' + str(distanceFrom_ActConc))

    import subprocess

    subprocess.run(['python', 'N04_Step30_DK5_Mapper_importingNeo4J.py'])
    subprocess.run(['python', 'O04_Step32_DK6_Tied_importingNeo4J.py'])
    subprocess.run(['python', 'P04_Step34_DK7_Bond_importingNeo4J.py'])
    subprocess.run(['python', 'Q04_Step2_DFG_importingNeo4J_Scneario.py'])


