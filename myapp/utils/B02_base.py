
import pandas as pd
import time, os, csv
from itertools import combinations
from neo4j import GraphDatabase
from datetime import datetime

def file_path(directory):
    file_path = os.path.realpath(directory)
    return file_path


def create_csv_with_row(file_path):
    header = ['name', 'start', 'end', 'duration (second)']
    # Check if the file exists and delete it if it does
    if os.path.exists(file_path):
        os.remove(file_path)
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(header)
        print(f"CSV file '{file_path}' created successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def add_row_to_csv(file_path, start,end,stepName):
    start_time = datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    end_time = datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    duration = end - start
    new_row = [stepName, start_time, end_time, duration]
    print('completed after ' + str(duration * 1000) + ' ms')



    try:
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
        print("Row added successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



#general function
def time_spend_for(strg, start,end):
    print(strg,": took : " + str((end - start)) + " seconds.")

#Function for finding neo4j import directory




def Neo4j_import_dir (driver):
    Query =f'''
           Call dbms.listConfig() YIELD name, value WHERE name='server.directories.import' RETURN value
           '''
    with driver.session() as session:
        record = session.run(Query).values()
    #driver.close()
    print(record)
    Neo4JImport = record[0][0] + "/"
    return Neo4JImport




#Importing Input CSV File
def ImportCSV(inputFileName):
    csvLog = pd.read_csv(os.path.realpath(inputFileName), keep_default_na=True)  # load full log from csv

    csvLog.drop_duplicates(keep='first', inplace=True)  # remove duplicates from the dataset
    csvLog = csvLog.reset_index(drop=True)  # renew the index to close gaps of removed duplicates


    return csvLog


# load data from CSV and import into graph
def LoadLog(localFile):
    datasetList = []
    headerCSV = []
    i = 0
    with open(localFile) as f:
        reader = csv.reader(f)
        for row in reader:
            if (i == 0):
                headerCSV = list(row)
                i += 1
            else:
                datasetList.append(row)

    log = pd.DataFrame(datasetList, columns=headerCSV)

    return headerCSV, log




# run query for Neo4J database
def runQuery(driver, query):
    with driver.session() as session:
        result = session.run(query)
        if result != None:
            return result
        else:
            return None


def list_abr_number(list4):
    x=len(list4)
    result = max(len(x) for x in list4)
    #print(result)

    for s in range(result):
        final=s+1
        #print("SSSSSSSSSSSSSSSSSSSSSSS")
        p=[]
        #print(len(p))
        for i in range(x):
            k = list4[i]
            #print(k)
            d=k[:s+1]
            p.append(d)
            #print(k[:final])
        p = list(dict.fromkeys(p))
        #print(p)
        if len(p)==x:
            #print(final)
            break
    return final




def classifierResult(option_Contains_Lifecycle_Information):
    if option_Contains_Lifecycle_Information:
        classifier = "Activity+Lifecycle"
    else:
        classifier = "Activity"
    return classifier




