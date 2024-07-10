from django.shortcuts import render,redirect
from django.http import JsonResponse

from myapp.forms import EnNumForm
from myapp.forms import ActivityForm
from myapp.forms import ActivityPropertiesIDForm
from myapp.forms import ActivitySynonymForm
from myapp.forms import ActivityValueIDForm
from myapp.forms import TimestampForm
from myapp.forms import EventIdTitleForm
from myapp.forms import Entity1IDForm
from myapp.forms import Entity2IDForm
from myapp.forms import Entity3IDForm
from myapp.forms import Entity4IDForm
from myapp.forms import Entity5IDForm
from myapp.forms import Entity6IDForm
from myapp.forms import Entity7IDForm
from myapp.forms import Entity8IDForm
from myapp.forms import Entity9IDForm
from myapp.forms import Entity10IDForm
from myapp.forms import Entity11IDForm
from myapp.forms import Entity12IDForm
from myapp.forms import Entity13IDForm
from myapp.forms import Entity14IDForm
from myapp.forms import Entity15IDForm
from myapp.forms import Entity16IDForm
from myapp.forms import Entity17IDForm
from myapp.forms import Entity18IDForm
from myapp.forms import Entity19IDForm
from myapp.forms import Entity20IDForm
from myapp.forms import Entity1OriginForm
from myapp.forms import Entity2OriginForm
from myapp.forms import Entity3OriginForm
from myapp.forms import Entity4OriginForm
from myapp.forms import Entity5OriginForm
from myapp.forms import Entity6OriginForm
from myapp.forms import Entity7OriginForm
from myapp.forms import Entity8OriginForm
from myapp.forms import Entity9OriginForm
from myapp.forms import Entity10OriginForm
from myapp.forms import Entity11OriginForm
from myapp.forms import Entity12OriginForm
from myapp.forms import Entity13OriginForm
from myapp.forms import Entity14OriginForm
from myapp.forms import Entity15OriginForm
from myapp.forms import Entity16OriginForm
from myapp.forms import Entity17OriginForm
from myapp.forms import Entity18OriginForm
from myapp.forms import Entity19OriginForm
from myapp.forms import Entity20OriginForm

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

