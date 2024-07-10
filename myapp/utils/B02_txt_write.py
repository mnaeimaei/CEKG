
def createEmptyGeneralFile(FilaeName):

    import os

    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    print(confPath)

    DFG_FilePath = confPath + "/" + FilaeName + "_general.txt"
    print("DFG=", FilaeName)

    with open(DFG_FilePath, 'w') as file:
        pass

    return DFG_FilePath


'''
DFG_FilePath=txtW.createEmptyGeneralFile(DFG)
print("DFG_FilePath=", DFG_FilePath)

'''


def writeEntityDFShiw(DFG_FilePath, EnNum, entityList,typeNumber):
    #Default (Enter) = 1
    TypeShow = []
    for i in range(EnNum):
        TypeEntityShow = None
        while TypeEntityShow not in ["",'1', '0']:
            # Prompt the user for input
            TypeEntityShow = input(
                f'''Please enter 1 if you want to show entity {entityList[i]} in DFG, or enter 0 if you do not:''')
            # If user presses enter without any input, default to '1'
            if TypeEntityShow == "":
                TypeEntityShow = '1'
            if TypeEntityShow not in ["", '1', '0']:
                print("Invalid input. Please enter 1 or 0.")
        with open(DFG_FilePath, 'a') as file:
            file.write(f'''Type{typeNumber}_Entity{i + 1}_DF_Show=''' + str(TypeEntityShow) + "\n")
        TypeShow.append(TypeEntityShow)

    return TypeShow



'''
TypeShow=txtW.writeEntityDFShiw(DFG_FilePath, EnNum, entityList,1)
print("TypeShow=", TypeShow)

Type1_Entity1_DF_Show=1
Type1_Entity2_DF_Show=1
Type1_Entity3_DF_Show=1

'''
def writeIDSelection(DFG_FilePath,typeNumber):
    Type_selection = None
    while Type_selection not in ["",'Y', 'N','y', 'n']:
        Type_selection = input(f'''Do you want to show specific IDs of an Entity (Y/N)?''')
        if Type_selection not in ["",'Y', 'N','y', 'n']:
            print("Invalid input. Please enter Y or N.")

    print(Type_selection)
    with open(DFG_FilePath, 'a') as file:
        if Type_selection == "y" or Type_selection == "Y" :
            file.write(f'''Type{typeNumber}_selection=True\n''')
        elif Type_selection == "n" or Type_selection == "N" or Type_selection == "":
            file.write(f'''Type{typeNumber}_selection=False\n''')
    return Type_selection

'''
Type_selection=txtW.writeIDSelection(DFG_FilePath, 1)
print("Type_selection=", Type_selection)

Type1_selection=False
'''




def writeIDSelectionInstance(Type_selection,entityList,TypeShow,DFG_FilePath,typeNumber):
    ListA = []
    ListB = []

    if Type_selection == "y" or Type_selection == "Y":
        print("yes")
        for i, j in zip(entityList, TypeShow):
            if j == '1':
                Type_selection_ID = None
                while Type_selection_ID not in ['Y', 'N', 'y', 'n']:
                    Type_selection_ID = input(f'''Do you want to show specific IDs of for Domain "{i}" (Y/N)?''')
                    if Type_selection_ID not in ['Y', 'N', 'y', 'n']:
                        print("Invalid input. Please enter Y or N.")
                if Type_selection_ID == "y" or Type_selection_ID == "Y":
                    ListA.append(i)
                    Type_selection_ID_instances = input(f'''Enter the IDs of "{i}" (for example 1,2)?''')
                    ListB.append(Type_selection_ID_instances.split(","))

    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_selection_ID=''' + str(ListA) + "\n")
        file.write(f'''Type{typeNumber}_selection_ID_instances=''' + str(ListB) + "\n")




'''
txtW.writeIDSelectionInstance(Type_selection,entityList,TypeShow,DFG_FilePath,1)

Type1_selection_ID=['Patient', 'Admission', 'Concept']
Type1_selection_ID_instances=[['1', '2'], ['1'], ['6']]

or

Type1_selection_ID=[]
Type1_selection_ID_instances=[]

'''


def writeDomainIDSelection(DFG_FilePath,typeNumber):
    Type_selection = None
    while Type_selection not in ["",'Y', 'N','y', 'n']:
        Type_selection = input(f'''Do you want to show specific IDs of an Domain (Y/N)?''')
        if Type_selection not in ["",'Y', 'N','y', 'n']:
            print("Invalid input. Please enter Y or N.")

    print(Type_selection)
    with open(DFG_FilePath, 'a') as file:
        if Type_selection == "y" or Type_selection == "Y" :
            file.write(f'''Type{typeNumber}_Domain_selection=True\n''')
        elif Type_selection == "n" or Type_selection == "N" or Type_selection == "":
            file.write(f'''Type{typeNumber}_Domain_selection=False\n''')
    return Type_selection

'''
Type_Domain_selection=txtW.writeDomainIDSelection(DFG_FilePath, 1)
print("Type1_Domain_selection=", Type_Domain_selection)

Type1_selection=False
'''

def writeIDDomainSelectionInstance(Type_Domain_selection,DFG_FilePath,DomainNode,domainColTitle,typeNumber):
    ListA = []


    if Type_Domain_selection.lower() == "y":  # Simplified check for 'y' or 'Y'
        import A5_EntryCol_Step3_Step as cl1
        driver = cl1.driver
        query1 = f'''     
                 MATCH p=()-[r:TYPE_OF]->(n:{DomainNode}) 
                with distinct n.{domainColTitle} as S
                RETURN distinct collect (S)
                        '''
        print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            record2 = record1[0][0]

        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input(
                "Please enter the number(s) corresponding to the semantic Tag(s) of concept (separated by commas, press Enter for default 1): ")

            # Handling default choice or multiple selections
            if user_input == "":
                print("Default choice selected: 1")
                ListA.append(record2[0])
                break
            else:
                try:
                    user_choices = [int(choice.strip()) for choice in user_input.split(',')]
                    # Ensure all choices are unique and within the valid range
                    valid_choices = set(filter(lambda x: 1 <= x <= len(record2), user_choices))
                    if not valid_choices:
                        raise ValueError("No valid choices entered.")

                    for choice in valid_choices:
                        answer = record2[choice - 1]
                        ListA.append(answer)
                        print(f"Selected: {answer}")


                    break
                except ValueError as e:
                    print(
                        f"Invalid input: {e}. Please enter integer numbers within the list's range, separated by commas if multiple.")


    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_Domain_ID=''' + str(ListA) + "\n")








'''
txtW.writeIDDomainSelectionInstance(Type_Domain_selection,DFG_FilePath,1)


Type1_Domain_ID = ["Transfer",...]
or
Type1_Domain_ID = []


'''


