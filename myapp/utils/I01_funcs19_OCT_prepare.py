import pandas as pd
import time, os, csv


def CreateMappingRelation1(csvLog):
    csvLog9 = csvLog[["s0", "s0_code", "s1", "s1_code"]]
    csvLog9.reset_index(drop=True, inplace=True)

    Concept_Relation=[]
    x =len(csvLog.index)
    for i in range(x):
        list1=[]
        a=csvLog.iloc[i]["s0"]
        b=csvLog.iloc[i]["s0_code"]
        c=csvLog.iloc[i]["s1"]
        d=csvLog.iloc[i]["s1_code"]
        list1.append(a)
        list1.append(b)
        list1.append(c)
        list1.append(d)
        Concept_Relation.append(list1)
    return Concept_Relation








def Create_CSV_in_Neo4J_import(union, Neo4JImport, outputFileName):
    sampleIds = []
    sampleList = []  # create a list (of lists) for the sample data containing a list of events for each of the selected cases
    # fix missing entity identifier for one record: check all records in the list of sample cases (or the entire dataset)
    for index, row in union.iterrows():
        if sampleIds == [] :
            rowList = list(row)  # add the event data to rowList
            #print(rowList)
            sampleList.append(rowList)  # add the extended, single row to the sample dataset
            #print(sampleList)

    header = list(union)  # save the updated header data
    #print(header)
    logSamples = pd.DataFrame(sampleList, columns=header)  # create pandas dataframe and add the samples

    logSamples.fillna(0)
    logSamples.to_csv(Neo4JImport + outputFileName, index=True, index_label="idx", na_rep="Unknown")


