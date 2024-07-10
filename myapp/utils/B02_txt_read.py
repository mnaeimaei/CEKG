
def txtExistance(FilaeName):
    import os
    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + FilaeName + ".txt"

    if os.path.exists(DFG_FilePath):
        return True
    else:
        return False


'''
txtFileExistance=txtExistance("DFG1")
print("txtFileExistance=", txtFileExistance)
'''

def ShowTxt(FilaeName, EnNum, part1Search,part2Search):
    import os
    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    print(confPath)
    print(FilaeName)

    DFG_FilePath = confPath + "/" + str(FilaeName) + ".txt"
    print(DFG_FilePath)

    with open(DFG_FilePath, 'r') as file:
        # Read the file line by line
        ListEnDFSHow = []
        for line in file:
            # print(line)
            for x in range(1, EnNum + 1):
                # print(x)
                moduleVaribale = part1Search + str(x) + part2Search
                #print(moduleVaribale)
                if line.startswith(moduleVaribale):
                    # print("yes")
                    variable_name, value = line.split('=')
                    # print(variable_name)
                    variable_name = variable_name.strip()
                    value = int(value.strip())  # Convert value to int if needed
                    exec(f"{variable_name} = {value}")
                    print(f"{variable_name}: {value}")
                    ListEnDFSHow.append(value)
    return ListEnDFSHow

'''
ListEnDFSHow=ShowTxt("DFG1",3, "Type1_Entity","_DF_Show")
print("ListEnDFSHow=", ListEnDFSHow)
'''

def TrueFalseTxt(FilaeName, searchText):
    import os
    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + str(FilaeName) + ".txt"

    with open(DFG_FilePath, 'r') as file:
        for line in file:
            if line.startswith(searchText):
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                if variable_name == searchText:
                    value = value.strip()
                    if value.lower() == 'true':
                        value = True
                    elif value.lower() == 'false':
                        value = False
                    case_selector_activation = value
    return case_selector_activation

'''
case_selector_activation=TrueFalseTxt("DFG1","Type1_selection")
print("case_selector_activation=", case_selector_activation)
'''

def listIntTxt(FilaeName, searchText):
    import os
    import ast
    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + str(FilaeName) + ".txt"

    with open(DFG_FilePath, 'r') as file:
        for line in file:
            if line.startswith(searchText):
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                if variable_name == searchText:
                    value = value.strip()
                    value = ast.literal_eval(value)
                    Type1_selection_ID = value
    return Type1_selection_ID

'''
Type1_selection_ID=listIntTxt("DFG1","Type1_selection_ID")
print("Type1_selection_ID=", Type1_selection_ID)


Type1_selection_ID_instances=listIntTxt("DFG1","Type1_selection_ID_instances")
print("Type1_selection_ID_instances=", Type1_selection_ID_instances)

distanceFrom_Domain=listIntTxt("DFG1_DomainConceptLevel","distanceFrom_Domain")
print("distanceFrom_Domain=", distanceFrom_Domain)
'''

def stringTxt(FilaeName, searchText):
    import os
    import ast
    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + str(FilaeName) + ".txt"

    with open(DFG_FilePath, 'r') as file:
        for line in file:
            if line.startswith(searchText):
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                if variable_name == searchText:
                    value = value.strip()
                    Type1_selection_ID = value
    return Type1_selection_ID

'''
Semanti_tags_Domain=stringTxt("DFG1_DomainConceptLevel","Semanti_tags_Domain")
print("Semanti_tags_Domain=", Semanti_tags_Domain)
'''

def TypeApproach(FilaeName, searchText):
    import os
    import ast
    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + str(FilaeName) + ".txt"

    with open(DFG_FilePath, 'r') as file:
        for line in file:
            if line.startswith(searchText):
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                if variable_name == searchText:
                    value = value.strip()
                    value = ast.literal_eval(value)
                    TypeApproach = value
    return TypeApproach


'''
Type1_approach= txtF.TypeApproach("DFG1_DomainConceptLevel","Type1_approach")
print("Type1_approach=", Type1_approach)
'''


def TypeCount(FilaeName, searchText):
    import os
    import ast
    confDirectory = "../Data/0_Conf"
    confPath = os.path.realpath(confDirectory)
    #print(confPath)

    DFG_FilePath = confPath + "/" + str(FilaeName) + ".txt"

    with open(DFG_FilePath, 'r') as file:
        for line in file:
            if line.startswith(searchText):
                variable_name, value = line.split('=')
                variable_name = variable_name.strip()
                if variable_name == searchText:
                    value = value.strip()
                    value = ast.literal_eval(value)
                    TypeApproach = value
    return TypeApproach