def writeIDSelectionTypeFeature(Type_selection,DFG_FilePath,typeNumber):
    Type = '0'
    if Type_selection == "y" or Type_selection == "Y":
        #Type = None
        while Type not in ["", '1', '2']:
            # Prompt the user for input
            Type = input(
                f'''Please enter 1 if you want to select approach 1, or enter 2 for approach 2 (default is 2).:''')
            if Type == "":
                Type = '0'
            if Type not in ["", '1', '2']:
                print("Invalid input. Please enter 1 or 2.")

    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_approach=''' + str(Type) + "\n")

    return Type


'''
Type_approach=txtW.writeIDSelectionTypeFeature(Type_selection, DFG_FilePath, 1)
print("Type1_approach=", Type_approach)

Type1_approach=2


'''

def writeIDSelectionInstancefeature(Type_approach,entityList,TypeShow,DFG_FilePath,typeNumber):
    ListA = []
    ListB = []
    ListC = []
    ListD = []
    ListE = []


    if Type_approach == "1":
        print("yes")
        for i, j in zip(entityList, TypeShow):
            if j == '1':
                Type_selection_ID = None
                while Type_selection_ID not in ['Y', 'N', 'y', 'n']:
                    Type_selection_ID = input(f'''Do you want to show specific IDs of for Domain "{i}" (Y/N)?''')
                    if Type_selection_ID not in ['Y', 'N', 'y', 'n']:
                        print("Invalid input. Please enter Y or N.")
                if Type_selection_ID == "y" or Type_selection_ID == "Y":
                    ListA.append(i)
                    Type_selection_ID_instances = input(f'''Enter the IDs of "{i}" (for example 1,2)?''')
                    ListB.append(Type_selection_ID_instances.split(","))

    if Type_approach == "2":
        ###############PartA
        for i, value in enumerate(entityList, start=1):
            print(f"{i}. {value}")

        # Asking the user for their choice
        while True:
            user_input = input("Please enter an Entity  (Press Enter for random'): ")

            # Condition for default choice
            if user_input == "":
                print("random choice selected")
                answer1 = entityList[0]
                ListA.append(answer1)
                break

            # Validating the input to ensure it's an integer
            elif user_input.isdigit():
                user_choice = int(user_input)
                # Checking if the choice is within the valid range
                if 1 <= user_choice <= len(entityList):
                    answer1 = entityList[user_choice - 1]
                    ListA.append(answer1)
                    print(f"You have chosen: {entityList[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")



        ###############PartC
        import A5_EntryCol_Step3_Step as cl1
        driver = cl1.driver
        query1 = f'''     
                MATCH p=()-[r:Assign]->(n:Feature) 
                with distinct n.Name as S
                RETURN distinct collect (S)
                                '''
        print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            record2 = record1[0][0]

        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input("Please enter the number corresponding to feature of that entity  (Press Enter for random'): ")

            if user_input == "":
                print("random choice selected")
                answer2 = record2[0]
                ListC.append(answer2)
                break

            elif user_input.isdigit():
                user_choice = int(user_input)
                if 1 <= user_choice <= len(record2):
                    answer2=record2[user_choice-1]
                    ListC.append(answer2)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        ###############PartD

        query2 = f'''     
                    MATCH p=()-[r:Assign]->(n:Feature) where n.Name="{answer2}"
                  with distinct n.label as S
                    RETURN distinct collect (S)
                                        '''
        print(query2)
        with driver.session() as session:
            record1 = session.run(query2).values()
            record3 = record1[0][0]

        for i, value in enumerate(record3, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input(f'''Please enter the number corresponding label for {answer2}  (Press Enter for random'): ''')

            # Handling default choice or multiple selections
            if user_input == "":
                print("Default choice selected")
                answer3 = record3[0]
                ListD.append(answer3)
                break
            else:
                try:
                    user_choices = [int(choice.strip()) for choice in user_input.split(',')]
                    # Ensure all choices are unique and within the valid range
                    valid_choices = set(filter(lambda x: 1 <= x <= len(record3), user_choices))
                    if not valid_choices:
                        raise ValueError("No valid choices entered.")

                    for choice in valid_choices:
                        answer3 = record3[choice - 1]
                        ListD.append(answer3)
                        print(f"Selected: {answer3}")

                    break
                except ValueError as e:
                    print(
                        f"Invalid input: {e}. Please enter integer numbers within the list's range, separated by commas if multiple.")

        ###############PartE
        for eachLabel in ListD:

            query3 = f'''     
                        MATCH p=()-[r:Assign]->(n:Feature) where n.Name="{answer2}" and n.label="{eachLabel}"
                      with distinct n.Value as S
                        RETURN distinct collect (S)
                                            '''
            print(query3)

            with driver.session() as session:
                record11 = session.run(query3).values()
                record33 = record11[0][0]

            for i, value in enumerate(record33, start=1):
                print(f"{i}. {value}")

            # Asking the user for their choice
            while True:
                user_input = input(f'''Please enter the number corresponding to value for {answer2} with {eachLabel} (Press Enter for random'): ''')

                # Condition for default choice
                if user_input == "":
                    print("random choice selected")
                    answer4 = record33[0]
                    ListE.append(answer4)
                    break

                # Validating the input to ensure it's an integer
                elif user_input.isdigit():
                    user_choice = int(user_input)
                    # Checking if the choice is within the valid range
                    if 1 <= user_choice <= len(record33):
                        answer4 = record33[user_choice - 1]
                        ListE.append(answer4)
                        print(f"You have chosen: {record33[user_choice - 1]}")
                        break
                    else:
                        print("Please enter a number within the list's range.")
                else:
                    print("Invalid input. Please enter an integer number.")


    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_selection_ID=''' + str(ListA) + "\n")
        file.write(f'''Type{typeNumber}_selection_ID_instances=''' + str(ListB) + "\n")
        file.write(f'''Type{typeNumber}_feature_Name=''' + str(ListC) + "\n")
        file.write(f'''Type{typeNumber}_feature_label=''' + str(ListD) + "\n")
        file.write(f'''Type{typeNumber}_feature_Value=''' + str(ListE) + "\n")



'''


txtW.writeIDSelectionInstancefeature(Type_approach,Type_selection,entityList,TypeShow,DFG_FilePath,1)

