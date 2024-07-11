from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage


from myapp.forms import NextButton1


from myapp.webSocketFunctions import ProgressBar

import subprocess

from django.http import HttpResponse
import json
import logging

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")


def importing_file(request):
    import os
    import ast
    import os
    confDirectory = "./myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)



    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)
    if request.method == 'POST' :

        if 'excelFile' in request.FILES:
            excel_file = request.FILES['excelFile']
            # Set the storage location to 'media/uploads/'
            fs = FileSystemStorage(location='media/uploads/0_Data')
            filename = fs.save(excel_file.name, excel_file)
            uploaded_file_url = fs.url(filename)
            logger.info(f"File uploaded at {uploaded_file_url}")


        scripts = [
            'A2_FileLocation_Step2_xlsx_Step.py',
            'A2_FileLocation_Step3_sheetName_Step.py'
        ]

        ProgressBar.run_scripts_asynchronously(script_directory, scripts)

        return redirect('excelPreview')

    else:



        return render(request, 'A02_browse.html', {



        }
                      )


