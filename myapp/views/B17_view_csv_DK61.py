from django.shortcuts import render,redirect
from django.http import JsonResponse


from myapp.forms import Domain1ActivityForm
from myapp.forms import Domain1ActivitySynonymForm
from myapp.forms import Domain1DomainForm

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

def DK61(request):
    import os
    import ast

    confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "../mydjangoapp/myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    dataDirectory  = '../mydjangoapp/media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

    if request.method == 'POST':
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view POST part")


        domain1_activity_form = Domain1ActivityForm(request.POST)
        domain1_activity_synonym_form = Domain1ActivitySynonymForm(request.POST)
        domain1_domain_form = Domain1DomainForm(request.POST)

        logger.debug(f"domain1_activity_form.is_valid() = {domain1_activity_form.is_valid()}")
        logger.debug(f"domain1_activity_synonym_form.is_valid() = {domain1_activity_synonym_form.is_valid()}")
        logger.debug(f"domain1_domain_form.is_valid() = {domain1_domain_form.is_valid()}")


        options_text_path = confPath + "/17_dk61Mapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/17_dk61Default.txt"

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

        if domain1_activity_form.is_valid():
            Domain1_Activity = domain1_activity_form.cleaned_data.get('dynamic_choice_B17_1')
            Domain1_Activity = options_text_map[Domain1_Activity]
            update_variable_in_file(savingPath, "Domain1_Activity", Domain1_Activity)

        if domain1_activity_synonym_form.is_valid():
            Domain1_Activity_Synonym = domain1_activity_synonym_form.cleaned_data.get('dynamic_choice_B17_2')
            Domain1_Activity_Synonym = options_text_map[Domain1_Activity_Synonym]
            update_variable_in_file(savingPath, "Domain1_Activity_Synonym", Domain1_Activity_Synonym)

        if domain1_domain_form.is_valid():
            Domain1_Domain = domain1_domain_form.cleaned_data.get('dynamic_choice_B17_3')
            Domain1_Domain = options_text_map[Domain1_Domain]
            update_variable_in_file(savingPath, "Domain1_Domain", Domain1_Domain)


        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[14])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")


        domain1_activity_form = Domain1ActivityForm()
        domain1_activity_synonym_form = Domain1ActivitySynonymForm()
        domain1_domain_form = Domain1DomainForm()

        nextButton = NextButton1()

        openingPath = confPath + "/17_dk61DefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b17 = json.dumps(listData2)

        openingPath2 = confPath + "/17_dk61Number.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b17 = json.dumps(listData4)

        csvPath = dataPath + "/O_DK6_1.csv"
        df_DK61 = pd.read_csv(csvPath)
        logger.info(df_DK61)
        html_DK61 = df_DK61.to_html(classes='dataframe', index=False)



        return render(request, 'B17_csv_DK61.html', {
            'html_DK61': html_DK61,
            'domain1_activity_form': domain1_activity_form,
            'domain1_activity_synonym_form': domain1_activity_synonym_form,
            'domain1_domain_form': domain1_domain_form,
            'options_to_show_default_b17': options_to_show_default_b17,
            'button_lists_b17': button_lists_b17,
            'nextButton': nextButton

                                            }
                  )