'''



def writeIntraEntityDFShiw(Selection,DFG_FilePath, EnNum, entityList,typeNumber):
    #Default (Enter) = 1
    TypeShow = []
    for i,eachEntity in zip(range(EnNum),Selection) :
        if eachEntity=="1":
            print("yes")
            TypeEntityShow = None
            while TypeEntityShow not in ["",'1', '0']:
                # Prompt the user for input
                TypeEntityShow = input(
                    f'''Please enter 1 if you want to show intra relationship for {entityList[i]} in DFG, or enter 0 if you do not:''')
                # If user presses enter without any input, default to '1'
                if TypeEntityShow == "":
                    TypeEntityShow = '1'
                if TypeEntityShow not in ["", '1', '0']:
                    print("Invalid input. Please enter 1 or 0.")
            with open(DFG_FilePath, 'a') as file:
                file.write(f'''Type{typeNumber}_Entity{i + 1}OrgRel_DF_Show=''' + str(TypeEntityShow) + "\n")
            TypeShow.append(TypeEntityShow)
        else:
            with open(DFG_FilePath, 'a') as file:
                file.write(f'''Type{typeNumber}_Entity{i + 1}OrgRel_DF_Show=0''' + "\n")
            TypeShow.append("0")

    return TypeShow



'''
TypeShowIntra=txtW.writeIntraEntityDFShiw(DFG_FilePath, EnNum, entityList,1)
print("TypeShowIntra=", TypeShowIntra)

Type2_Entity1OrgRel_DF_Show = 1
Type2_Entity2OrgRel_DF_Show = 1
Type2_Entity3OrgRel_DF_Show = 1

'''

def writeCount(DFG_FilePath,typeNumber):
    while True:
        user_input = input("Please enter the minimum number of aggregated relationship (At least 0): ")
        if user_input.isdigit():
            number = int(user_input)
            if number >= 0:
                print(f"You have entered: {number}")
                break
            else:
                print("The number must be 0 or higher. Please try again.")
        else:
            print("Invalid input. Please enter a valid integer number.")

    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_Count=''' + str(number) +  "\n")




'''
txtW.writeCount(DFG_FilePath,3)
'''


def writeTypeNumber(DFG_FilePath,typeNumber):
    TypeEntityShow = None
    while TypeEntityShow not in ["",'1', '2']:
        # Prompt the user for input
        TypeEntityShow = input(
            f'''Please chose one 
            1 : RelateveAndAbsolute
            2: OnlyAbsolute (non Relative)
            ?''')
        if TypeEntityShow == "":
            TypeEntityShow = '1'
        if TypeEntityShow not in ["", '1', '2']:
            print("Invalid input. Please enter 1 or 2.")
    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}=''' + str(TypeEntityShow) + "\n")
    return TypeEntityShow




'''
txtW.writeTypeNumber(DFG_FilePath,3)
'''




def writeIDSelectionNonRelative(DFG_FilePath,typeNumber):
    Type_selection = None
    while Type_selection not in ["",'Y', 'N','y', 'n']:
        Type_selection = input(f'''Do you want to show specific IDs of an Entity (Y/N)?''')
        if Type_selection not in ["",'Y', 'N','y', 'n']:
            print("Invalid input. Please enter Y or N.")

    print(Type_selection)
    with open(DFG_FilePath, 'a') as file:
        if Type_selection == "y" or Type_selection == "Y" :
            file.write(f'''Type{typeNumber}_non_Relative_selection=True\n''')
        elif Type_selection == "n" or Type_selection == "N" or Type_selection == "":
            file.write(f'''Type{typeNumber}_non_Relative_selection=False\n''')
    return Type_selection

'''
Type_selection=txtW.writeIDSelectionNonRelative(DFG_FilePath, 1)
print("Type_selection=", Type_selection)

Type1_selection=False
'''


def writeIDSelectionTypeNonRelative(Type_selection,DFG_FilePath,typeNumber):
    Type = '0'
    if Type_selection == "y" or Type_selection == "Y":
        #Type = None
        while Type not in ["", '1', '2']:
            # Prompt the user for input
            Type = input(
                f'''Please enter 1 if you want to select approach 1, or enter 2 for approach 2 (default is 2).:''')
            if Type == "":
                Type = '0'
            if Type not in ["", '1', '2']:
                print("Invalid input. Please enter 1 or 2.")

    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_non_Relative_approach=''' + str(Type) + "\n")

    return Type


'''
Type_approach=txtW.writeIDSelectionTypeNonRelative(Type_selection, DFG_FilePath, 1)
print("Type1_approach=", Type_approach)

Type1_approach=2


'''



