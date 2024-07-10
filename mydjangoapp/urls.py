
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path

from myapp.views.A00_view_Login import login_view

from myapp.views.A000_view_Directory import browse


from myapp.views.A1_view_home import home_view
from myapp.views.A02_view_browse import importing_file
from myapp.views.A02_view_downloading import importing_view
from myapp.views.A3_view_preview import preview_view

from myapp.views.B4_view_csv_eventLog import event_log
from myapp.views.B5_view_csv_otherEntities import otherEntities
from myapp.views.B6_view_csv_entityRel import entityRel
from myapp.views.B7_view_csv_activityProperties import activityProperties
from myapp.views.B8_view_csv_Domain import Domain
from myapp.views.B9_view_csv_ICD import ICD
from myapp.views.B10_view_csv_SctNode import SctNode
from myapp.views.B11_view_csv_SctRel import SctRel
from myapp.views.B12_view_csv_DK1 import DK1
from myapp.views.B13_view_csv_DK2 import DK2
from myapp.views.B14_view_csv_DK3 import DK3
from myapp.views.B15_view_csv_DK4 import DK4
from myapp.views.B16_view_csv_DK5 import DK5
from myapp.views.B17_view_csv_DK61 import DK61
from myapp.views.B18_view_csv_DK62 import DK62
from myapp.views.B19_view_csv_DK7 import DK7

from myapp.views.C20_view_neo4j_converting import convertingNeo4jFunc
from myapp.views.C21_view_neo4j_eventLog import eventLogNeo4jFunc
from myapp.views.C22_view_neo4j_otherEntities import otherEntitiesNeo4jFunc
from myapp.views.C23_view_neo4j_entityRel import entityRelNeo4jFunc
from myapp.views.C24_view_neo4j_activityProperties import activityPropertiesNeo4jFunc
from myapp.views.C25_view_neo4j_Domain import DomainNeo4jFunc
from myapp.views.C26_view_neo4j_ICD import ICDNeo4jFunc
from myapp.views.C27_view_neo4j_SctNode import SctNodeNeo4jFunc
from myapp.views.C28_view_neo4j_SctRel import SctRelNeo4jFunc
from myapp.views.C29_view_neo4j_DK1 import DK1Neo4jFunc
from myapp.views.C30_view_neo4j_DK2 import DK2Neo4jFunc
from myapp.views.C31_view_neo4j_DK3 import DK3Neo4jFunc
from myapp.views.C32_view_neo4j_DK4 import DK4Neo4jFunc
from myapp.views.C33_view_neo4j_DK5 import DK5Neo4jFunc
from myapp.views.C34_view_neo4j_DK6 import DK6Neo4jFunc
from myapp.views.C35_view_neo4j_DK7 import DK7Neo4jFunc


