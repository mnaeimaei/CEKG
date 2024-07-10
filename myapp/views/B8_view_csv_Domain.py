from django.shortcuts import render,redirect
from django.http import JsonResponse



from myapp.forms import DomainForm

from myapp.forms import NextButton1

import subprocess

import os
import pandas as pd
import ast



from django.http import HttpResponse
import json
import logging
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")

def Domain(request):
    import os
    import ast

    confDirectory = "./myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    dataDirectory  = './media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

    if request.method == 'POST':
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view POST part")

        domain_form = DomainForm(request.POST)

        logger.debug(f"domain_form.is_valid() = {domain_form.is_valid()}")

        options_text_path = confPath + "/8_domainMapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/8_domainEntitiesDefault.txt"

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

        if domain_form.is_valid():
            ACT_Domain = domain_form.cleaned_data.get('dynamic_choice_B8_1')
            ACT_Domain = options_text_map[ACT_Domain]
            update_variable_in_file(savingPath, "ACT_Domain", ACT_Domain)


        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[5])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")


        domain_form = DomainForm()

        nextButton = NextButton1()

        openingPath = confPath + "/8_domainDefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b8 = json.dumps(listData2)

        openingPath2 = confPath + "/8_domainNumber.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b8 = json.dumps(listData4)

        csvPath = dataPath + "/F_Domain.csv"
        df_Domain = pd.read_csv(csvPath)
        logger.info(df_Domain)
        html_Domain = df_Domain.to_html(classes='dataframe', index=False)



        return render(request, 'B8_csv_Domain.html', {
            'html_Domain': html_Domain,
            'domain_form': domain_form,
            'options_to_show_default_b8': options_to_show_default_b8,
            'button_lists_b8': button_lists_b8,
            'nextButton': nextButton

                                            }
                  )


