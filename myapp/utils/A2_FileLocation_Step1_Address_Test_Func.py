



def existanceFileName(confPath):
    import os
    value1=""
    value2=""


    inputTex_FilePath = confPath + "/2_downloadingLocal1.txt"
    if os.path.exists(inputTex_FilePath):
        with open(inputTex_FilePath, 'r') as file:
            for line in file:
                variable_name, value1 = line.split('=')
                value1 = value1.strip()

    inputTex_FilePath = confPath + "/2_downloadingLocal2.txt"
    if os.path.exists(inputTex_FilePath):
        with open(inputTex_FilePath, 'r') as file:
            for line in file:
                variable_name, value2 = line.split('=')
                value2 = value2.strip()

    return value1, value2


def excelFileNameTest(confPath,user_input):
    inputTex_FilePath= confPath + "/2_downloadingLocal1.txt"
    with open(inputTex_FilePath, 'w') as file:
        file.write(f'''finalUsrWord={user_input}''' + "\n")
        return user_input


def local1_Test(confPath, user_input):

    inputTex_FilePath= confPath + "/2_downloadingLocal2.txt"
    with open(inputTex_FilePath, 'w') as file:
        file.write(f'''finalPassWord={user_input}''' + "\n")
        return user_input






