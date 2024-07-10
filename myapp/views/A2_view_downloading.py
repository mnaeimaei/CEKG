from django.shortcuts import render,redirect
from django.http import JsonResponse

from myapp.forms import BrowsingMethodForm
from myapp.forms import FileNameBox
from myapp.forms import LocationTextBox
from myapp.forms import ServiceKeyTextBox
from myapp.forms import NextButton1

from myapp.webSocketFunctions import ProgressBar

import subprocess






from django.http import HttpResponse
import json
import logging
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")

def importing_view(request):
    import os
    import ast
    import os
    confDirectory = "../z/myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)


    pyDirectory = "../mydjangoapp/myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    if request.method == 'POST':
        logger.debug(f"Hello23")
        logger.info("This is an info message")

        browsingMethodForm = BrowsingMethodForm(request.POST)
        fileNameBox = FileNameBox(request.POST)
        locationTextBox = LocationTextBox(request.POST)
        serviceKeyTextBox = ServiceKeyTextBox(request.POST)






        logger.debug(f"browsingMethodForm.is_valid() = {browsingMethodForm.is_valid()}")
        logger.debug(f"fileNameBox.is_valid() = {fileNameBox.is_valid()}")
        logger.debug(f"locationTextBox.is_valid() = {locationTextBox.is_valid()}")
        logger.debug(f"serviceKeyTextBox.is_valid() = {serviceKeyTextBox.is_valid()}")



        if browsingMethodForm.is_valid():
            logger.debug(f"browsingMethodForm.cleaned_data = {browsingMethodForm.cleaned_data}")
            browsingMethodForm_json = json.dumps(browsingMethodForm.cleaned_data)
            fileSource = browsingMethodForm.cleaned_data.get('browsingMethodMode')

        if fileNameBox.is_valid():
            logger.debug(f"fileNameBox.cleaned_data = {fileNameBox.cleaned_data}")
            fileNameBox_json = json.dumps(fileNameBox.cleaned_data)
            EventLogFinal = fileNameBox.cleaned_data.get('fileNameMode')

        if locationTextBox.is_valid():
            logger.debug(f"locationTextBox.cleaned_data = {locationTextBox.cleaned_data}")
            locationTextBox_json = json.dumps(locationTextBox.cleaned_data)
            importPath = locationTextBox.cleaned_data.get('locationTextMode')

        if serviceKeyTextBox.is_valid():
            logger.debug(f"serviceKeyTextBox.cleaned_data = {serviceKeyTextBox.cleaned_data}")
            serviceKeyTextBox_json = json.dumps(serviceKeyTextBox.cleaned_data)
            myCredentials = serviceKeyTextBox.cleaned_data.get('serviceKeyTextMode')




        savingFile1 = confPath + "/" + "2_downloadingFileSource.txt"
        with open(savingFile1, 'w') as file:
            file.write(f'''fileSource={fileSource}''' + "\n")

        if fileSource=="1":
            print("yes")

            savingFile2 = confPath + "/" + "2_downloadingGoogleCloud1.txt"
            with open(savingFile2, 'w') as file:
                file.write(f'''EventLogFinal={EventLogFinal}''' + "\n")

            savingFile3 = confPath + "/" + "2_downloadingGoogleCloud2.txt"
            with open(savingFile3, 'w') as file:
                file.write(f'''myCredentials={myCredentials}''' + "\n")

        if fileSource=="2":
            print("no")

            savingFile4 = confPath + "/" + "2_downloadingLocal1.txt"
            with open(savingFile4, 'w') as file:
                file.write(f'''EventLogFinal={EventLogFinal}''' + "\n")

            savingFile5 = confPath + "/" + "2_downloadingLocal2.txt"
            with open(savingFile5, 'w') as file:
                file.write(f'''importPath={importPath}''' + "\n")




        scripts = [
            'A2_FileLocation_Step1_Address_Software_Step.py',
            'A2_FileLocation_Step2_xlsx_Step.py',
            'A2_FileLocation_Step3_sheetName_Step.py'
        ]

        ProgressBar.run_scripts_asynchronously(script_directory, scripts)

        return redirect('excelPreview')

    else:

        browsingMethodForm = BrowsingMethodForm()
        fileNameBox = FileNameBox()
        locationTextBox = LocationTextBox()
        serviceKeyTextBox = ServiceKeyTextBox()
        nextButton1 = NextButton1()


        gFileName, gKey, lFileName, lLocation=existanceFileName(confPath)
        logger.info(gFileName)
        logger.info(gKey)
        logger.info(lFileName)
        logger.info(lLocation)



        return render(request, 'A2_downloading.html', {'browsingMethodForm': browsingMethodForm,
                                            'fileNameBox': fileNameBox,
                                            'locationTextBox': locationTextBox,
                                            'serviceKeyTextBox': serviceKeyTextBox,

                                           'gFileName': gFileName,
                                           'gKey': gKey,
                                           'lFileName': lFileName,
                                           'lLocation': lLocation,
                                            'nextButton1': nextButton1

                                            }
                  )



def existanceFileName(confPath):

    value1=""
    value2=""
    value3=""
    value4=""

    import os
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

    inputTex_FilePath = confPath + "/2_downloadingLocal1.txt"
    if os.path.exists(inputTex_FilePath):
        with open(inputTex_FilePath, 'r') as file:
            for line in file:
                variable_name, value3 = line.split('=')
                value3 = value3.strip()

    inputTex_FilePath = confPath + "/2_downloadingLocal2.txt"
    if os.path.exists(inputTex_FilePath):
        with open(inputTex_FilePath, 'r') as file:
            for line in file:
                variable_name, value4 = line.split('=')
                value4 = value4.strip()


    return value1, value2, value3, value4