def writeIDSelectionInstancefeatureType3(Type_approach,entityList,TypeShow,DFG_FilePath,typeNumber):
    ListA = []
    ListB = []
    ListC = []
    ListD = []


    if Type_approach == "1":
        print("yes")
        for i, j in zip(entityList, TypeShow):
            if j == '1':
                Type_selection_ID = None
                while Type_selection_ID not in ['Y', 'N', 'y', 'n']:
                    Type_selection_ID = input(f'''Do you want to show specific IDs of for Domain "{i}" (Y/N)?''')
                    if Type_selection_ID not in ['Y', 'N', 'y', 'n']:
                        print("Invalid input. Please enter Y or N.")
                if Type_selection_ID == "y" or Type_selection_ID == "Y":
                    Type_selection_ID_instances = input(f'''Enter the IDs of "{i}" (for example 1,2)?''')
                    ListA.append(Type_selection_ID_instances.split(","))

    if Type_approach == "2":

        ###############PartC
        import A5_EntryCol_Step3_Step as cl1
        driver = cl1.driver
        query1 = f'''     
                MATCH p=()-[r:Assign]->(n:Feature) 
                with distinct n.Name as S
                RETURN distinct collect (S)
                                '''
        print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            record2 = record1[0][0]

        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input("Please enter the number corresponding to feature  (Press Enter for random'): ")

            if user_input == "":
                print("random choice selected")
                answer2 = record2[0]
                ListB.append(answer2)
                break

            elif user_input.isdigit():
                user_choice = int(user_input)
                if 1 <= user_choice <= len(record2):
                    answer2=record2[user_choice-1]
                    ListB.append(answer2)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        ###############PartD

        query2 = f'''     
                    MATCH p=()-[r:Assign]->(n:Feature) where n.Name="{answer2}"
                  with distinct n.label as S
                    RETURN distinct collect (S)
                                        '''
        print(query2)
        with driver.session() as session:
            record1 = session.run(query2).values()
            record3 = record1[0][0]

        for i, value in enumerate(record3, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input("Please enter the number corresponding to label  (Press Enter for random'): ")

            # Handling default choice or multiple selections
            if user_input == "":
                print("Default choice selected")
                answer3 = record3[0]
                ListC.append(answer3)
                break
            else:
                try:
                    user_choices = [int(choice.strip()) for choice in user_input.split(',')]
                    # Ensure all choices are unique and within the valid range
                    valid_choices = set(filter(lambda x: 1 <= x <= len(record3), user_choices))
                    if not valid_choices:
                        raise ValueError("No valid choices entered.")

                    for choice in valid_choices:
                        answer3 = record3[user_choice - 1]
                        ListC.append(answer3)
                        print(f"Selected: {answer3}")

                    break
                except ValueError as e:
                    print(
                        f"Invalid input: {e}. Please enter integer numbers within the list's range, separated by commas if multiple.")

        ###############PartE
        for eachLabel in ListC:

            query3 = f'''     
                        MATCH p=()-[r:Assign]->(n:Feature) where n.Name="{answer2}" and n.label="{eachLabel}"
                      with distinct n.Value as S
                        RETURN distinct collect (S)
                                            '''
            print(query3)

            with driver.session() as session:
                record11 = session.run(query3).values()
                record33 = record11[0][0]

            for i, value in enumerate(record33, start=1):
                print(f"{i}. {value}")

            # Asking the user for their choice
            while True:
                user_input = input("Please enter the number corresponding to label value  (Press Enter for random'): ")

                # Condition for default choice
                if user_input == "":
                    print("random choice selected")
                    answer4 = record33[0]
                    ListD.append(answer4)
                    break

                # Validating the input to ensure it's an integer
                elif user_input.isdigit():
                    user_choice = int(user_input)
                    # Checking if the choice is within the valid range
                    if 1 <= user_choice <= len(record33):
                        answer4 = record33[user_choice - 1]
                        ListD.append(answer4)
                        print(f"You have chosen: {record33[user_choice - 1]}")
                        break
                    else:
                        print("Please enter a number within the list's range.")
                else:
                    print("Invalid input. Please enter an integer number.")


    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_non_Relative_selection_ID_instances=''' + str(ListA) + "\n")
        file.write(f'''Type{typeNumber}_non_Relative_selection_feature_Name=''' + str(ListB) + "\n")
        file.write(f'''Type{typeNumber}_non_Relative_selection_feature_label=''' + str(ListC) + "\n")
        file.write(f'''Type{typeNumber}_non_Relative_selection_feature_Value=''' + str(ListD) + "\n")





'''


txtW.writeIDSelectionInstancefeatureType3(Type_approach,Type_selection,entityList,TypeShow,DFG_FilePath,1)

'''




def writeEntityDFShiwType4(DFG_FilePath, entityList,typeNumber):
    import random
    for i, value in enumerate(entityList, start=1):
        print(f"{i}. {value}")

    selection_marks = [0] * len(entityList)  # Initialize all selections with 0

    while True:
        user_input = input("Please enter the number corresponding to feature (Press Enter for random): ")

        if user_input == "":
            print("Random choice selected")
            random_choice_index = random.randint(0, len(entityList) - 1)
            selection_marks[random_choice_index] = 1
            print(f"Randomly selected: {entityList[random_choice_index]}")
            break

        elif user_input.isdigit():
            user_choice = int(user_input)
            if 1 <= user_choice <= len(entityList):
                selection_marks[user_choice - 1] = 1  # Mark the selected feature with 1
                print(f"You have chosen: {entityList[user_choice - 1]}")
                break
            else:
                print("Please enter a number within the list's range.")
        else:
            print("Invalid input. Please enter an integer number.")

    for item, j in zip(selection_marks,range(len(entityList))):
        print(item)
        with open(DFG_FilePath, 'a') as file:
            file.write(f'''Type{typeNumber}_Entity{j + 1}_DF_Show=''' + str(item) + "\n")


    return selection_marks




'''
TypeShow=txtW.writeEntityDFShiwType4(DFG_FilePath, EnNum, entityList,1)
print("TypeShow=", TypeShow)

Type1_Entity1_DF_Show=1
Type1_Entity2_DF_Show=1
Type1_Entity3_DF_Show=1

'''


def writeIDSelectionInstanceType4(Type_selection,entityList,TypeShow,DFG_FilePath,typeNumber):
    ListA = []

    if Type_selection == "y" or Type_selection == "Y":
        Type_selection_ID_instances = input(f'''Enter the IDs (for example 1,2)?''')
        ListA.extend(Type_selection_ID_instances.split(","))

    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_selection_ID_instances=''' + str(ListA) + "\n")