def event_log(request):
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
        logger.info(f"This is the Event Log view POST part")

        enum_form = EnNumForm(request.POST)
        activity_form = ActivityForm(request.POST)
        activity_properties_id_form = ActivityPropertiesIDForm(request.POST)
        activity_synonym_form = ActivitySynonymForm(request.POST)
        activity_value_id_form = ActivityValueIDForm(request.POST)
        timestamp_form = TimestampForm(request.POST)
        event_id_title_form = EventIdTitleForm(request.POST)
        entity1_id_form = Entity1IDForm(request.POST)
        entity2_id_form = Entity2IDForm(request.POST)
        entity3_id_form = Entity3IDForm(request.POST)
        entity4_id_form = Entity4IDForm(request.POST)
        entity5_id_form = Entity5IDForm(request.POST)
        entity6_id_form = Entity6IDForm(request.POST)
        entity7_id_form = Entity7IDForm(request.POST)
        entity8_id_form = Entity8IDForm(request.POST)
        entity9_id_form = Entity9IDForm(request.POST)
        entity10_id_form = Entity10IDForm(request.POST)
        entity11_id_form = Entity11IDForm(request.POST)
        entity12_id_form = Entity12IDForm(request.POST)
        entity13_id_form = Entity13IDForm(request.POST)
        entity14_id_form = Entity14IDForm(request.POST)
        entity15_id_form = Entity15IDForm(request.POST)
        entity16_id_form = Entity16IDForm(request.POST)
        entity17_id_form = Entity17IDForm(request.POST)
        entity18_id_form = Entity18IDForm(request.POST)
        entity19_id_form = Entity19IDForm(request.POST)
        entity20_id_form = Entity20IDForm(request.POST)
        entity1_origin_form = Entity1OriginForm(request.POST)
        entity2_origin_form = Entity2OriginForm(request.POST)
        entity3_origin_form = Entity3OriginForm(request.POST)
        entity4_origin_form = Entity4OriginForm(request.POST)
        entity5_origin_form = Entity5OriginForm(request.POST)
        entity6_origin_form = Entity6OriginForm(request.POST)
        entity7_origin_form = Entity7OriginForm(request.POST)
        entity8_origin_form = Entity8OriginForm(request.POST)
        entity9_origin_form = Entity9OriginForm(request.POST)
        entity10_origin_form = Entity10OriginForm(request.POST)
        entity11_origin_form = Entity11OriginForm(request.POST)
        entity12_origin_form = Entity12OriginForm(request.POST)
        entity13_origin_form = Entity13OriginForm(request.POST)
        entity14_origin_form = Entity14OriginForm(request.POST)
        entity15_origin_form = Entity15OriginForm(request.POST)
        entity16_origin_form = Entity16OriginForm(request.POST)
        entity17_origin_form = Entity17OriginForm(request.POST)
        entity18_origin_form = Entity18OriginForm(request.POST)
        entity19_origin_form = Entity19OriginForm(request.POST)
        entity20_origin_form = Entity20OriginForm(request.POST)

        logger.debug(f"enum_form.is_valid() = {enum_form.is_valid()}")
        logger.debug(f"activity_form.is_valid() = {activity_form.is_valid()}")
        logger.debug(f"activity_properties_id_form.is_valid() = {activity_properties_id_form.is_valid()}")
        logger.debug(f"activity_synonym_form.is_valid() = {activity_synonym_form.is_valid()}")
        logger.debug(f"activity_value_id_form.is_valid() = {activity_value_id_form.is_valid()}")
        logger.debug(f"timestamp_form.is_valid() = {timestamp_form.is_valid()}")
        logger.debug(f"event_id_title_form.is_valid() = {event_id_title_form.is_valid()}")
        logger.debug(f"entity1_id_form.is_valid() = {entity1_id_form.is_valid()}")
        logger.debug(f"entity2_id_form.is_valid() = {entity2_id_form.is_valid()}")
        logger.debug(f"entity3_id_form.is_valid() = {entity3_id_form.is_valid()}")
        logger.debug(f"entity4_id_form.is_valid() = {entity4_id_form.is_valid()}")
        logger.debug(f"entity5_id_form.is_valid() = {entity5_id_form.is_valid()}")
        logger.debug(f"entity6_id_form.is_valid() = {entity6_id_form.is_valid()}")
        logger.debug(f"entity7_id_form.is_valid() = {entity7_id_form.is_valid()}")
        logger.debug(f"entity8_id_form.is_valid() = {entity8_id_form.is_valid()}")
        logger.debug(f"entity9_id_form.is_valid() = {entity9_id_form.is_valid()}")
        logger.debug(f"entity10_id_form.is_valid() = {entity10_id_form.is_valid()}")
        logger.debug(f"entity11_id_form.is_valid() = {entity11_id_form.is_valid()}")
        logger.debug(f"entity12_id_form.is_valid() = {entity12_id_form.is_valid()}")
        logger.debug(f"entity13_id_form.is_valid() = {entity13_id_form.is_valid()}")
        logger.debug(f"entity14_id_form.is_valid() = {entity14_id_form.is_valid()}")
        logger.debug(f"entity15_id_form.is_valid() = {entity15_id_form.is_valid()}")
        logger.debug(f"entity16_id_form.is_valid() = {entity16_id_form.is_valid()}")
        logger.debug(f"entity17_id_form.is_valid() = {entity17_id_form.is_valid()}")
        logger.debug(f"entity18_id_form.is_valid() = {entity18_id_form.is_valid()}")
        logger.debug(f"entity19_id_form.is_valid() = {entity19_id_form.is_valid()}")
        logger.debug(f"entity20_id_form.is_valid() = {entity20_id_form.is_valid()}")
        logger.debug(f"entity1_origin_form.is_valid() = {entity1_origin_form.is_valid()}")
        logger.debug(f"entity2_origin_form.is_valid() = {entity2_origin_form.is_valid()}")
        logger.debug(f"entity3_origin_form.is_valid() = {entity3_origin_form.is_valid()}")
        logger.debug(f"entity4_origin_form.is_valid() = {entity4_origin_form.is_valid()}")
        logger.debug(f"entity5_origin_form.is_valid() = {entity5_origin_form.is_valid()}")
        logger.debug(f"entity6_origin_form.is_valid() = {entity6_origin_form.is_valid()}")
        logger.debug(f"entity7_origin_form.is_valid() = {entity7_origin_form.is_valid()}")
        logger.debug(f"entity8_origin_form.is_valid() = {entity8_origin_form.is_valid()}")
        logger.debug(f"entity9_origin_form.is_valid() = {entity9_origin_form.is_valid()}")
        logger.debug(f"entity10_origin_form.is_valid() = {entity10_origin_form.is_valid()}")
        logger.debug(f"entity11_origin_form.is_valid() = {entity11_origin_form.is_valid()}")
        logger.debug(f"entity12_origin_form.is_valid() = {entity12_origin_form.is_valid()}")
        logger.debug(f"entity13_origin_form.is_valid() = {entity13_origin_form.is_valid()}")
        logger.debug(f"entity14_origin_form.is_valid() = {entity14_origin_form.is_valid()}")
        logger.debug(f"entity15_origin_form.is_valid() = {entity15_origin_form.is_valid()}")
        logger.debug(f"entity16_origin_form.is_valid() = {entity16_origin_form.is_valid()}")
        logger.debug(f"entity17_origin_form.is_valid() = {entity17_origin_form.is_valid()}")
        logger.debug(f"entity18_origin_form.is_valid() = {entity18_origin_form.is_valid()}")
        logger.debug(f"entity19_origin_form.is_valid() = {entity19_origin_form.is_valid()}")
        logger.debug(f"entity20_origin_form.is_valid() = {entity20_origin_form.is_valid()}")





        options_text_path = confPath + "/4_eventLogMapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")


        savingPath = confPath + "/4_eventLogDefault.txt"

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

        if enum_form.is_valid():
            ED_EnNum = enum_form.cleaned_data.get('dynamic_choice_B4_1')
            update_variable_in_file(savingPath, "ED_EnNum", ED_EnNum)

        if event_id_title_form.is_valid():
            ED_eventIdTitle = event_id_title_form.cleaned_data.get('dynamic_choice_B4_2')
            ED_eventIdTitle = options_text_map[ED_eventIdTitle]
            update_variable_in_file(savingPath, "ED_eventIdTitle", ED_eventIdTitle)

        if activity_form.is_valid():
            ED_Activity = activity_form.cleaned_data.get('dynamic_choice_B4_3')
            ED_Activity = options_text_map[ED_Activity]
            update_variable_in_file(savingPath, "ED_Activity", ED_Activity)

        if activity_synonym_form.is_valid():
            ED_ActivitySynonym = activity_synonym_form.cleaned_data.get('dynamic_choice_B4_4')
            ED_ActivitySynonym = options_text_map[ED_ActivitySynonym]
            update_variable_in_file(savingPath, "ED_ActivitySynonym", ED_ActivitySynonym)

        if timestamp_form.is_valid():
            ED_Timestamp = timestamp_form.cleaned_data.get('dynamic_choice_B4_5')
            ED_Timestamp = options_text_map[ED_Timestamp]
            update_variable_in_file(savingPath, "ED_Timestamp", ED_Timestamp)

        if activity_value_id_form.is_valid():
            ED_Activity_Value_ID = activity_value_id_form.cleaned_data.get('dynamic_choice_B4_6')
            ED_Activity_Value_ID = options_text_map[ED_Activity_Value_ID]
            update_variable_in_file(savingPath, "ED_Activity_Value_ID", ED_Activity_Value_ID)


        if activity_properties_id_form.is_valid():
            ED_Activity_Properties_ID = activity_properties_id_form.cleaned_data.get('dynamic_choice_B4_7')
            ED_Activity_Properties_ID = options_text_map[ED_Activity_Properties_ID]
            update_variable_in_file(savingPath, "ED_Activity_Properties_ID", ED_Activity_Properties_ID)

        if entity1_id_form.is_valid():
            Entity1ID = entity1_id_form.cleaned_data.get('dynamic_choice_B4_8')
            Entity1ID = options_text_map[Entity1ID]
            update_variable_in_file(savingPath, "Entity1ID", Entity1ID)

        if entity2_id_form.is_valid():
            Entity2ID = entity2_id_form.cleaned_data.get('dynamic_choice_B4_9')
            Entity2ID = options_text_map[Entity2ID]
            update_variable_in_file(savingPath, "Entity2ID", Entity2ID)

        if entity3_id_form.is_valid():
            Entity3ID = entity3_id_form.cleaned_data.get('dynamic_choice_B4_10')
            Entity3ID = options_text_map[Entity3ID]
            update_variable_in_file(savingPath, "Entity3ID", Entity3ID)

        if entity4_id_form.is_valid():
            Entity4ID = entity4_id_form.cleaned_data.get('dynamic_choice_B4_11')
            Entity4ID = options_text_map[Entity4ID]
            update_variable_in_file(savingPath, "Entity4ID", Entity4ID)

        if entity5_id_form.is_valid():
            Entity5ID = entity5_id_form.cleaned_data.get('dynamic_choice_B4_12')
            Entity5ID = options_text_map[Entity5ID]
            update_variable_in_file(savingPath, "Entity5ID", Entity5ID)

        if entity6_id_form.is_valid():
            Entity6ID = entity6_id_form.cleaned_data.get('dynamic_choice_B4_13')
            Entity6ID = options_text_map[Entity6ID]
            update_variable_in_file(savingPath, "Entity6ID", Entity6ID)

        if entity7_id_form.is_valid():
            Entity7ID = entity7_id_form.cleaned_data.get('dynamic_choice_B4_14')
            Entity7ID = options_text_map[Entity7ID]
            update_variable_in_file(savingPath, "Entity7ID", Entity7ID)

        if entity8_id_form.is_valid():
            Entity8ID = entity8_id_form.cleaned_data.get('dynamic_choice_B4_15')
            Entity8ID = options_text_map[Entity8ID]
            update_variable_in_file(savingPath, "Entity8ID", Entity8ID)

        if entity9_id_form.is_valid():
            Entity9ID = entity9_id_form.cleaned_data.get('dynamic_choice_B4_16')
            Entity9ID = options_text_map[Entity9ID]
            update_variable_in_file(savingPath, "Entity9ID", Entity9ID)

        if entity10_id_form.is_valid():
            Entity10ID = entity10_id_form.cleaned_data.get('dynamic_choice_B4_17')
            Entity10ID = options_text_map[Entity10ID]
            update_variable_in_file(savingPath, "Entity10ID", Entity10ID)

        if entity11_id_form.is_valid():
            Entity11ID = entity11_id_form.cleaned_data.get('dynamic_choice_B4_18')
            Entity11ID = options_text_map[Entity11ID]
            update_variable_in_file(savingPath, "Entity11ID", Entity11ID)

        if entity12_id_form.is_valid():
            Entity12ID = entity12_id_form.cleaned_data.get('dynamic_choice_B4_19')
            Entity12ID = options_text_map[Entity12ID]
            update_variable_in_file(savingPath, "Entity12ID", Entity12ID)

        if entity13_id_form.is_valid():
            Entity13ID = entity13_id_form.cleaned_data.get('dynamic_choice_B4_20')
            Entity13ID = options_text_map[Entity13ID]
            update_variable_in_file(savingPath, "Entity13ID", Entity13ID)

        if entity14_id_form.is_valid():
            Entity14ID = entity14_id_form.cleaned_data.get('dynamic_choice_B4_21')
            Entity14ID = options_text_map[Entity14ID]
            update_variable_in_file(savingPath, "Entity14ID", Entity14ID)

        if entity15_id_form.is_valid():
            Entity15ID = entity15_id_form.cleaned_data.get('dynamic_choice_B4_22')
            Entity15ID = options_text_map[Entity15ID]
            update_variable_in_file(savingPath, "Entity15ID", Entity15ID)

        if entity16_id_form.is_valid():
            Entity16ID = entity16_id_form.cleaned_data.get('dynamic_choice_B4_23')
            Entity16ID = options_text_map[Entity16ID]
            update_variable_in_file(savingPath, "Entity16ID", Entity16ID)

        if entity17_id_form.is_valid():
            Entity17ID = entity17_id_form.cleaned_data.get('dynamic_choice_B4_24')
            Entity17ID = options_text_map[Entity17ID]
            update_variable_in_file(savingPath, "Entity17ID", Entity17ID)

        if entity18_id_form.is_valid():
            Entity18ID = entity18_id_form.cleaned_data.get('dynamic_choice_B4_25')
            Entity18ID = options_text_map[Entity18ID]
            update_variable_in_file(savingPath, "Entity18ID", Entity18ID)

        if entity19_id_form.is_valid():
            Entity19ID = entity19_id_form.cleaned_data.get('dynamic_choice_B4_26')
            Entity19ID = options_text_map[Entity19ID]
            update_variable_in_file(savingPath, "Entity19ID", Entity19ID)

        if entity20_id_form.is_valid():
            Entity20ID = entity20_id_form.cleaned_data.get('dynamic_choice_B4_27')
            Entity20ID = options_text_map[Entity20ID]
            update_variable_in_file(savingPath, "Entity20ID", Entity20ID)

        if entity1_origin_form.is_valid():
            Entity1Origin = entity1_origin_form.cleaned_data.get('dynamic_choice_B4_28')
            Entity1Origin = options_text_map[Entity1Origin]
            update_variable_in_file(savingPath, "Entity1Origin", Entity1Origin)

        if entity2_origin_form.is_valid():
            Entity2Origin = entity2_origin_form.cleaned_data.get('dynamic_choice_B4_29')
            Entity2Origin = options_text_map[Entity2Origin]
            update_variable_in_file(savingPath, "Entity2Origin", Entity2Origin)

        if entity3_origin_form.is_valid():
            Entity3Origin = entity3_origin_form.cleaned_data.get('dynamic_choice_B4_30')
            Entity3Origin = options_text_map[Entity3Origin]
            update_variable_in_file(savingPath, "Entity3Origin", Entity3Origin)

        if entity4_origin_form.is_valid():
            Entity4Origin = entity4_origin_form.cleaned_data.get('dynamic_choice_B4_31')
            Entity4Origin = options_text_map[Entity4Origin]
            update_variable_in_file(savingPath, "Entity4Origin", Entity4Origin)

        if entity5_origin_form.is_valid():
            Entity5Origin = entity5_origin_form.cleaned_data.get('dynamic_choice_B4_32')
            Entity5Origin = options_text_map[Entity5Origin]
            update_variable_in_file(savingPath, "Entity5Origin", Entity5Origin)

        if entity6_origin_form.is_valid():
            Entity6Origin = entity6_origin_form.cleaned_data.get('dynamic_choice_B4_33')
            Entity6Origin = options_text_map[Entity6Origin]
            update_variable_in_file(savingPath, "Entity6Origin", Entity6Origin)

        if entity7_origin_form.is_valid():
            Entity7Origin = entity7_origin_form.cleaned_data.get('dynamic_choice_B4_34')
            Entity7Origin = options_text_map[Entity7Origin]
            update_variable_in_file(savingPath, "Entity7Origin", Entity7Origin)

        if entity8_origin_form.is_valid():
            Entity8Origin = entity8_origin_form.cleaned_data.get('dynamic_choice_B4_35')
            Entity8Origin = options_text_map[Entity8Origin]
            update_variable_in_file(savingPath, "Entity8Origin", Entity8Origin)

        if entity9_origin_form.is_valid():
            Entity9Origin = entity9_origin_form.cleaned_data.get('dynamic_choice_B4_36')
            Entity9Origin = options_text_map[Entity9Origin]
            update_variable_in_file(savingPath, "Entity9Origin", Entity9Origin)

        if entity10_origin_form.is_valid():
            Entity10Origin = entity10_origin_form.cleaned_data.get('dynamic_choice_B4_37')
            Entity10Origin = options_text_map[Entity10Origin]
            update_variable_in_file(savingPath, "Entity10Origin", Entity10Origin)

        if entity11_origin_form.is_valid():
            Entity11Origin = entity11_origin_form.cleaned_data.get('dynamic_choice_B4_38')
            Entity11Origin = options_text_map[Entity11Origin]
            update_variable_in_file(savingPath, "Entity11Origin", Entity11Origin)

        if entity12_origin_form.is_valid():
            Entity12Origin = entity12_origin_form.cleaned_data.get('dynamic_choice_B4_39')
            Entity12Origin = options_text_map[Entity12Origin]
            update_variable_in_file(savingPath, "Entity12Origin", Entity12Origin)

        if entity13_origin_form.is_valid():
            Entity13Origin = entity13_origin_form.cleaned_data.get('dynamic_choice_B4_40')
            Entity13Origin = options_text_map[Entity13Origin]
            update_variable_in_file(savingPath, "Entity13Origin", Entity13Origin)

        if entity14_origin_form.is_valid():
            Entity14Origin = entity14_origin_form.cleaned_data.get('dynamic_choice_B4_41')
            Entity14Origin = options_text_map[Entity14Origin]
            update_variable_in_file(savingPath, "Entity14Origin", Entity14Origin)

        if entity15_origin_form.is_valid():
            Entity15Origin = entity15_origin_form.cleaned_data.get('dynamic_choice_B4_42')
            Entity15Origin = options_text_map[Entity15Origin]
            update_variable_in_file(savingPath, "Entity15Origin", Entity15Origin)

        if entity16_origin_form.is_valid():
            Entity16Origin = entity16_origin_form.cleaned_data.get('dynamic_choice_B4_43')
            Entity16Origin = options_text_map[Entity16Origin]
            update_variable_in_file(savingPath, "Entity16Origin", Entity16Origin)

        if entity17_origin_form.is_valid():
            Entity17Origin = entity18_origin_form.cleaned_data.get('dynamic_choice_B4_44')
            Entity17Origin = options_text_map[Entity17Origin]
            update_variable_in_file(savingPath, "Entity17Origin", Entity17Origin)

        if entity18_origin_form.is_valid():
            Entity18Origin = entity19_origin_form.cleaned_data.get('dynamic_choice_B4_45')
            Entity18Origin = options_text_map[Entity18Origin]
            update_variable_in_file(savingPath, "Entity18Origin", Entity18Origin)

        if entity19_origin_form.is_valid():
            Entity19Origin = entity19_origin_form.cleaned_data.get('dynamic_choice_B4_46')
            Entity19Origin = options_text_map[Entity19Origin]
            update_variable_in_file(savingPath, "Entity19Origin", Entity19Origin)

        if entity20_origin_form.is_valid():
            Entity20Origin = entity20_origin_form.cleaned_data.get('dynamic_choice_B4_47')
            Entity20Origin = options_text_map[Entity20Origin]
            update_variable_in_file(savingPath, "Entity20Origin", Entity20Origin)


        #subprocess.run(['python', 'XXXXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXXXX.py'], cwd=script_directory)

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[1])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")

        enum_form = EnNumForm()
        activity_form = ActivityForm()
        activity_properties_id_form = ActivityPropertiesIDForm()
        activity_synonym_form = ActivitySynonymForm()
        activity_value_id_form = ActivityValueIDForm()
        timestamp_form = TimestampForm()
        event_id_title_form = EventIdTitleForm()
        entity1_id_form = Entity1IDForm()
        entity2_id_form = Entity2IDForm()
        entity3_id_form = Entity3IDForm()
        entity4_id_form = Entity4IDForm()
        entity5_id_form = Entity5IDForm()
        entity6_id_form = Entity6IDForm()
        entity7_id_form = Entity7IDForm()
        entity8_id_form = Entity8IDForm()
        entity9_id_form = Entity9IDForm()
        entity10_id_form = Entity10IDForm()
        entity11_id_form = Entity11IDForm()
        entity12_id_form = Entity12IDForm()
        entity13_id_form = Entity13IDForm()
        entity14_id_form = Entity14IDForm()
        entity15_id_form = Entity15IDForm()
        entity16_id_form = Entity16IDForm()
        entity17_id_form = Entity17IDForm()
        entity18_id_form = Entity18IDForm()
        entity19_id_form = Entity19IDForm()
        entity20_id_form = Entity20IDForm()
        entity1_origin_form = Entity1OriginForm()
        entity2_origin_form = Entity2OriginForm()
        entity3_origin_form = Entity3OriginForm()
        entity4_origin_form = Entity4OriginForm()
        entity5_origin_form = Entity5OriginForm()
        entity6_origin_form = Entity6OriginForm()
        entity7_origin_form = Entity7OriginForm()
        entity8_origin_form = Entity8OriginForm()
        entity9_origin_form = Entity9OriginForm()
        entity10_origin_form = Entity10OriginForm()
        entity11_origin_form = Entity11OriginForm()
        entity12_origin_form = Entity12OriginForm()
        entity13_origin_form = Entity13OriginForm()
        entity14_origin_form = Entity14OriginForm()
        entity15_origin_form = Entity15OriginForm()
        entity16_origin_form = Entity16OriginForm()
        entity17_origin_form = Entity17OriginForm()
        entity18_origin_form = Entity18OriginForm()
        entity19_origin_form = Entity19OriginForm()
        entity20_origin_form = Entity20OriginForm()

        nextButton = NextButton1()

        openingPath1 = confPath + "/4_eventLogDefaultValue1.txt"
        import ast
        with open(openingPath1, 'r') as file:
            default1 = file.read()
            listData1 = ast.literal_eval(default1)
            options_default_b41 = json.dumps(listData1)


        openingPath2 = confPath + "/4_eventLogDefaultValue2.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default2 = file.read()
            listData2 = ast.literal_eval(default2)
            options_default_b42 = json.dumps(listData2)


        openingPath3 = confPath + "/4_eventLogNumber1.txt"
        import ast
        with open(openingPath3, 'r') as file:
            default3 = file.read()
            listData3 = ast.literal_eval(default3)
            button_to_show_b41 = json.dumps(listData3)


        openingPath4 = confPath + "/4_eventLogNumber2.txt"
        import ast
        with open(openingPath4, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_to_show_b42 = json.dumps(listData4)





        csvPath = dataPath + "/C_Log.csv"
        df_cLog = pd.read_csv(csvPath)
        logger.info(df_cLog)
        html_cLog = df_cLog.to_html(classes='dataframe', index=False)



        return render(request, 'B4_csv_EventLog.html', {
            'html_cLog': html_cLog,
            'enum_form': enum_form,
            'activity_form': activity_form,
            'activity_properties_id_form': activity_properties_id_form,
            'activity_synonym_form': activity_synonym_form,
            'activity_value_id_form': activity_value_id_form,
            'timestamp_form': timestamp_form,
            'event_id_title_form': event_id_title_form,
            'entity1_id_form': entity1_id_form,
            'entity2_id_form': entity2_id_form,
            'entity3_id_form': entity3_id_form,
            'entity4_id_form': entity4_id_form,
            'entity5_id_form': entity5_id_form,
            'entity6_id_form': entity6_id_form,
            'entity7_id_form': entity7_id_form,
            'entity8_id_form': entity8_id_form,
            'entity9_id_form': entity9_id_form,
            'entity10_id_form': entity10_id_form,
            'entity11_id_form': entity11_id_form,
            'entity12_id_form': entity12_id_form,
            'entity13_id_form': entity13_id_form,
            'entity14_id_form': entity14_id_form,
            'entity15_id_form': entity15_id_form,
            'entity16_id_form': entity16_id_form,
            'entity17_id_form': entity17_id_form,
            'entity18_id_form': entity18_id_form,
            'entity19_id_form': entity19_id_form,
            'entity20_id_form': entity20_id_form,
            'entity1_origin_form': entity1_origin_form,
            'entity2_origin_form': entity2_origin_form,
            'entity3_origin_form': entity3_origin_form,
            'entity4_origin_form': entity4_origin_form,
            'entity5_origin_form': entity5_origin_form,
            'entity6_origin_form': entity6_origin_form,
            'entity7_origin_form': entity7_origin_form,
            'entity8_origin_form': entity8_origin_form,
            'entity9_origin_form': entity9_origin_form,
            'entity10_origin_form': entity10_origin_form,
            'entity11_origin_form': entity11_origin_form,
            'entity12_origin_form': entity12_origin_form,
            'entity13_origin_form': entity13_origin_form,
            'entity14_origin_form': entity14_origin_form,
            'entity15_origin_form': entity15_origin_form,
            'entity16_origin_form': entity16_origin_form,
            'entity17_origin_form': entity17_origin_form,
            'entity18_origin_form': entity18_origin_form,
            'entity19_origin_form': entity19_origin_form,
            'entity20_origin_form': entity20_origin_form,
            'options_default_b41': options_default_b41,
            'options_default_b42': options_default_b42,
            'button_to_show_b41': button_to_show_b41,
            'button_to_show_b42': button_to_show_b42,
            'nextButton': nextButton

                                            }
                  )


