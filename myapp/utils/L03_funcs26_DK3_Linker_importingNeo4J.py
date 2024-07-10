import pandas as pd
import time, csv
from neo4j import GraphDatabase


def deleteRelation(tx, relationTypes, queryLocation):
    for relType in relationTypes:
        qDeleteRelation = f'''MATCH () -[r:{relType}]- () DELETE r;'''
        print(qDeleteRelation)
        tx.run(qDeleteRelation)
        with open(queryLocation, 'a') as file:
            file.write(f'''//deleteRelation''')
            file.write(f'''\n{qDeleteRelation}\n\n''')

def deletePartiallyRel(tx, rel, where, val, queryLocation):
    qDeleteRelation = f'''MATCH ( e ) -[r:{rel}]-> ( p ) where r.{where}="{val}" DELETE r;'''
    print(qDeleteRelation)
    tx.run(qDeleteRelation)
    with open(queryLocation, 'a') as file:
        file.write(f'''//deletePartiallyRel''')
        file.write(f'''\n{qDeleteRelation}\n\n''')


def Entity1_Potential_Entities(tx, multiMorbidity,	icd_code_syn, queryLocation):

    qLinkSCTs = f''' 
            MATCH ( n:Disorder ) WHERE n.Name="{multiMorbidity}"
            MATCH ( s:Clinical ) WHERE s.icdCode="{icd_code_syn}" 
            CREATE ( n ) -[:LINKED_TO]-> ( s );
            '''
    print(qLinkSCTs)
    tx.run(qLinkSCTs)

    qTesting = f'''
            #########Testing:#######################################
            MATCH p=( n:Disorder ) -[:LINKED_TO]-> (s:Clinical)
            RETURN p;
            
            
            ##############################################################
            '''
    print("Testing:")
    print(qTesting)
    with open(queryLocation, 'a') as file:
        file.write(f'''//Entity1_Potential_Entities''')
        file.write(f'''\n{qLinkSCTs}\n\n''')




################################################################################