def writeIDSelectionInstancefeatureType4(Type_approach,entityList,TypeShow,DFG_FilePath,typeNumber):
    ListA = []
    ListB = []
    ListC = []
    ListD = []
    ListE = []


    if Type_approach == "1":
        print("sADas")
        for i, j in zip(entityList, TypeShow):
            if j == 1:
                ListA.append(i)
                Type_selection_ID_instances = input(f'''Enter the IDs of "{i}" (for example 1,2)?''')
                ListB.extend(Type_selection_ID_instances.split(","))


    if Type_approach == "2":
        for i, j in zip(entityList, TypeShow):
            if j == 1:
                ListA.append(i)


        ###############PartC
        import A5_EntryCol_Step3_Step as cl1
        driver = cl1.driver
        query1 = f'''     
                MATCH p=()-[r:Assign]->(n:Feature) 
                with distinct n.Name as S
                RETURN distinct collect (S)
                                '''
        print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            record2 = record1[0][0]

        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input("Please enter the number corresponding to feature  (Press Enter for random'): ")

            if user_input == "":
                print("random choice selected")
                answer2 = record2[0]
                ListC.append(answer2)
                break

            elif user_input.isdigit():
                user_choice = int(user_input)
                if 1 <= user_choice <= len(record2):
                    answer2=record2[user_choice-1]
                    ListC.append(answer2)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        ###############PartD

        query2 = f'''     
                    MATCH p=()-[r:Assign]->(n:Feature) where n.Name="{answer2}"
                  with distinct n.label as S
                    RETURN distinct collect (S)
                                        '''
        print(query2)
        with driver.session() as session:
            record1 = session.run(query2).values()
            record3 = record1[0][0]

        for i, value in enumerate(record3, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input("Please enter the number corresponding to label  (Press Enter for random'): ")

            # Handling default choice or multiple selections
            if user_input == "":
                print("Default choice selected")
                answer3 = record3[0]
                ListD.append(answer3)
                break
            else:
                try:
                    user_choices = [int(choice.strip()) for choice in user_input.split(',')]
                    # Ensure all choices are unique and within the valid range
                    valid_choices = set(filter(lambda x: 1 <= x <= len(record3), user_choices))
                    if not valid_choices:
                        raise ValueError("No valid choices entered.")

                    for choice in valid_choices:
                        answer3 = record3[user_choice - 1]
                        ListD.append(answer3)
                        print(f"Selected: {answer3}")

                    break
                except ValueError as e:
                    print(
                        f"Invalid input: {e}. Please enter integer numbers within the list's range, separated by commas if multiple.")

        ###############PartE
        for eachLabel in ListD:

            query3 = f'''     
                        MATCH p=()-[r:Assign]->(n:Feature) where n.Name="{answer2}" and n.label="{eachLabel}"
                      with distinct n.Value as S
                        RETURN distinct collect (S)
                                            '''
            print(query3)

            with driver.session() as session:
                record11 = session.run(query3).values()
                record33 = record11[0][0]

            for i, value in enumerate(record33, start=1):
                print(f"{i}. {value}")

            # Asking the user for their choice
            while True:
                user_input = input("Please enter the number corresponding to label value  (Press Enter for random'): ")

                # Condition for default choice
                if user_input == "":
                    print("random choice selected")
                    answer4 = record33[0]
                    ListE.append(answer4)
                    break

                # Validating the input to ensure it's an integer
                elif user_input.isdigit():
                    user_choice = int(user_input)
                    # Checking if the choice is within the valid range
                    if 1 <= user_choice <= len(record33):
                        answer4 = record33[user_choice - 1]
                        ListE.append(answer4)
                        print(f"You have chosen: {record33[user_choice - 1]}")
                        break
                    else:
                        print("Please enter a number within the list's range.")
                else:
                    print("Invalid input. Please enter an integer number.")


        query7 = f'''     
        MATCH (e:Event)-[r:Assign]->(f:Feature) 
        WHERE e.Activity = f.Name 
        AND f.Name = "{ListC[0]}" 
        AND f.label IN {ListD}
        AND f.Value IN {ListE}
        WITH id(f) as x, collect(DISTINCT e.Event) AS events
        WITH collect(events) AS allEvents
        with reduce(commonEvents = allEvents[0], events IN tail(allEvents) | apoc.coll.intersection(commonEvents, events)) as value
        UNWIND range(0,size(value)-1) AS i
        MATCH (n )<-[:CORR]-(e:Event)
        where n.Category = "Absolute" and e.Event=value[i] 
        return labels(n)[0], collect(DISTINCT n.ID) as ID
            '''
        print(query7)
        with driver.session() as session:
            record7 = session.run(query7).values()
            # print("record7=", record7)



        compare1 = []
        for any in record7:
            if ListA[0] in any[0]:
                compare1.append(any[1])
        print("compare1=", compare1)
        ListB=compare1[0]


    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_selection_ID=''' + str(ListA) + "\n")
        file.write(f'''Type{typeNumber}_selection_ID_instances=''' + str(ListB) + "\n")
        file.write(f'''Type{typeNumber}_selection_feature_Name=''' + str(ListC) + "\n")
        file.write(f'''Type{typeNumber}_selection_feature_label=''' + str(ListD) + "\n")
        file.write(f'''Type{typeNumber}_selection_feature_Value=''' + str(ListE) + "\n")





def writeEntityDFShowType5(DFG_FilePath, EnNum, entityList,typeNumber):
    def get_user_choice(prompt_message, exclude=None):
        while True:
            for i, value in enumerate(entityList, start=1):
                if value != exclude:  # Do not display the option if it's meant to be excluded
                    print(f"{i}. {value}")

            user_input = input(prompt_message)

            if user_input.isdigit():
                user_choice = int(user_input)
                if 1 <= user_choice <= len(entityList):
                    selected_value = entityList[user_choice - 1]
                    if selected_value == exclude:
                        print("This choice has already been selected. Please choose a different item.")
                        continue
                    print(f"You have chosen: {selected_value}")
                    return selected_value
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

    # Prompt the user for the first item
    firstItem = get_user_choice("Please enter the number corresponding to the first item: ")

    # Prompt the user for the second item, excluding the first choice
    secondItem = get_user_choice("Please enter the number corresponding to the second item: ", exclude=firstItem)

    # Assigning the selected items to variables
    Type5_Rel_1_DF_Show = firstItem
    Type5_Rel_2_DF_Show = secondItem

    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type5_Rel_1_DF_Show=\"''' + str(firstItem) + "\"" + "\n")
        file.write(f'''Type5_Rel_2_DF_Show=\"''' + str(secondItem) + "\"" +"\n")



    return Type5_Rel_1_DF_Show, Type5_Rel_2_DF_Show


def writeIDSelectionNonRelativT5(DFG_FilePath,typeNumber,typeNumber2):
    Type_selection = None
    while Type_selection not in ["",'Y', 'N','y', 'n']:
        Type_selection = input(f'''Do you want to show specific IDs of an Entity (Y/N)?''')
        if Type_selection not in ["",'Y', 'N','y', 'n']:
            print("Invalid input. Please enter Y or N.")

    print(Type_selection)
    with open(DFG_FilePath, 'a') as file:
        if Type_selection == "y" or Type_selection == "Y" :
            file.write(f'''Type{typeNumber}_Rel_{typeNumber2}_DF_Show_selection=True\n''')
        elif Type_selection == "n" or Type_selection == "N" or Type_selection == "":
            file.write(f'''Type{typeNumber}_Rel_{typeNumber2}_DF_Show_selection=False\n''')
    return Type_selection


