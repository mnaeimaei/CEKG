from django.shortcuts import render,redirect
from django.http import JsonResponse


from myapp.forms import Domain2DomainForm
from myapp.forms import Domain2OTCForm
from myapp.forms import Domain2SCTCodeForm

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

def DK62(request):
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

        domain2_domain_form = Domain2DomainForm(request.POST)
        domain2_otc_form = Domain2OTCForm(request.POST)
        domain2_sct_code_form = Domain2SCTCodeForm(request.POST)

        logger.debug(f"domain2_domain_form.is_valid() = {domain2_domain_form.is_valid()}")
        logger.debug(f"domain2_otc_form.is_valid() = {domain2_otc_form.is_valid()}")
        logger.debug(f"domain2_sct_code_form.is_valid() = {domain2_sct_code_form.is_valid()}")


        options_text_path = confPath + "/18_dk62Mapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/18_dk62Default.txt"

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

        if domain2_domain_form.is_valid():
            Domain2_Domain = domain2_domain_form.cleaned_data.get('dynamic_choice_B18_1')
            Domain2_Domain = options_text_map[Domain2_Domain]
            update_variable_in_file(savingPath, "Domain2_Domain", Domain2_Domain)

        if domain2_otc_form.is_valid():
            Domain2_OTC = domain2_otc_form.cleaned_data.get('dynamic_choice_B18_2')
            Domain2_OTC = options_text_map[Domain2_OTC]
            update_variable_in_file(savingPath, "Domain2_OTC", Domain2_OTC)

        if domain2_sct_code_form.is_valid():
            Domain2_SCTCode = domain2_sct_code_form.cleaned_data.get('dynamic_choice_B18_3')
            Domain2_SCTCode = options_text_map[Domain2_SCTCode]
            update_variable_in_file(savingPath, "Domain2_SCTCode", Domain2_SCTCode)

        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)


        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[15])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")


        domain2_domain_form = Domain2DomainForm()
        domain2_otc_form = Domain2OTCForm()
        domain2_sct_code_form = Domain2SCTCodeForm()


        nextButton = NextButton1()

        openingPath = confPath + "/18_dk62DefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b18 = json.dumps(listData2)

        openingPath2 = confPath + "/18_dk62Number.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b18 = json.dumps(listData4)


        csvPath = dataPath + "/O_DK6_2.csv"
        df_DK62 = pd.read_csv(csvPath)
        logger.info(df_DK62)
        html_DK62 = df_DK62.to_html(classes='dataframe', index=False)



        return render(request, 'B18_csv_DK62.html', {
            'html_DK62': html_DK62,
            'domain2_domain_form': domain2_domain_form,
            'domain2_otc_form': domain2_otc_form,
            'domain2_sct_code_form': domain2_sct_code_form,
            'options_to_show_default_b18': options_to_show_default_b18,
            'button_lists_b18': button_lists_b18,
            'nextButton': nextButton

                                            }
                  )


