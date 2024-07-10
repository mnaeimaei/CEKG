import pandas as pd
import time, os, csv
from itertools import combinations
from itertools import chain, permutations
import itertools
import re
import copy
from neo4j import GraphDatabase










def creatingDfFromGraph(driver):
    query1 = f'''     
    MATCH  (p:Patient)<-[:CORR]-(e:Event)-[:CORR]->(a:Admission)-[:INCLUDED]->(m:Multimorbidity) -[:INCLUDED]->(d:Disorder) 
    where p.Category="Absolute" and a.Category="Absolute"  
    RETURN p.ID, e.timestamp, a.ID, m.Name, d.Name
    ;
    '''
    print(query1)
    with driver.session() as session:
        record = session.run(query1).values()
        print("record=", record)
    x=[]
    for item in record:
        #print(item)
        item[1] = item[1].isoformat()
        #print(item)
        x.append(item)

    df = pd.DataFrame(x, columns=['Patient', 'Timestamp', 'Admission', 'Multimorbidity', 'Disorder'])
    return df



def rankingAdm(df):
    columns_order = ['Patient', 'Admission', 'Timestamp']
    new_df = df[columns_order]
    result = new_df.groupby(['Patient', 'Admission'])['Timestamp'].max().reset_index(name='MaxT')
    #print(result)
    result_sorted = result.sort_values(by=['Patient', 'MaxT'])
    #print(result_sorted)
    # Group by 'A1', 'A2', and 'C' and use cumcount to create the 'Row' column

    result_sorted['Row'] = result_sorted.groupby(['Patient']).cumcount('Admission') + 1
    #print(result_sorted)
    fianl_df = result_sorted[['Patient', 'Admission','Row']]
    # Now, df includes the 'Row' column as in Table2
    return fianl_df


def groupingDisorder(df1):
    df3 = df1[['Patient', 'Admission','Disorder']]
    df2 = df3.drop_duplicates()
    #print(df2)
    conditioned_sorted_df = df2.sort_values(by='Disorder')
    result = conditioned_sorted_df.groupby(['Patient', 'Admission'])['Disorder'].agg(','.join).reset_index(name='Disorders')
    return result

def lefJoinTable(df1,df2):
    result = pd.merge(df1, df2, left_on='Admission', right_on='Admission', how='left')
    df3 = result[['Patient_x', 'Admission','Row', 'Disorders']]
    df4=df3.copy()
    df4.rename(columns={'Patient_x': 'Patient'}, inplace=True)

    return df4


import ast

def comparing(df1):
    df2=df1.copy()
    df13=df1.copy()
    df2['Row'] = df2['Row'] - 1
    df13['Row'] = df13['Row'] + 1
    result = pd.merge(df1, df2, left_on=['Patient', 'Row'], right_on=['Patient', 'Row'], how='left')
    df3=result.copy()
    df3 = df3[['Patient', 'Admission_x','Row', 'Disorders_x', 'Disorders_y']]
    df4=df3.copy()
    df4.rename(columns={'Admission_x': 'Admission','Disorders_x': 'Disorders','Disorders_y': 'Next', }, inplace=True)
    df5 = pd.merge(df4, df13, left_on=['Patient', 'Row'], right_on=['Patient', 'Row'], how='left')
    df5.rename(columns={'Admission_x': 'Admission','Disorders_y': 'Previous' ,'Disorders_x': 'Disorders' }, inplace=True)
    df6=df5.copy()
    df6 = df6[['Patient', 'Admission','Row', 'Disorders', 'Next', 'Previous']]
    df6.fillna('UNK', inplace=True)
    df6['Disorders'] = df6['Disorders'].str.split(',')
    df6['Next'] = df6['Next'].str.split(',')
    df6['Previous'] = df6['Previous'].str.split(',')
    return df6

def createFinal(df):
    df['Treated'] = df.apply(lambda x: [item for item in x['Disorders'] if item not in x['Next']], axis=1)
    df['New'] = df.apply(lambda x: [item for item in x['Disorders'] if item not in x['Previous']], axis=1)
    df['notTreated'] = df.apply(lambda x: [item for item in x['Next'] if item in x['Disorders']], axis=1)
    df.loc[df['Previous'].apply(lambda x: 'UNK' in x), 'New'] = 'UNK'
    df.loc[df['Next'].apply(lambda x: 'UNK' in x), 'Treated'] = 'UNK'
    df.loc[df['Next'].apply(lambda x: 'UNK' in x), 'notTreated'] = 'UNK'
    df = df.map(lambda x: 'Nothing' if x == [] else x)
    df2=df.copy()
    df2 = df2[['Patient', 'Admission','Row', 'Treated', 'New', 'notTreated']]
    #print(df.to_string())
    return df2

def createTreated(df,value):
    df2=df.copy()
    df2 = df2[['Patient', 'Admission', value]]
    df_exploded = df2.explode(value)
    df3=df_exploded.copy()
    print(f'''\ndf{value}=\n''', df3)
    df3 = df3[[ 'Admission', value]]
    list_of_lists = df3.values.tolist()
    return list_of_lists

def multiDis(df):
    df2=df.copy()
    df3 = df2[['Admission', "Disorders"]]
    list_of_lists = df3.values.tolist()
    return list_of_lists


def treatVal(df):
    df['Treated'] = df['Treated'].apply(lambda x: x if isinstance(x, list) else [x])
    df2=df.copy()
    df3 = df2[['Admission', "Treated"]]
    list_of_lists = df3.values.tolist()
    treatedValue = [[x[0], ','.join(x[1])] for x in list_of_lists]
    return treatedValue


def notVal(df):
    df['New'] = df['New'].apply(lambda x: x if isinstance(x, list) else [x])
    df2=df.copy()
    df3 = df2[['Admission', "New"]]
    list_of_lists = df3.values.tolist()
    treatedValue = [[x[0], ','.join(x[1])] for x in list_of_lists]
    return treatedValue

def newVal(df):
    df['notTreated'] = df['notTreated'].apply(lambda x: x if isinstance(x, list) else [x])
    df2=df.copy()
    df3 = df2[['Admission', "notTreated"]]
    list_of_lists = df3.values.tolist()
    treatedValue = [[x[0], ','.join(x[1])] for x in list_of_lists]
    return treatedValue