def writeIDSelectionInstanceType5(Type_selection,entityList,TypeShow,DFG_FilePath,typeNumber,typeNumber2):
    ListA = []

    if Type_selection == "y" or Type_selection == "Y":
        Type_selection_ID_instances = input(f'''Enter the IDs (for example 1,2)?''')
        ListA.extend(Type_selection_ID_instances.split(","))

    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_Rel_{typeNumber2}_DF_Show_selection_ID_instances=''' + str(ListA) + "\n")



def writeIDSelectionInstancefeatureType5(Type_approach,TypeShow,Type_selection_ID, DFG_FilePath,Entity1,typeNumber):
    ListA = []
    ListC = []
    ListD = []
    ListE = []

    if Type_approach == "1":
        print("yes")
        if Type_selection_ID == "y" or Type_selection_ID == "Y":
            Type_selection_ID_instances = input(f'''Enter the IDs of Type5_Rel_1_DF_Show (for example 1,2)?''')
            ListA.extend(Type_selection_ID_instances.split(","))

    if Type_approach == "2":
        ###############PartA


        ###############PartC
        import A5_EntryCol_Step3_Step as cl1
        driver = cl1.driver
        query1 = f'''     
                MATCH p=()-[r:Assign]->(n:Feature) 
                with distinct n.Name as S
                RETURN distinct collect (S)
                                '''
        print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            record2 = record1[0][0]

        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input("Please enter the number corresponding to feature  (Press Enter for random'): ")

            if user_input == "":
                print("random choice selected")
                answer2 = record2[0]
                ListC.append(answer2)
                break

            elif user_input.isdigit():
                user_choice = int(user_input)
                if 1 <= user_choice <= len(record2):
                    answer2=record2[user_choice-1]
                    ListC.append(answer2)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        ###############PartD

        query2 = f'''     
                    MATCH p=()-[r:Assign]->(n:Feature) where n.Name="{answer2}"
                  with distinct n.label as S
                    RETURN distinct collect (S)
                                        '''
        print(query2)
        with driver.session() as session:
            record1 = session.run(query2).values()
            record3 = record1[0][0]

        for i, value in enumerate(record3, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input("Please enter the number corresponding to label  (Press Enter for random'): ")

            # Handling default choice or multiple selections
            if user_input == "":
                print("Default choice selected")
                answer3 = record3[0]
                ListD.append(answer3)
                break
            else:
                try:
                    user_choices = [int(choice.strip()) for choice in user_input.split(',')]
                    # Ensure all choices are unique and within the valid range
                    valid_choices = set(filter(lambda x: 1 <= x <= len(record3), user_choices))
                    if not valid_choices:
                        raise ValueError("No valid choices entered.")

                    for choice in valid_choices:
                        answer3 = record3[user_choice - 1]
                        ListD.append(answer3)
                        print(f"Selected: {answer3}")

                    break
                except ValueError as e:
                    print(
                        f"Invalid input: {e}. Please enter integer numbers within the list's range, separated by commas if multiple.")

        ###############PartE
        for eachLabel in ListD:

            query3 = f'''     
                        MATCH p=()-[r:Assign]->(n:Feature) where n.Name="{answer2}" and n.label="{eachLabel}"
                      with distinct n.Value as S
                        RETURN distinct collect (S)
                                            '''
            print(query3)

            with driver.session() as session:
                record11 = session.run(query3).values()
                record33 = record11[0][0]

            for i, value in enumerate(record33, start=1):
                print(f"{i}. {value}")

            # Asking the user for their choice
            while True:
                user_input = input("Please enter the number corresponding to label value  (Press Enter for random'): ")

                # Condition for default choice
                if user_input == "":
                    print("random choice selected")
                    answer4 = record33[0]
                    ListE.append(answer4)
                    break

                # Validating the input to ensure it's an integer
                elif user_input.isdigit():
                    user_choice = int(user_input)
                    # Checking if the choice is within the valid range
                    if 1 <= user_choice <= len(record33):
                        answer4 = record33[user_choice - 1]
                        ListE.append(answer4)
                        print(f"You have chosen: {record33[user_choice - 1]}")
                        break
                    else:
                        print("Please enter a number within the list's range.")
                else:
                    print("Invalid input. Please enter an integer number.")

        query1 = f'''     
        MATCH (e:Event)-[r:Assign]->(f:Feature) 
        WHERE e.Activity = f.Name 
        AND f.Name = "{ListC[0]}" 
        AND f.label IN {ListD}
        AND f.Value IN {ListE}
        WITH id(f) as x, collect(DISTINCT e.Event) AS events
        WITH collect(events) AS allEvents
        with reduce(commonEvents = allEvents[0], events IN tail(allEvents) | apoc.coll.intersection(commonEvents, events)) as value
        UNWIND range(0,size(value)-1) AS i
        MATCH (n )<-[:CORR]-(e:Event)
        where n.Category = "Absolute" and e.Event=value[i] 
        return labels(n)[0], collect(DISTINCT n.ID) as ID
            '''
        print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            # print("record1=", record1)

        compare1 = []
        for any in record1:
            if any[0]==Entity1:
                compare1.append(any[1])
        print("compare1=", compare1)
        ListA=compare1[0]


    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_Rel_1_DF_Show_selection_ID_instances=''' + str(ListA) + "\n")
        file.write(f'''Type{typeNumber}_Rel_1_DF_Show_selection_feature_Name=''' + str(ListC) + "\n")
        file.write(f'''Type{typeNumber}_Rel_1_DF_Show_selection_feature_label=''' + str(ListD) + "\n")
        file.write(f'''Type{typeNumber}_Rel_1_DF_Show_selection_feature_Value=''' + str(ListE) + "\n")





