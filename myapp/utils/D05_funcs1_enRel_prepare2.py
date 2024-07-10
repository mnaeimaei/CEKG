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




def ListMaker(A):
    B = []
    for sublist in A:
        new_sublist = []
        i1 = sublist[0]
        i2 = sublist[1]
        i3 = sublist[2]
        i4 = sublist[3]
        new_sublist.append(i1)
        new_sublist.append(i2)
        new_sublist.append(i3)
        if ',' in i4:
            list1 = []
            x = i4.split(',')
            for item in x:
                immutable_copy = new_sublist[:]
                immutable_copy.append(item)
                list1.append(immutable_copy)
        else:
            immutable_copy2 = new_sublist[:]
            immutable_copy2.append(i4)
            list1=[immutable_copy2]

        B.extend(list1)
    return B