from myapp.views.C20_view_neo4j_Converting_resourseURL import seve_jpegCKEG
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ1_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ2_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ3_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ4_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ5_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ6_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ7_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ8_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ9_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ10_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ11_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_funcQ12_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ4_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ5_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ6_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ7_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ8_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ9_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ10_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ11_EventLog
from myapp.views.C21_view_neo4j_eventLog_resourseURL import seve_neo4jQuery_svgQ12_EventLog
from myapp.views.C22_view_neo4j_otherEntities_resourseURL import seve_neo4jQuery_funcQ1_otherEntities
from myapp.views.C22_view_neo4j_otherEntities_resourseURL import seve_neo4jQuery_funcQ2_otherEntities
from myapp.views.C22_view_neo4j_otherEntities_resourseURL import seve_neo4jQuery_funcQ3_otherEntities
from myapp.views.C22_view_neo4j_otherEntities_resourseURL import seve_neo4jQuery_funcQ4_otherEntities
from myapp.views.C22_view_neo4j_otherEntities_resourseURL import seve_neo4jQuery_svgQ4_otherEntities
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ1_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ2_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ3_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ4_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ5_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ6_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ7_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ8_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ9_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ10_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ11_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_funcQ12_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ3_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ6_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ7_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ8_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ9_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ10_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ11_entityRel
from myapp.views.C23_view_neo4j_entityRel_resourseURL import seve_neo4jQuery_svgQ12_entityRel
from myapp.views.C24_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_funcQ1_activityProperties
from myapp.views.C24_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_funcQ2_activityProperties
from myapp.views.C24_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_funcQ3_activityProperties
from myapp.views.C24_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_funcQ4_activityProperties
from myapp.views.C24_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_funcQ5_activityProperties
from myapp.views.C24_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_svgQ4_activityProperties
from myapp.views.C24_view_neo4j_activityProperties_resourseURL import seve_neo4jQuery_svgQ5_activityProperties
from myapp.views.C25_view_neo4j_Domain_resourseURL import seve_neo4jQuery_funcQ1_Domain
from myapp.views.C25_view_neo4j_Domain_resourseURL import seve_neo4jQuery_funcQ2_Domain
from myapp.views.C25_view_neo4j_Domain_resourseURL import seve_neo4jQuery_funcQ3_Domain
from myapp.views.C25_view_neo4j_Domain_resourseURL import seve_neo4jQuery_funcQ4_Domain
from myapp.views.C25_view_neo4j_Domain_resourseURL import seve_neo4jQuery_svgQ4_Domain
from myapp.views.C26_view_neo4j_ICD_resourseURL import seve_neo4jQuery_funcQ1_ICD
from myapp.views.C26_view_neo4j_ICD_resourseURL import seve_neo4jQuery_funcQ2_ICD
from myapp.views.C26_view_neo4j_ICD_resourseURL import seve_neo4jQuery_funcQ3_ICD
from myapp.views.C26_view_neo4j_ICD_resourseURL import seve_neo4jQuery_funcQ4_ICD
from myapp.views.C26_view_neo4j_ICD_resourseURL import seve_neo4jQuery_svgQ4_ICD
from myapp.views.C27_view_neo4j_SctNode_resourseURL import seve_neo4jQuery_funcQ1_sctNode
from myapp.views.C27_view_neo4j_SctNode_resourseURL import seve_neo4jQuery_funcQ2_sctNode
from myapp.views.C27_view_neo4j_SctNode_resourseURL import seve_neo4jQuery_funcQ3_sctNode
from myapp.views.C27_view_neo4j_SctNode_resourseURL import seve_neo4jQuery_funcQ4_sctNode
from myapp.views.C27_view_neo4j_SctNode_resourseURL import seve_neo4jQuery_svgQ4_sctNode
from myapp.views.C28_view_neo4j_SctRel_resourseURL import seve_neo4jQuery_funcQ1_sctRel
from myapp.views.C28_view_neo4j_SctRel_resourseURL import seve_neo4jQuery_funcQ2_sctRel
from myapp.views.C28_view_neo4j_SctRel_resourseURL import seve_neo4jQuery_funcQ3_sctRel
from myapp.views.C28_view_neo4j_SctRel_resourseURL import seve_neo4jQuery_svgQ2_sctRel
from myapp.views.C28_view_neo4j_SctRel_resourseURL import seve_neo4jQuery_svgQ3_sctRel
from myapp.views.C31_view_neo4j_DK3_resourseURL import seve_neo4jQuery_funcQ1_DK3
from myapp.views.C31_view_neo4j_DK3_resourseURL import seve_neo4jQuery_funcQ2_DK3
from myapp.views.C31_view_neo4j_DK3_resourseURL import seve_neo4jQuery_svgQ2_DK3
from myapp.views.C32_view_neo4j_DK4_resourseURL import seve_neo4jQuery_funcQ1_DK4
from myapp.views.C32_view_neo4j_DK4_resourseURL import seve_neo4jQuery_funcQ2_DK4
from myapp.views.C32_view_neo4j_DK4_resourseURL import seve_neo4jQuery_svgQ2_DK4
from myapp.views.C33_view_neo4j_DK5_resourseURL import seve_neo4jQuery_funcQ1_DK5
from myapp.views.C33_view_neo4j_DK5_resourseURL import seve_neo4jQuery_funcQ2_DK5
from myapp.views.C33_view_neo4j_DK5_resourseURL import seve_neo4jQuery_funcQ3_DK5
from myapp.views.C33_view_neo4j_DK5_resourseURL import seve_neo4jQuery_svgQ2_DK5
from myapp.views.C33_view_neo4j_DK5_resourseURL import seve_neo4jQuery_svgQ3_DK5
from myapp.views.C34_view_neo4j_DK6_resourseURL import seve_neo4jQuery_funcQ1_DK6
from myapp.views.C34_view_neo4j_DK6_resourseURL import seve_neo4jQuery_funcQ2_DK6
from myapp.views.C34_view_neo4j_DK6_resourseURL import seve_neo4jQuery_svgQ2_DK6
from myapp.views.C35_view_neo4j_DK7_resourseURL import seve_neo4jQuery_funcQ1_DK7
from myapp.views.C35_view_neo4j_DK7_resourseURL import seve_neo4jQuery_funcQ2_DK7
from myapp.views.C35_view_neo4j_DK7_resourseURL import seve_neo4jQuery_svgQ2_DK7
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ1_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ2_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ3_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ4_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ5_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ6_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ7_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ8_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ9_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ10_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ11_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ12_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ13_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ14_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ15_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ16_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ17_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ18_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ19_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ20_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ21_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_funcQ22_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ3_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ4_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ5_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ6_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ7_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ8_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ9_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ10_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ11_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ12_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ13_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ14_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ15_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ16_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ17_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ18_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ19_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ20_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ21_Final
from myapp.views.D36_view_BuildingQuery_resourseURL import seve_neo4jQuery_svgQ22_Final