def writeIDSelectionInstanceType3(Type3,Type_selection,entityList,TypeShow,DFG_FilePath,typeNumber):
    ListA = []

    if Type3 == "2" and Type_selection == "Y" :
        for i, j in zip(entityList, TypeShow):
            if j == '1':
                Type_selection_ID = None
                while Type_selection_ID not in ['Y', 'N', 'y', 'n']:
                    Type_selection_ID = input(f'''Do you want to show specific IDs of for Domain "{i}" (Y/N)?''')
                    if Type_selection_ID not in ['Y', 'N', 'y', 'n']:
                        print("Invalid input. Please enter Y or N.")



                if Type_selection_ID == "n" or Type_selection_ID == "N":
                    ListA.append([])

                if Type_selection_ID == "y" or Type_selection_ID == "Y":
                    Type_selection_ID_instances = input(f'''Enter the IDs of "{i}" (for example 1,2)?''')
                    ListA.append(Type_selection_ID_instances.split(","))


    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type{typeNumber}_non_Relative_selection_ID_instances=''' + str(ListA) + "\n")
    return ListA



def writeIDSelectionNonRelativeType3(Type3, DFG_FilePath,typeNumber):

    if Type3 == '1' :
        Type_selection = "N"
        with open(DFG_FilePath, 'a') as file:
                file.write(f'''Type{typeNumber}_non_Relative_selection=False\n''')
        return Type_selection

    if Type3 == '2':
        Type_selection = None
        while Type_selection not in ["",'Y', 'N','y', 'n']:
            Type_selection = input(f'''Do you want to show specific IDs of an Entity (Y/N)?''')
            if Type_selection not in ["",'Y', 'N','y', 'n']:
                print("Invalid input. Please enter Y or N.")

        print(Type_selection)
        with open(DFG_FilePath, 'a') as file:
            if Type_selection == "y" or Type_selection == "Y" :
                Type_selection = "Y"

                file.write(f'''Type{typeNumber}_non_Relative_selection=True\n''')
            elif Type_selection == "n" or Type_selection == "N" or Type_selection == "":
                Type_selection = "N"
                file.write(f'''Type{typeNumber}_non_Relative_selection=False\n''')

            return Type_selection

def writeType3_non_Relative_approach(Type3, Type3_non_Relative_selection, DFG_FilePath,typeNumber):

    if Type3 == '1' :
        user_choice = 0
        with open(DFG_FilePath, 'a') as file:
                file.write(f'''Type{typeNumber}_non_Relative_approach=0\n''')
        return user_choice

    if Type3 == '2' and Type3_non_Relative_selection=="N":
        user_choice = 0
        with open(DFG_FilePath, 'a') as file:
                file.write(f'''Type{typeNumber}_non_Relative_approach=0\n''')
        return user_choice

    if Type3 == '2' and Type3_non_Relative_selection=="Y":

        while True:
            try:
                user_choice = int(input(
                    "Please select an option:\n- For selection based on entities ID, enter 1\n- For selection based on features, enter 2\nYour choice: "))
                if user_choice in [1, 2]:
                    break
                else:
                    print("Invalid input. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter an integer value (1 or 2).")

        print(f"You've selected option {user_choice}.")
        with open(DFG_FilePath, 'a') as file:
            file.write(f'''Type{typeNumber}_non_Relative_approach={user_choice}\n''')

            return user_choice

#######################################################

def writeInQ(FilaeName,Type,Type3_non_Relative_selection,Type3_non_Relative_selection_ID_instances):

    import os

    confDirectory  = "../Data/0_qRelationship"
    confPath = os.path.realpath(confDirectory)
    print(confPath)

    DFG_FilePath = confPath + "/" + FilaeName + ".txt"
    print("DFG=", FilaeName)


    if Type3_non_Relative_selection=="N":
        valueType="False"
    else:
        valueType="True"
    with open(DFG_FilePath, 'w') as file:
        file.write(f'''Type3={Type}\n''')
        file.write(f'''Type3_non_Relative_selection={valueType}\n''')
        file.write(f'''Type3_non_Relative_selection_ID_instances={Type3_non_Relative_selection_ID_instances}\n''')

    return DFG_FilePath


def writeInQTyep3Feature(FilaeName,Type,Type3_non_Relative_selection,Type3_non_Relative_selection_ID_instances):

    import os

    confDirectory  = "../Data/0_qRelationship"
    confPath = os.path.realpath(confDirectory)
    print(confPath)

    DFG_FilePath = confPath + "/" + FilaeName + ".txt"
    print("DFG=", FilaeName)


    if Type3_non_Relative_selection=="N":
        valueType="False"
    else:
        valueType="True"
    with open(DFG_FilePath, 'w') as file:
        file.write(f'''Type3={Type}\n''')
        file.write(f'''Type3_non_Relative_selection={valueType}\n''')
        file.write(f'''Type3_non_Relative_selection_ID_instances={Type3_non_Relative_selection_ID_instances}\n''')

    return DFG_FilePath




def writeIDSelectionInstancefeatureType3Feature(Type_approach,entityList,TypeShow,DFG_FilePath,typeNumber):
    ListA = []
    ListB = []
    ListC = []
    ListD = []

    if Type_approach == 0:
        with open(DFG_FilePath, 'a') as file:
            file.write(f'''Type{typeNumber}_non_Relative_selection_ID_instances=''' + str(ListA) + "\n")
            file.write(f'''Type{typeNumber}_non_Relative_selection_feature_Name=''' + str(ListB) + "\n")
            file.write(f'''Type{typeNumber}_non_Relative_selection_feature_label=''' + str(ListC) + "\n")
            file.write(f'''Type{typeNumber}_non_Relative_selection_feature_Value=''' + str(ListD) + "\n")


    if Type_approach == 1:
        print("yes")
        for i, j in zip(entityList, TypeShow):
            if j == '1':
                Type_selection_ID = None
                while Type_selection_ID not in ['Y', 'N', 'y', 'n']:
                    Type_selection_ID = input(f'''Do you want to show specific IDs of for Domain "{i}" (Y/N)?''')
                    if Type_selection_ID not in ['Y', 'N', 'y', 'n']:
                        print("Invalid input. Please enter Y or N.")
                if Type_selection_ID == "n" or Type_selection_ID == "N":
                    ListA.append([])

                if Type_selection_ID == "y" or Type_selection_ID == "Y":
                    Type_selection_ID_instances = input(f'''Enter the IDs of "{i}" (for example 1,2)?''')
                    ListA.append(Type_selection_ID_instances.split(","))

        with open(DFG_FilePath, 'a') as file:
            file.write(f'''Type{typeNumber}_non_Relative_selection_ID_instances=''' + str(ListA) + "\n")
            file.write(f'''Type{typeNumber}_non_Relative_selection_feature_Name=''' + str(ListB) + "\n")
            file.write(f'''Type{typeNumber}_non_Relative_selection_feature_label=''' + str(ListC) + "\n")
            file.write(f'''Type{typeNumber}_non_Relative_selection_feature_Value=''' + str(ListD) + "\n")

        return ListA

    if Type_approach == 2:

        ###############PartC
        import A5_EntryCol_Step3_Step as cl1
        driver = cl1.driver
        query1 = f'''     
                MATCH p=()-[r:Assign]->(n:Feature) 
                with distinct n.Name as S
                RETURN distinct collect (S)
                                '''
        print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            record2 = record1[0][0]

        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input("Please enter the number corresponding to feature  (Press Enter for random'): ")

            if user_input == "":
                print("random choice selected")
                answer2 = record2[0]
                ListB.append(answer2)
                break

            elif user_input.isdigit():
                user_choice = int(user_input)
                if 1 <= user_choice <= len(record2):
                    answer2=record2[user_choice-1]
                    ListB.append(answer2)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        ###############PartD

        query2 = f'''     
                    MATCH p=()-[r:Assign]->(n:Feature) where n.Name="{answer2}"
                  with distinct n.label as S
                    RETURN distinct collect (S)
                                        '''
        print(query2)
        with driver.session() as session:
            record1 = session.run(query2).values()
            record3 = record1[0][0]

        for i, value in enumerate(record3, start=1):
            print(f"{i}. {value}")

        while True:
            user_input = input("Please enter the number corresponding to label  (Press Enter for random'): ")

            # Handling default choice or multiple selections
            if user_input == "":
                print("Default choice selected")
                answer3 = record3[0]
                ListC.append(answer3)
                break
            else:
                try:
                    user_choices = [int(choice.strip()) for choice in user_input.split(',')]
                    # Ensure all choices are unique and within the valid range
                    valid_choices = set(filter(lambda x: 1 <= x <= len(record3), user_choices))
                    if not valid_choices:
                        raise ValueError("No valid choices entered.")

                    for choice in valid_choices:
                        answer3 = record3[choice - 1]
                        ListC.append(answer3)
                        print(f"Selected: {answer3}")

                    break
                except ValueError as e:
                    print(
                        f"Invalid input: {e}. Please enter integer numbers within the list's range, separated by commas if multiple.")

        ###############PartE
        for eachLabel in ListC:

            query3 = f'''     
                        MATCH p=()-[r:Assign]->(n:Feature) where n.Name="{answer2}" and n.label="{eachLabel}"
                      with distinct n.Value as S
                        RETURN distinct collect (S)
                                            '''
            print(query3)

            with driver.session() as session:
                record11 = session.run(query3).values()
                record33 = record11[0][0]

            for i, value in enumerate(record33, start=1):
                print(f"{i}. {value}")

            # Asking the user for their choice
            while True:
                user_input = input("Please enter the number corresponding to label value  (Press Enter for random'): ")

                # Condition for default choice
                if user_input == "":
                    print("random choice selected")
                    answer4 = record33[0]
                    ListD.append(answer4)
                    break

                # Validating the input to ensure it's an integer
                elif user_input.isdigit():
                    user_choice = int(user_input)
                    # Checking if the choice is within the valid range
                    if 1 <= user_choice <= len(record33):
                        answer4 = record33[user_choice - 1]
                        ListD.append(answer4)
                        print(f"You have chosen: {record33[user_choice - 1]}")
                        break
                    else:
                        print("Please enter a number within the list's range.")
                else:
                    print("Invalid input. Please enter an integer number.")

        query1 = f'''     
        MATCH (e:Event)-[r:Assign]->(f:Feature) 
        WHERE e.Activity = f.Name 
        AND f.Name = "{ListB[0]}" 
        AND f.label IN {ListC}
        AND f.Value IN {ListD}
        WITH id(f) as x, collect(DISTINCT e.Event) AS events
        WITH collect(events) AS allEvents
        with reduce(commonEvents = allEvents[0], events IN tail(allEvents) | apoc.coll.intersection(commonEvents, events)) as value
        UNWIND range(0,size(value)-1) AS i
        MATCH (n )<-[:CORR]-(e:Event)
        where n.Category = "Absolute" and e.Event=value[i] 
        return labels(n)[0], collect(DISTINCT n.ID) as ID
            '''
        print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            # print("record1=", record1)

        compare1 = []
        for item in entityList:
            for any in record1:
                if item[0] in any[0]:
                    compare1.append(any[1])
        print("compare1=", compare1)


        with open(DFG_FilePath, 'a') as file:
            file.write(f'''Type{typeNumber}_non_Relative_selection_ID_instances=''' + str(ListA) + "\n")
            file.write(f'''Type{typeNumber}_non_Relative_selection_feature_Name=''' + str(ListB) + "\n")
            file.write(f'''Type{typeNumber}_non_Relative_selection_feature_label=''' + str(ListC) + "\n")
            file.write(f'''Type{typeNumber}_non_Relative_selection_feature_Value=''' + str(ListD) + "\n")

        return compare1


def writeInQTyep5(FilaeName,Type5_Rel_1_DF_Show,Type5_Rel_2_DF_Show):

    import os

    confDirectory  = "../Data/0_qRelationship"
    confPath = os.path.realpath(confDirectory)
    print(confPath)

    DFG_FilePath = confPath + "/" + FilaeName + ".txt"
    print("DFG=", FilaeName)

    with open(DFG_FilePath, 'w') as file:
        file.write(f'''Type5_Rel_1_DF_Show={Type5_Rel_1_DF_Show}\n''')
        file.write(f'''Type5_Rel_2_DF_Show={Type5_Rel_2_DF_Show}\n''')

    return DFG_FilePath


def writeOtherFinder(DFG_FilePath):
    import A5_EntryCol_Step3_Step as cl1
    driver = cl1.driver


    query1 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE NOT EXISTS {{ (x)-[:INCLUDED]->(n) }} and n.Category="Absolute"
    RETURN  COLLECT (distinct LABELS(n))
    '''
    #print(query1)
    with driver.session() as session:
        record1 = session.run(query1).values()
        #print("record1=", record1)
        flat_list = record1[0][0]
        flattened_list = [label for sublist in flat_list for label in sublist]



    query2 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE NOT EXISTS {{ (z)-[:INCLUDED]->(y) }} and z.Category="Absolute"
    RETURN  COLLECT (distinct LABELS(z))
    '''
    #print(query1)
    with driver.session() as session:
        record2 = session.run(query2).values()
        #print("record1=", record1)
        flat_list2 = record2[0][0]
        flattened_list2 = [label for sublist in flat_list2 for label in sublist]




    query3 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE z.Category="Absolute" and n.Category="Absolute"
    RETURN COLLECT(DISTINCT LABELS(z)) + COLLECT(DISTINCT LABELS(n)) AS combinedLabels
    '''
    #print(query1)
    with driver.session() as session:
        record3 = session.run(query3).values()
        #print("record3=", record3)
        flat_list3 = record3[0][0]
        flattened_list3 = [label for sublist in flat_list3 for label in sublist]
        no_duplicates_list = list(set(flattened_list3))

    #print(no_duplicates_list)

    result1 = [item for item in no_duplicates_list if item not in flattened_list]
    result2 = [item for item in result1 if item not in flattened_list2]

    print(result2)


    for i, value in enumerate(result2, start=1):
        print(f"{i}. {value}")

    while True:
        user_input = input("Please enter the number corresponding entity : ")

        if user_input.isdigit():
            user_choice = int(user_input)
            if 1 <= user_choice <= len(result2):
                answer2 = result2[user_choice - 1]
                with open(DFG_FilePath, 'a') as file:
                    file.write(f'''Entity_Show={answer2}\n''')
                return answer2
                print(f"You have chosen: {result2[user_choice - 1]}")
                break
            else:
                print("Please enter a number within the list's range.")
        else:
            print("Invalid input. Please enter an integer number.")



