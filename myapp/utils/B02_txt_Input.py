

def txt_input():
    import os
    import A1_Scenario_Step2 as clN

    myInput=clN.myInput

    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    print(confPath)

    FilePath = confPath + "/" + myInput + ".txt"
    print("FilePath=", FilePath)
    print("input=", myInput)

    if myInput == 'main_Entities':  # 1
        pass

    if myInput == 'main_Entities_plus_Disorder':  # 2
        pass

    if myInput == 'main_Entities_plus_ICD':  # 2
        pass

    if myInput == 'main_Entities_plus_ICD_level_doesnt_work':  # 3
        pass

    if myInput == 'main_Entities_plus_SCT':  # 4
        pass

    if myInput == 'main_Entities_plus_SCT_level':  # 5
        with open(FilePath, 'w') as file:
            pass

        print("SSSSSSSSSSSSSSSSSSS")


        ###########################Part 1########################################################
        while True:
            try:

                distanceFromTLC = int(input("Enter the distance from SCT ? "))

                break
            except ValueError:
                print("Only integer input is acceptable. Please try again.")

        with open(FilePath, 'a') as file:
            file.write(f'''distanceFromTLC=''' + str(distanceFromTLC) + "\n")

        print("SSSSSSSSSSSSSSSSSSS")
        ###########################Part 2########################################################
        import A5_EntryCol_Step3_Step as cl1
        driver = cl1.driver
        query1 = f'''     
        MATCH (n:Concept)
        WITH DISTINCT n.Semanti_tags AS tags
        RETURN COLLECT(tags) AS distinct_tags
        '''
        # print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            record2 = record1[0][0]

        # Displaying the options to the user
        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        # Asking the user for their choice
        while True:
            user_input = input(
                "Please enter the number corresponding to semantic Tag of concept (Press Enter for 'disorder'): ")

            # Condition for default choice
            if user_input == "":
                print("Default choice selected: procedure")
                answer = "disorder"
                # print(answer)
                break

            # Validating the input to ensure it's an integer
            elif user_input.isdigit():
                user_choice = int(user_input)
                # Checking if the choice is within the valid range
                if 1 <= user_choice <= len(record2):
                    answer = record2[user_choice - 1]
                    # print(answer)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        with open(FilePath, 'a') as file:
            file.write(f'''Semanti_tags={answer}\n''')

        ###########################Part 2########################################################
        query2 = f'''     
        MATCH (n:Concept)
        WITH DISTINCT n.ConceptType AS tags
        RETURN COLLECT(tags) AS ConceptType
        '''
        # print(query2)

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
                # print(answer)
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
            file.write(f'''ConceptType={answer}\n''')

        ###########################Part 4########################################################

        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        # Asking the user for their choice
        while True:
            user_input = input(
                "Please enter the number corresponding to semantic Tag of TLC (Press Enter for 'finding'): ")

            # Condition for default choice
            if user_input == "":
                print("Default choice selected: procedure")
                answer = "finding"
                # print(answer)
                break

            # Validating the input to ensure it's an integer
            elif user_input.isdigit():
                user_choice = int(user_input)
                # Checking if the choice is within the valid range
                if 1 <= user_choice <= len(record2):
                    answer = record2[user_choice - 1]
                    # print(answer)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        with open(FilePath, 'a') as file:
            file.write(f'''TLC_Semanti_tags={answer}\n''')

        ###########################Part Final########################################################

        import subprocess

        subprocess.run(['python', 'P04_Step34_DK7_Bond_importingNeo4J.py'])
        subprocess.run(['python', 'Q04_Step2_DFG_importingNeo4J_Scneario.py'])

    if myInput == 'main_Entities_plus_SCT_Level_One':  # 6
        pass

        with open(FilePath, 'w') as file:
            pass

        print("SSSSSSSSSSSSSSSSSSS")

        ###########################Part 1########################################################
        while True:
            try:

                distanceFromTLC = int(input("Enter the distance from SCT ? "))

                break
            except ValueError:
                print("Only integer input is acceptable. Please try again.")

        with open(FilePath, 'a') as file:
            file.write(f'''distanceFromTLC=''' + str(distanceFromTLC) + "\n")

        print("SSSSSSSSSSSSSSSSSSS")
        ###########################Part 2########################################################
        import A5_EntryCol_Step3_Step as cl1
        driver = cl1.driver
        query1 = f'''     
        MATCH (n:Concept)
        WITH DISTINCT n.Semanti_tags AS tags
        RETURN COLLECT(tags) AS distinct_tags
        '''
        # print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            record2 = record1[0][0]

        # Displaying the options to the user
        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        # Asking the user for their choice
        while True:
            user_input = input(
                "Please enter the number corresponding to semantic Tag of concept (Press Enter for 'disorder'): ")

            # Condition for default choice
            if user_input == "":
                print("Default choice selected: procedure")
                answer = "disorder"
                # print(answer)
                break

            # Validating the input to ensure it's an integer
            elif user_input.isdigit():
                user_choice = int(user_input)
                # Checking if the choice is within the valid range
                if 1 <= user_choice <= len(record2):
                    answer = record2[user_choice - 1]
                    # print(answer)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        with open(FilePath, 'a') as file:
            file.write(f'''Semanti_tags={answer}\n''')

        ###########################Part 2########################################################
        query2 = f'''     
        MATCH (n:Concept)
        WITH DISTINCT n.ConceptType AS tags
        RETURN COLLECT(tags) AS ConceptType
        '''
        # print(query2)

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
                # print(answer)
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
            file.write(f'''ConceptType={answer}\n''')

        ###########################Part 4########################################################

        for i, value in enumerate(record2, start=1):
            print(f"{i}. {value}")

        # Asking the user for their choice
        while True:
            user_input = input(
                "Please enter the number corresponding to semantic Tag of TLC (Press Enter for 'finding'): ")

            # Condition for default choice
            if user_input == "":
                print("Default choice selected: procedure")
                answer = "finding"
                # print(answer)
                break

            # Validating the input to ensure it's an integer
            elif user_input.isdigit():
                user_choice = int(user_input)
                # Checking if the choice is within the valid range
                if 1 <= user_choice <= len(record2):
                    answer = record2[user_choice - 1]
                    # print(answer)
                    print(f"You have chosen: {record2[user_choice - 1]}")
                    break
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")

        with open(FilePath, 'a') as file:
            file.write(f'''TLC_Semanti_tags={answer}\n''')

        ###########################Part Final########################################################

        import subprocess

        subprocess.run(['python', 'P04_Step34_DK7_Bond_importingNeo4J.py'])
        subprocess.run(['python', 'Q04_Step2_DFG_importingNeo4J_Scneario.py'])

    if myInput == 'main_Entities_plus_ICD_one':  # 7

        with open(FilePath, 'w') as file:
            pass

        while True:
            try:
                icdCode = int(input("Enter the ICD Code ? "))

                break
            except ValueError:
                print("Only integer input is acceptable. Please try again.")

        with open(FilePath, 'a') as file:
            file.write(f'''icdCode=''' + str(icdCode) + "\n")

    if myInput == 'main_Entities_plus_SCT_one':  # 8
        with open(FilePath, 'w') as file:
            pass

        while True:
            try:
                conceptId = int(input("Enter the SCT ID ? "))

                break
            except ValueError:
                print("Only integer input is acceptable. Please try again.")

        with open(FilePath, 'a') as file:
            file.write(f'''conceptId=''' + str(conceptId) + "\n")



