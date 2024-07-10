
def saveFileSource(confPath,fileSource):

    inputTex_FilePath = confPath + "/2_downloadingFileSource.txt"
    fileValue=str(fileSource)
    with open(inputTex_FilePath, 'w') as file:
        file.write(f'''fileSource={fileValue}''' + "\n")




def existanceFileName(confPath,fileSource):
    import os
    value1=""
    value2=""



    if fileSource == 1:
        inputTex_FilePath= confPath + "/2_downloadingGoogleCloud1.txt"
        if os.path.exists(inputTex_FilePath):
            with open(inputTex_FilePath, 'r') as file:
                for line in file:
                    variable_name, value1 = line.split('=')
                    value1 = value1.strip()

        inputTex_FilePath= confPath + "/2_downloadingGoogleCloud2.txt"
        if os.path.exists(inputTex_FilePath):
            with open(inputTex_FilePath, 'r') as file:
                for line in file:
                    variable_name, value2 = line.split('=')
                    value2 = value2.strip()




    if fileSource == 2:
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



def excelFileNameTest(confPath,fileSource,user_input):
    if fileSource == 1:
        inputTex_FilePath= confPath + "/2_downloadingGoogleCloud1.txt"
        with open(inputTex_FilePath, 'w') as file:
            file.write(f'''EventLogFinal={user_input}''' + "\n")
            return user_input
    if fileSource == 2:
        inputTex_FilePath= confPath + "/2_downloadingLocal1.txt"
        with open(inputTex_FilePath, 'w') as file:
            file.write(f'''EventLogFinal={user_input}''' + "\n")
            return user_input

###########################################################################################

def GCP1_Test(confPath, user_input):

    inputTex_FilePath= confPath + "/2_downloadingGoogleCloud2.txt"
    with open(inputTex_FilePath, 'w') as file:
        file.write(f'''myCredentials={user_input}''' + "\n")
        return user_input





###########################################################################################



def local1_Test(confPath, user_input):

    inputTex_FilePath= confPath + "/2_downloadingLocal2.txt"
    with open(inputTex_FilePath, 'w') as file:
        file.write(f'''importPath={user_input}''' + "\n")



#########################################################################################################


