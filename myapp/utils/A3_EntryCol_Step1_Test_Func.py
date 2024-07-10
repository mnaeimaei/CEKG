import copy
import os
import pandas as pd




def Others_func_first(optionPath):
    with open(optionPath, 'r') as file:
        for line in file:
            pass
    import ast
    cLogColumn = ast.literal_eval(line)
    return cLogColumn


def modifyDefault(file_path_final,ListOf_variable_to_update,ListOf_new_value):
    def update_variable_in_file(file_path, variable_to_update, new_value):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Update the specific line
        updated = False
        for i, line in enumerate(lines):
            if line.strip().startswith(variable_to_update):
                lines[i] = f"{variable_to_update}={new_value}\n"
                updated = True
                break
        if updated:
            with open(file_path, 'w') as file:
                file.writelines(lines)


    for i, j in zip(ListOf_variable_to_update, ListOf_new_value):
        update_variable_in_file(file_path_final, i, j)







####################################################################################################



def EventLog_EntityFinder(savingPath):
    while True:
        user_input = input("Please enter the minimum number of aggregated relationship (At least 1 maximum 20): ")
        if user_input.isdigit():
            ED_EnNum = int(user_input)
            if ED_EnNum >= 0:
                print(f"You have entered: {ED_EnNum}")
                break
            else:
                print("The number must be 0 or higher. Please try again.")
        else:
            print("Invalid input. Please enter a valid integer number.")

    def update_variable_in_file(file_path, variable_to_update, new_value):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Update the specific line
        updated = False
        for i, line in enumerate(lines):
            if line.strip().startswith(variable_to_update):
                lines[i] = f"{variable_to_update}={new_value}\n"
                updated = True
                break
        if updated:
            with open(file_path, 'w') as file:
                file.writelines(lines)

    update_variable_in_file(savingPath, "ED_EnNum", ED_EnNum)

    return ED_EnNum








def EventLog_func(FilePath, ED_EnNum, csvColumn):

    def update_variable_in_file(file_path, variable_to_update, new_value):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Update the specific line
        updated = False
        for i, line in enumerate(lines):
            if line.strip().startswith(variable_to_update):
                lines[i] = f"{variable_to_update}={new_value}\n"
                updated = True
                break
        if updated:
            with open(file_path, 'w') as file:
                file.writelines(lines)



    goalList0 = []

    for i in range(ED_EnNum):
        x1 = f'''Entity{i + 1}Origin'''
        x2 = f'''Entity{i + 1}ID'''
        goalList0.append(x1)
        goalList0.append(x2)

    def get_user_choice(listOrg, prompt_message):
        while True:
            for i, value in enumerate(listOrg, start=1):
                print(f"{i}. {value}")

            user_input = input(prompt_message)

            if user_input.isdigit():
                user_choice = int(user_input)
                if 1 <= user_choice <= len(listOrg):
                    selected_value = listOrg[user_choice - 1]
                    print(f"You have chosen: {selected_value}")
                    return selected_value
                else:
                    print("Please enter a number within the list's range.")
            else:
                print("Invalid input. Please enter an integer number.")


    for item in goalList0:

        itemSelection = get_user_choice(csvColumn, f'''Please enter the corresponding column to {item}?''')
        update_variable_in_file(FilePath, item, itemSelection)





























#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
#########################################################################################################
