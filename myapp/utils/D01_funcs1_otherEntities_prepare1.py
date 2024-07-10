import pandas as pd
import time, os, csv
from itertools import combinations
from itertools import chain, permutations
import itertools
import re
import copy
from neo4j import GraphDatabase



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

def CreateLoL(dataset):
    list_of_lists = dataset.values.tolist()
    modified_list_of_lists = [sublist[1:] for sublist in list_of_lists]
    modified_list_of_lists.append(['Disorder', 'UNK', 'UNK','UNK', 'Absolute'])
    modified_list_of_lists.append(['Disorder', 'Nothing', 'Nothing','Nothing', 'Absolute'])
    return modified_list_of_lists


def CreateEntity(list_of_lists):
    list1 = [sublist[0] for sublist in list_of_lists]
    list2 = list(set(list1))
    return list2




