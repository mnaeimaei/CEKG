from django.shortcuts import render,redirect
from django.http import JsonResponse


from myapp.forms import Dk5ActivityForm
from myapp.forms import Dk5ActivitySynonymForm
from myapp.forms import Dk5OtcForm
from myapp.forms import Dk5SctCodeForm

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

def DK5(request):
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

        dk5_activity_form = Dk5ActivityForm(request.POST)
        dk5_activity_synonym_form = Dk5ActivitySynonymForm(request.POST)
        dk5_otc_form = Dk5OtcForm(request.POST)
        dk5_sct_code_form = Dk5SctCodeForm(request.POST)

        logger.debug(f"dk5_activity_form.is_valid() = {dk5_activity_form.is_valid()}")
        logger.debug(f"dk5_activity_synonym_form.is_valid() = {dk5_activity_synonym_form.is_valid()}")
        logger.debug(f"dk5_otc_form.is_valid() = {dk5_otc_form.is_valid()}")
        logger.debug(f"dk5_sct_code_form.is_valid() = {dk5_sct_code_form.is_valid()}")


        options_text_path = confPath + "/16_dk5Mapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/16_dk5Default.txt"

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

        if dk5_activity_form.is_valid():
            DK5_Activity = dk5_activity_form.cleaned_data.get('dynamic_choice_B16_1')
            DK5_Activity = options_text_map[DK5_Activity]
            update_variable_in_file(savingPath, "DK5_Activity", DK5_Activity)

        if dk5_activity_synonym_form.is_valid():
            DK5_Activity_Synonym = dk5_activity_synonym_form.cleaned_data.get('dynamic_choice_B16_2')
            DK5_Activity_Synonym = options_text_map[DK5_Activity_Synonym]
            update_variable_in_file(savingPath, "DK5_Activity_Synonym", DK5_Activity_Synonym)

        if dk5_otc_form.is_valid():
            DK5_OTC = dk5_otc_form.cleaned_data.get('dynamic_choice_B16_3')
            DK5_OTC = options_text_map[DK5_OTC]
            update_variable_in_file(savingPath, "DK5_OTC", DK5_OTC)

        if dk5_sct_code_form.is_valid():
            DK5_SCTCode = dk5_sct_code_form.cleaned_data.get('dynamic_choice_B16_4')
            DK5_SCTCode = options_text_map[DK5_SCTCode]
            update_variable_in_file(savingPath, "DK5_SCTCode", DK5_SCTCode)



        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[13])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")


        dk5_activity_form = Dk5ActivityForm()
        dk5_activity_synonym_form = Dk5ActivitySynonymForm()
        dk5_otc_form = Dk5OtcForm()
        dk5_sct_code_form = Dk5SctCodeForm()

        nextButton = NextButton1()

        openingPath = confPath + "/16_dk5DefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b16 = json.dumps(listData2)

        openingPath2 = confPath + "/16_dk5Number.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b16 = json.dumps(listData4)


        csvPath = dataPath + "/N_DK5.csv"
        df_DK5 = pd.read_csv(csvPath)
        logger.info(df_DK5)
        html_DK5 = df_DK5.to_html(classes='dataframe', index=False)



        return render(request, 'B16_csv_DK5.html', {
            'html_DK5': html_DK5,
            'dk5_activity_form': dk5_activity_form,
            'dk5_activity_synonym_form': dk5_activity_synonym_form,
            'dk5_otc_form': dk5_otc_form,
            'dk5_sct_code_form': dk5_sct_code_form,
            'options_to_show_default_b16': options_to_show_default_b16,
            'button_lists_b16': button_lists_b16,
            'nextButton': nextButton

                                            }
                  )