def writeIDSelectionNonRelativT6(DFG_FilePath):
    Type_selection = None
    while Type_selection not in ["",'Y', 'N','y', 'n']:
        Type_selection = input(f'''Do you want to show specific IDs of an Entity (Y/N)?''')
        if Type_selection not in ["",'Y', 'N','y', 'n']:
            print("Invalid input. Please enter Y or N.")

    print(Type_selection)
    with open(DFG_FilePath, 'a') as file:
        if Type_selection == "y" or Type_selection == "Y" :
            file.write(f'''mainEntity_selection=True\n''')
        elif Type_selection == "n" or Type_selection == "N" or Type_selection == "":
            file.write(f'''mainEntity_selection=False\n''')
    return Type_selection


def writeIDSelectionInstanceType6(Type_selection,DFG_FilePath):
    ListA = []

    if Type_selection == "y" or Type_selection == "Y":
        Type_selection_ID_instances = input(f'''Enter the IDs (for example 1,2)?''')
        ListA.extend(Type_selection_ID_instances.split(","))

    with open(DFG_FilePath, 'a') as file:
        file.write(f'''mainEntity_selection_ID_instances=''' + str(ListA) + "\n")


def writeTypeApproach6(DFG_FilePath):
    Type="0"
    while Type not in ["", '1', '2']:
        # Prompt the user for input
        Type = input(
            f'''Please enter 1 if you want to select common Entities and 2 for unique (Default press enter):''')
        if Type == "":
            Type = '1'
        if Type not in ["", '1', '2']:
            print("Invalid input. Please enter 1 or 2.")

    with open(DFG_FilePath, 'a') as file:
        file.write(f'''Type_approach=''' + str(Type) + "\n")