from myapp.views.D36_view_BuildingQuery import queryLister

from myapp.views.E37_view_DFG import DFG
from myapp.views.E37_view_dfg import serve_pdf_func
from myapp.views.E37_view_dfg import serve_dot_func
from myapp.views.E37_view_dfg import serve_graphvizQuery_func
from myapp.views.E37_view_dfg import serve_svg_func
from myapp.views.E37_view_dfg import serve_neo4jQuery_func





urlpatterns = [
    path('', login_view, name='login'),

    path('browse/', browse, {'path': ''}, name='browse'),

    re_path(r'^files/(?P<path>.*)$', browse, name='browse'),

    path('homePage/', home_view, name='home'),

    path('importingFile/', importing_file, name='importingFile'),
    path('importingExcel/', importing_view, name='importingExcel'),
    path('excelPreview/', preview_view, name='excelPreview'),

    path('eventLog/', event_log, name='eventLogName'),
    path('otherEntities/', otherEntities, name='otherEntitiesName'),
    path('entityRel/', entityRel, name='entityRelName'),
    path('activityProperties/', activityProperties, name='activityPropertiesName'),
    path('Domain/', Domain, name='DomainName'),
    path('ICD/', ICD, name='ICDName'),
    path('SctNode/', SctNode, name='SctNodeName'),
    path('SctRel/', SctRel, name='SctRelName'),
    path('DK1/', DK1, name='DK1Name'),
    path('DK2/', DK2, name='DK2Name'),
    path('DK3/', DK3, name='DK3Name'),
    path('DK4/', DK4, name='DK4Name'),
    path('DK5/', DK5, name='DK5Name'),
    path('DK61/', DK61, name='DK61Name'),
    path('DK62/', DK62, name='DK62Name'),
    path('DK7/', DK7, name='DK7Name'),

    path('convertingNeo4j/', convertingNeo4jFunc, name='convertingNeo4jName'),
    path('eventLogNeo4j/', eventLogNeo4jFunc, name='eventLogNeo4jName'),
    path('otherEntitiesNeo4j/', otherEntitiesNeo4jFunc, name='otherEntitiesNeo4jName'),
    path('entityRelNeo4j/', entityRelNeo4jFunc, name='entityRelNeo4jName'),
    path('activityPropertiesNeo4j/', activityPropertiesNeo4jFunc, name='activityPropertiesNeo4jName'),
    path('DomainNeo4j/', DomainNeo4jFunc, name='DomainNeo4jName'),
    path('ICDNeo4j/', ICDNeo4jFunc, name='ICDNeo4jName'),
    path('SctNodeNeo4j/', SctNodeNeo4jFunc, name='SctNodeNeo4jName'),
    path('SctRelNeo4j/', SctRelNeo4jFunc, name='SctRelNeo4jName'),
    path('DK1Neo4j/', DK1Neo4jFunc, name='DK1Neo4jName'),
    path('DK2Neo4j/', DK2Neo4jFunc, name='DK2Neo4jName'),
    path('DK3Neo4j/', DK3Neo4jFunc, name='DK3Neo4jName'),
    path('DK4Neo4j/', DK4Neo4jFunc, name='DK4Neo4jName'),
    path('DK5Neo4j/', DK5Neo4jFunc, name='DK5Neo4jName'),
    path('DK6Neo4j/', DK6Neo4jFunc, name='DK6Neo4jName'),
    path('DK7Neo4j/', DK7Neo4jFunc, name='DK7Neo4jName'),

    path('convertingNeo4jCKEG/', seve_jpegCKEG, name='seve_jpegCKEG_name'),

    path('eventLogNeo4jQ1/',  seve_neo4jQuery_funcQ1_EventLog, name='seve_neo4jQuery_nameQ1_EventLog'),
    path('eventLogNeo4jQ2/',  seve_neo4jQuery_funcQ2_EventLog, name='seve_neo4jQuery_nameQ2_EventLog'),
    path('eventLogNeo4jQ3/',  seve_neo4jQuery_funcQ3_EventLog, name='seve_neo4jQuery_nameQ3_EventLog'),
    path('eventLogNeo4jQ4/',  seve_neo4jQuery_funcQ4_EventLog, name='seve_neo4jQuery_nameQ4_EventLog'),
    path('eventLogNeo4jQ5/',  seve_neo4jQuery_funcQ5_EventLog, name='seve_neo4jQuery_nameQ5_EventLog'),
    path('eventLogNeo4jQ6/',  seve_neo4jQuery_funcQ6_EventLog, name='seve_neo4jQuery_nameQ6_EventLog'),
    path('eventLogNeo4jQ7/',  seve_neo4jQuery_funcQ7_EventLog, name='seve_neo4jQuery_nameQ7_EventLog'),
    path('eventLogNeo4jQ8/',  seve_neo4jQuery_funcQ8_EventLog, name='seve_neo4jQuery_nameQ8_EventLog'),
    path('eventLogNeo4jQ9/',  seve_neo4jQuery_funcQ9_EventLog, name='seve_neo4jQuery_nameQ9_EventLog'),
    path('eventLogNeo4jQ10/',  seve_neo4jQuery_funcQ10_EventLog, name='seve_neo4jQuery_nameQ10_EventLog'),
    path('eventLogNeo4jQ11/',  seve_neo4jQuery_funcQ11_EventLog, name='seve_neo4jQuery_nameQ11_EventLog'),
    path('eventLogNeo4jQ12/',  seve_neo4jQuery_funcQ12_EventLog, name='seve_neo4jQuery_nameQ12_EventLog'),
    path('otherEntitiesNeo4jQ1/',  seve_neo4jQuery_funcQ1_otherEntities, name='seve_neo4jQuery_nameQ1_otherEntities'),
    path('otherEntitiesNeo4jQ2/',  seve_neo4jQuery_funcQ2_otherEntities, name='seve_neo4jQuery_nameQ2_otherEntities'),
    path('otherEntitiesNeo4jQ3/',  seve_neo4jQuery_funcQ3_otherEntities, name='seve_neo4jQuery_nameQ3_otherEntities'),
    path('otherEntitiesNeo4jQ4/',  seve_neo4jQuery_funcQ4_otherEntities, name='seve_neo4jQuery_nameQ4_otherEntities'),
    path('entityRelNeo4jQ1/',  seve_neo4jQuery_funcQ1_entityRel, name='seve_neo4jQuery_nameQ1_entityRel'),
    path('entityRelNeo4jQ2/',  seve_neo4jQuery_funcQ2_entityRel, name='seve_neo4jQuery_nameQ2_entityRel'),
    path('entityRelNeo4jQ3/',  seve_neo4jQuery_funcQ3_entityRel, name='seve_neo4jQuery_nameQ3_entityRel'),
    path('entityRelNeo4jQ4/',  seve_neo4jQuery_funcQ4_entityRel, name='seve_neo4jQuery_nameQ4_entityRel'),
    path('entityRelNeo4jQ5/',  seve_neo4jQuery_funcQ5_entityRel, name='seve_neo4jQuery_nameQ5_entityRel'),
    path('entityRelNeo4jQ6/',  seve_neo4jQuery_funcQ6_entityRel, name='seve_neo4jQuery_nameQ6_entityRel'),
    path('entityRelNeo4jQ7/',  seve_neo4jQuery_funcQ7_entityRel, name='seve_neo4jQuery_nameQ7_entityRel'),
    path('entityRelNeo4jQ8/',  seve_neo4jQuery_funcQ8_entityRel, name='seve_neo4jQuery_nameQ8_entityRel'),
    path('entityRelNeo4jQ9/',  seve_neo4jQuery_funcQ9_entityRel, name='seve_neo4jQuery_nameQ9_entityRel'),
    path('entityRelNeo4jQ10/',  seve_neo4jQuery_funcQ10_entityRel, name='seve_neo4jQuery_nameQ10_entityRel'),
    path('entityRelNeo4jQ11/',  seve_neo4jQuery_funcQ11_entityRel, name='seve_neo4jQuery_nameQ11_entityRel'),
    path('entityRelNeo4jQ12/',  seve_neo4jQuery_funcQ12_entityRel, name='seve_neo4jQuery_nameQ12_entityRel'),
    path('activityPropertiesNeo4jQ1/',  seve_neo4jQuery_funcQ1_activityProperties, name='seve_neo4jQuery_nameQ1_activityProperties'),
    path('activityPropertiesNeo4jQ2/',  seve_neo4jQuery_funcQ2_activityProperties, name='seve_neo4jQuery_nameQ2_activityProperties'),
    path('activityPropertiesNeo4jQ3/',  seve_neo4jQuery_funcQ3_activityProperties, name='seve_neo4jQuery_nameQ3_activityProperties'),
    path('activityPropertiesNeo4jQ4/',  seve_neo4jQuery_funcQ4_activityProperties, name='seve_neo4jQuery_nameQ4_activityProperties'),
    path('activityPropertiesNeo4jQ5/',  seve_neo4jQuery_funcQ5_activityProperties, name='seve_neo4jQuery_nameQ5_activityProperties'),
    path('DomainNeo4jQ1/',  seve_neo4jQuery_funcQ1_Domain, name='seve_neo4jQuery_nameQ1_Domain'),
    path('DomainNeo4jQ2/',  seve_neo4jQuery_funcQ2_Domain, name='seve_neo4jQuery_nameQ2_Domain'),
    path('DomainNeo4jQ3/',  seve_neo4jQuery_funcQ3_Domain, name='seve_neo4jQuery_nameQ3_Domain'),
    path('DomainNeo4jQ4/',  seve_neo4jQuery_funcQ4_Domain, name='seve_neo4jQuery_nameQ4_Domain'),
    path('ICDNeo4jQ1/',  seve_neo4jQuery_funcQ1_ICD, name='seve_neo4jQuery_nameQ1_ICD'),
    path('ICDNeo4jQ2/',  seve_neo4jQuery_funcQ2_ICD, name='seve_neo4jQuery_nameQ2_ICD'),
    path('ICDNeo4jQ3/',  seve_neo4jQuery_funcQ3_ICD, name='seve_neo4jQuery_nameQ3_ICD'),
    path('ICDNeo4jQ4/',  seve_neo4jQuery_funcQ4_ICD, name='seve_neo4jQuery_nameQ4_ICD'),
    path('SctNodeNeo4jQ1/',  seve_neo4jQuery_funcQ1_sctNode, name='seve_neo4jQuery_nameQ1_sctNode'),
    path('SctNodeNeo4jQ2/',  seve_neo4jQuery_funcQ2_sctNode, name='seve_neo4jQuery_nameQ2_sctNode'),
    path('SctNodeNeo4jQ3/',  seve_neo4jQuery_funcQ3_sctNode, name='seve_neo4jQuery_nameQ3_sctNode'),
    path('SctNodeNeo4jQ4/',  seve_neo4jQuery_funcQ4_sctNode, name='seve_neo4jQuery_nameQ4_sctNode'),
    path('SctRelNeo4jQ1/',  seve_neo4jQuery_funcQ1_sctRel, name='seve_neo4jQuery_nameQ1_sctRel'),
    path('SctRelNeo4jQ2/',  seve_neo4jQuery_funcQ2_sctRel, name='seve_neo4jQuery_nameQ2_sctRel'),
    path('SctRelNeo4jQ3/',  seve_neo4jQuery_funcQ3_sctRel, name='seve_neo4jQuery_nameQ3_sctRel'),
    path('DK3Neo4jQ1/',  seve_neo4jQuery_funcQ1_DK3, name='seve_neo4jQuery_nameQ1_DK3'),
    path('DK3Neo4jQ2/',  seve_neo4jQuery_funcQ2_DK3, name='seve_neo4jQuery_nameQ2_DK3'),
    path('DK4Neo4jQ1/',  seve_neo4jQuery_funcQ1_DK4, name='seve_neo4jQuery_nameQ1_DK4'),
    path('DK4Neo4jQ2/',  seve_neo4jQuery_funcQ2_DK4, name='seve_neo4jQuery_nameQ2_DK4'),
    path('DK5Neo4jQ1/',  seve_neo4jQuery_funcQ1_DK5, name='seve_neo4jQuery_nameQ1_DK5'),
    path('DK5Neo4jQ2/',  seve_neo4jQuery_funcQ2_DK5, name='seve_neo4jQuery_nameQ2_DK5'),
    path('DK5Neo4jQ3/',  seve_neo4jQuery_funcQ3_DK5, name='seve_neo4jQuery_nameQ3_DK5'),
    path('DK6Neo4jQ1/',  seve_neo4jQuery_funcQ1_DK6, name='seve_neo4jQuery_nameQ1_DK6'),
    path('DK6Neo4jQ2/',  seve_neo4jQuery_funcQ2_DK6, name='seve_neo4jQuery_nameQ2_DK6'),
    path('DK7Neo4jQ1/',  seve_neo4jQuery_funcQ1_DK7, name='seve_neo4jQuery_nameQ1_DK7'),
    path('DK7Neo4jQ2/',  seve_neo4jQuery_funcQ2_DK7, name='seve_neo4jQuery_nameQ2_DK7'),
    path('eventLogNeo4jQ4svg/', seve_neo4jQuery_svgQ4_EventLog, name='seve_neo4jQuery_svg_nameQ4_EventLog'),
    path('eventLogNeo4jQ5svg/', seve_neo4jQuery_svgQ5_EventLog, name='seve_neo4jQuery_svg_nameQ5_EventLog'),
    path('eventLogNeo4jQ6svg/', seve_neo4jQuery_svgQ6_EventLog, name='seve_neo4jQuery_svg_nameQ6_EventLog'),
    path('eventLogNeo4jQ7svg/', seve_neo4jQuery_svgQ7_EventLog, name='seve_neo4jQuery_svg_nameQ7_EventLog'),
    path('eventLogNeo4jQ8svg/', seve_neo4jQuery_svgQ8_EventLog, name='seve_neo4jQuery_svg_nameQ8_EventLog'),
    path('eventLogNeo4jQ9svg/', seve_neo4jQuery_svgQ9_EventLog, name='seve_neo4jQuery_svg_nameQ9_EventLog'),
    path('eventLogNeo4jQ10svg/', seve_neo4jQuery_svgQ10_EventLog, name='seve_neo4jQuery_svg_nameQ10_EventLog'),
    path('eventLogNeo4jQ11svg/', seve_neo4jQuery_svgQ11_EventLog, name='seve_neo4jQuery_svg_nameQ11_EventLog'),
    path('eventLogNeo4jQ12svg/', seve_neo4jQuery_svgQ12_EventLog, name='seve_neo4jQuery_svg_nameQ12_EventLog'),
    path('otherEntitiesNeo4jQ1svg/', seve_neo4jQuery_svgQ4_otherEntities,
         name='seve_neo4jQuery_svg_nameQ4_otherEntities'),
    path('entityRelNeo4jQ1svg/', seve_neo4jQuery_svgQ3_entityRel, name='seve_neo4jQuery_svg_nameQ3_entityRel'),
    path('entityRelNeo4jQ2svg/', seve_neo4jQuery_svgQ6_entityRel, name='seve_neo4jQuery_svg_nameQ6_entityRel'),
    path('entityRelNeo4jQ3svg/', seve_neo4jQuery_svgQ7_entityRel, name='seve_neo4jQuery_svg_nameQ7_entityRel'),
    path('entityRelNeo4jQ4svg/', seve_neo4jQuery_svgQ8_entityRel, name='seve_neo4jQuery_svg_nameQ8_entityRel'),
    path('entityRelNeo4jQ5svg/', seve_neo4jQuery_svgQ9_entityRel, name='seve_neo4jQuery_svg_nameQ9_entityRel'),
    path('entityRelNeo4jQ6svg/', seve_neo4jQuery_svgQ10_entityRel, name='seve_neo4jQuery_svg_nameQ10_entityRel'),
    path('entityRelNeo4jQ7svg/', seve_neo4jQuery_svgQ11_entityRel, name='seve_neo4jQuery_svg_nameQ11_entityRel'),
    path('entityRelNeo4jQ8svg/', seve_neo4jQuery_svgQ12_entityRel, name='seve_neo4jQuery_svg_nameQ12_entityRel'),
    path('activityPropertiesNeo4jQ1svg/', seve_neo4jQuery_svgQ4_activityProperties,
         name='seve_neo4jQuery_svg_nameQ4_activityProperties'),
    path('activityPropertiesNeo4jQ2svg/', seve_neo4jQuery_svgQ5_activityProperties,
         name='seve_neo4jQuery_svg_nameQ5_activityProperties'),
    path('DomainNeo4jQ4svg/', seve_neo4jQuery_svgQ4_Domain, name='seve_neo4jQuery_svg_nameQ4_Domain'),
    path('ICDNeo4jQ4svg/', seve_neo4jQuery_svgQ4_ICD, name='seve_neo4jQuery_svg_nameQ4_ICD'),
    path('SctNodeNeo4jQ1svg/', seve_neo4jQuery_svgQ4_sctNode, name='seve_neo4jQuery_svg_nameQ4_sctNode'),
    path('SctRelNeo4jQ1svg/', seve_neo4jQuery_svgQ2_sctRel, name='seve_neo4jQuery_svg_nameQ2_sctRel'),
    path('SctRelNeo4jQ2svg/', seve_neo4jQuery_svgQ3_sctRel, name='seve_neo4jQuery_svg_nameQ3_sctRel'),
    path('DK3Neo4jQ1svg/', seve_neo4jQuery_svgQ2_DK3, name='seve_neo4jQuery_svg_nameQ2_DK3'),
    path('DK4Neo4jQ2svg/', seve_neo4jQuery_svgQ2_DK4, name='seve_neo4jQuery_svg_nameQ2_DK4'),
    path('DK5Neo4jQ1svg/', seve_neo4jQuery_svgQ2_DK5, name='seve_neo4jQuery_svg_nameQ2_DK5'),
    path('DK5Neo4jQ2svg/', seve_neo4jQuery_svgQ3_DK5, name='seve_neo4jQuery_svg_nameQ3_DK5'),
    path('DK6Neo4jQ1svg/', seve_neo4jQuery_svgQ2_DK6, name='seve_neo4jQuery_svg_nameQ2_DK6'),
    path('DK7Neo4jQ1svg/', seve_neo4jQuery_svgQ2_DK7, name='seve_neo4jQuery_svg_nameQ2_DK7'),


    path('queryLister/', queryLister, name='queryLister'),
    path('queryListerQ1/',  seve_neo4jQuery_funcQ1_Final, name='seve_neo4jQuery_nameQ1_Final'),
    path('queryListerQ2/',  seve_neo4jQuery_funcQ2_Final, name='seve_neo4jQuery_nameQ2_Final'),
    path('queryListerQ3/',  seve_neo4jQuery_funcQ3_Final, name='seve_neo4jQuery_nameQ3_Final'),
    path('queryListerQ4/',  seve_neo4jQuery_funcQ4_Final, name='seve_neo4jQuery_nameQ4_Final'),
    path('queryListerQ5/',  seve_neo4jQuery_funcQ5_Final, name='seve_neo4jQuery_nameQ5_Final'),
    path('queryListerQ6/',  seve_neo4jQuery_funcQ6_Final, name='seve_neo4jQuery_nameQ6_Final'),
    path('queryListerQ7/',  seve_neo4jQuery_funcQ7_Final, name='seve_neo4jQuery_nameQ7_Final'),
    path('queryListerQ8/',  seve_neo4jQuery_funcQ8_Final, name='seve_neo4jQuery_nameQ8_Final'),
    path('queryListerQ9/',  seve_neo4jQuery_funcQ9_Final, name='seve_neo4jQuery_nameQ9_Final'),
    path('queryListerQ10/',  seve_neo4jQuery_funcQ10_Final, name='seve_neo4jQuery_nameQ10_Final'),
    path('queryListerQ11/',  seve_neo4jQuery_funcQ11_Final, name='seve_neo4jQuery_nameQ11_Final'),
    path('queryListerQ12/',  seve_neo4jQuery_funcQ12_Final, name='seve_neo4jQuery_nameQ12_Final'),
    path('queryListerQ13/',  seve_neo4jQuery_funcQ13_Final, name='seve_neo4jQuery_nameQ13_Final'),
    path('queryListerQ14/',  seve_neo4jQuery_funcQ14_Final, name='seve_neo4jQuery_nameQ14_Final'),
    path('queryListerQ15/',  seve_neo4jQuery_funcQ15_Final, name='seve_neo4jQuery_nameQ15_Final'),
    path('queryListerQ16/',  seve_neo4jQuery_funcQ16_Final, name='seve_neo4jQuery_nameQ16_Final'),
    path('queryListerQ17/',  seve_neo4jQuery_funcQ17_Final, name='seve_neo4jQuery_nameQ17_Final'),
    path('queryListerQ18/',  seve_neo4jQuery_funcQ18_Final, name='seve_neo4jQuery_nameQ18_Final'),
    path('queryListerQ19/', seve_neo4jQuery_funcQ19_Final, name='seve_neo4jQuery_nameQ19_Final'),
    path('queryListerQ20/', seve_neo4jQuery_funcQ20_Final, name='seve_neo4jQuery_nameQ20_Final'),
    path('queryListerQ21/', seve_neo4jQuery_funcQ21_Final, name='seve_neo4jQuery_nameQ21_Final'),
    path('queryListerQ22/', seve_neo4jQuery_funcQ22_Final, name='seve_neo4jQuery_nameQ22_Final'),
    path('queryListerQ3svg/', seve_neo4jQuery_svgQ3_Final, name='seve_neo4jQuery_svg_nameQ3_Final'),
    path('queryListerQ4svg/', seve_neo4jQuery_svgQ4_Final, name='seve_neo4jQuery_svg_nameQ4_Final'),
    path('queryListerQ5svg/', seve_neo4jQuery_svgQ5_Final, name='seve_neo4jQuery_svg_nameQ5_Final'),
    path('queryListerQ6svg/', seve_neo4jQuery_svgQ6_Final, name='seve_neo4jQuery_svg_nameQ6_Final'),
    path('queryListerQ7svg/', seve_neo4jQuery_svgQ7_Final, name='seve_neo4jQuery_svg_nameQ7_Final'),
    path('queryListerQ8svg/', seve_neo4jQuery_svgQ8_Final, name='seve_neo4jQuery_svg_nameQ8_Final'),
    path('queryListerQ9svg/', seve_neo4jQuery_svgQ9_Final, name='seve_neo4jQuery_svg_nameQ9_Final'),
    path('queryListerQ10svg/', seve_neo4jQuery_svgQ10_Final, name='seve_neo4jQuery_svg_nameQ10_Final'),
    path('queryListerQ11svg/', seve_neo4jQuery_svgQ11_Final, name='seve_neo4jQuery_svg_nameQ11_Final'),
    path('queryListerQ12svg/', seve_neo4jQuery_svgQ12_Final, name='seve_neo4jQuery_svg_nameQ12_Final'),
    path('queryListerQ13svg/', seve_neo4jQuery_svgQ13_Final, name='seve_neo4jQuery_svg_nameQ13_Final'),
    path('queryListerQ14svg/', seve_neo4jQuery_svgQ14_Final, name='seve_neo4jQuery_svg_nameQ14_Final'),
    path('queryListerQ15svg/', seve_neo4jQuery_svgQ15_Final, name='seve_neo4jQuery_svg_nameQ15_Final'),
    path('queryListerQ16svg/', seve_neo4jQuery_svgQ16_Final, name='seve_neo4jQuery_svg_nameQ16_Final'),
    path('queryListerQ17svg/', seve_neo4jQuery_svgQ17_Final, name='seve_neo4jQuery_svg_nameQ17_Final'),
    path('queryListerQ18svg/', seve_neo4jQuery_svgQ18_Final, name='seve_neo4jQuery_svg_nameQ18_Final'),
    path('queryListerQ19svg/', seve_neo4jQuery_svgQ19_Final, name='seve_neo4jQuery_svg_nameQ19_Final'),
    path('queryListerQ20svg/', seve_neo4jQuery_svgQ20_Final, name='seve_neo4jQuery_svg_nameQ20_Final'),
    path('queryListerQ21svg/', seve_neo4jQuery_svgQ21_Final, name='seve_neo4jQuery_svg_nameQ21_Final'),
    path('queryListerQ22svg/', seve_neo4jQuery_svgQ22_Final, name='seve_neo4jQuery_svg_nameQ22_Final'),



    path('DFG1/', DFG, name='DFG1'),
    path('serve-pdf/', serve_pdf_func, name='serve_pdf_name'),
    path('serve-dot/', serve_dot_func, name='serve_dot_name'),
    path('serve-graphvizQ/', serve_graphvizQuery_func, name='serve_graphvizQ_name'),
    path('serve-svg/', serve_svg_func, name='serve_svg_name'),
    path('serve-neo4jQ/', serve_neo4jQuery_func, name='serve_neo4jQ_name'),



]
