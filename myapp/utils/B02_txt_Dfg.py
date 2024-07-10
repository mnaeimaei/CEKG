

def txt_dfg():
    import os
    import A1_Scenario_Step2 as clN

    DFG=clN.DFG

    DFG="DFG1_DomainConceptLevel"

    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    print(confPath)

    FilePath = confPath + "/" + DFG + ".txt"
    print("FilePath=", FilePath)
    print("DFG=", DFG)




    list0 = ['DFG1', 'DFG1_featureValue', 'DFG2', 'DFG2_featureValue', 'DFG3', 'DFG3_feature', 'DFG3_featureValue',
             'DFG4', 'DFG4_feature', 'DFG4_featureValue', 'DFG5', 'DFG5_feature', 'DFG5_featureValue']
    list1 = ['DFG1_Domain', 'DFG1_featureValue_Domain', 'DFG2_Domain', 'DFG2_featureValue_Domain', 'DFG3_Domain',
             'DFG3_feature_Domain', 'DFG3_featureValue_Domain', 'DFG4_Domain', 'DFG4_feature_Domain',
             'DFG4_featureValue_Domain', 'DFG5_Domain', 'DFG5_feature_Domain', 'DFG5_featureValue_Domain']
    list2 = ['DFG1_DomainConcept', 'DFG1_featureValue_DomainConcept', 'DFG2_DomainConcept',
             'DFG2_featureValue_DomainConcept', 'DFG3_DomainConcept', 'DFG3_feature_DomainConcept',
             'DFG3_featureValue_DomainConcept', 'DFG4_DomainConcept', 'DFG4_feature_DomainConcept',
             'DFG4_featureValue_DomainConcept', 'DFG5_DomainConcept', 'DFG5_feature_DomainConcept',
             'DFG5_featureValue_DomainConcept']
    list3 = ['DFG1_DomainConceptLevel', 'DFG1_featureValue_DomainConceptLevel', 'DFG2_DomainConceptLevel',
             'DFG2_featureValue_DomainConceptLevel', 'DFG3_DomainConceptLevel', 'DFG3_feature_DomainConceptLevel',
             'DFG3_featureValue_DomainConceptLevel', 'DFG4_DomainConceptLevel', 'DFG4_feature_DomainConceptLevel',
             'DFG4_featureValue_DomainConceptLevel', 'DFG5_DomainConceptLevel', 'DFG5_feature_DomainConceptLevel',
             'DFG5_featureValue_DomainConceptLevel']

    if DFG in list0:
        pass

    if DFG in list1:
        pass

    if DFG in list2:
        pass

    if DFG in list3:
        with open(FilePath, 'w') as file:
            pass


        ###########################Part 1########################################################
        while True:
            try:
                distanceFrom_Domain = int(input("Enter the distance from SCT Domain? "))
                break
            except ValueError:
                print("Only integer input is acceptable. Please try again.")

        with open(FilePath, 'a') as file:
            file.write(f'''distanceFrom_Domain=''' + str(distanceFrom_Domain) + "\n")

        ###########################Part 2########################################################
        import A5_EntryCol_Step3_Step as cl1
        driver = cl1.driver
        query1 = f'''     
        MATCH (n:Concept)
        WITH DISTINCT n.Semanti_tags AS tags
        RETURN COLLECT(tags) AS distinct_tags
        '''
        #print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            record2 = record1[0][0]

        # Displaying the options to the user
        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        # Asking the user for their choice
        while True:
            user_input = input("Please enter the number corresponding to semantic Tag of concept (Press Enter for 'procedure'): ")

            # Condition for default choice
            if user_input == "":
                print("Default choice selected: procedure")
                answer = "procedure"
                #print(answer)
                break

            # Validating the input to ensure it's an integer
            elif user_input.isdigit():
                user_choice = int(user_input)
                # Checking if the choice is within the valid range
                if 1 <= user_choice <= len(record2):
                    answer=record2[user_choice-1]
                    #print(answer)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        with open(FilePath, 'a') as file:
            file.write(f'''Semanti_tags_Domain={answer}\n''')


        ###########################Part 2########################################################
        query2 = f'''     
        MATCH (n:Concept)
        WITH DISTINCT n.ConceptType AS tags
        RETURN COLLECT(tags) AS ConceptType
        '''
        #print(query2)

        with driver.session() as session:
            record3 = session.run(query2).values()
            record4 = record3[0][0]

        # Displaying the options to the user
        for i, value in enumerate(record4, start=1):
            print(f"{i}. {value}")

        # Asking the user for their choice
        while True:
            user_input = input("Please enter the number corresponding to your choice (Press Enter for 'Concept'): ")

            # Condition for default choice
            if user_input == "":
                print("Default choice selected: Concept")
                answer = "Concept"
                #print(answer)
                break

            # Validating the input to ensure it's an integer
            elif user_input.isdigit():
                user_choice = int(user_input)
                # Checking if the choice is within the valid range
                if 1 <= user_choice <= len(record4):
                    answer = record4[user_choice - 1]
                    print(answer)
                    print(f"You have chosen: {record4[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        with open(FilePath, 'a') as file:
            file.write(f'''ConceptType_Domain={answer}\n''')


        ###########################Part 4########################################################

        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        # Asking the user for their choice
        while True:
            user_input = input("Please enter the number corresponding to semantic Tag of TLC (Press Enter for 'procedure'): ")

            # Condition for default choice
            if user_input == "":
                print("Default choice selected: procedure")
                answer = "procedure"
                #print(answer)
                break

            # Validating the input to ensure it's an integer
            elif user_input.isdigit():
                user_choice = int(user_input)
                # Checking if the choice is within the valid range
                if 1 <= user_choice <= len(record2):
                    answer=record2[user_choice-1]
                    #print(answer)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        with open(FilePath, 'a') as file:
            file.write(f'''TLC_Semanti_tags_Domain={answer}\n''')


        ###########################Part Final########################################################

        import subprocess

        subprocess.run(['python', 'O04_Step32_DK6_Tied_importingNeo4J.py'])
        subprocess.run(['python', 'P04_Step34_DK7_Bond_importingNeo4J.py'])
        subprocess.run(['python', 'Q04_Step2_DFG_importingNeo4J_Scneario.py'])




