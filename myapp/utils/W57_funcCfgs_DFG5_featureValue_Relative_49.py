import B02_neo4j as myNeo

def Finading_Entities_ID(driver,col1,entityListIDproperty, conditionProperty, conditionPropertyValue):
    listFinal=[]
    for i in range(len(col1)):
        EnityName=col1[i]
        idCol=entityListIDproperty[i]
        prop=conditionProperty[i]
        val = conditionPropertyValue[i]
        #print(EnityName)

        query1 = f'''     
        MATCH p=(e)-[:CORR]->(n:{EnityName})
        where n.{prop}="{val}"
        return distinct n.{idCol}
        '''

        print(query1)

        with driver.session() as session:
            record1 = session.run(query1).values()
            #print("record1=", record1)
            flat_list = [item for sublist in record1 for item in sublist]
            #print("flat_list=", flat_list)

        listFinal.append(flat_list)

    #print(listFinal)
    return listFinal


def idColumnAndValueMaler(EntityIDColumnList, EntityOriginIDValue, EnNum):
    list2 = []
    for i in range(EnNum):
        list1 = []
        list1.append(EntityIDColumnList[i])
        list1.append(EntityOriginIDValue[i])
        list2.append(list1)

    return list2


def Final_AG_forListID(En1, En2, idColumnAndValue):
    list2 = []
    list2.append(En1)
    list2.append(En2)
    for i in range(len(idColumnAndValue)):
        if En2 == idColumnAndValue[i][0]:
            list2.append(idColumnAndValue[i][1])
    return list2



def case_Selector1(cases):
    txt = " df.En1_ID IN "
    txt2 = " n1.ID IN "
    case_selector1 = txt + str(cases)
    case_selector3 = txt2 + str(cases)
    return case_selector1, case_selector3, cases

def case_Selector2(cases):
    txt = " df.En2_ID IN "
    txt2 = " n1.ID IN "
    case_selector2 = txt + str(cases)
    case_selector4 = txt2 + str(cases)
    return case_selector2, case_selector4, cases



def Type_Entities_ID(driver,name, label, value, compare):

    query1 = f'''     
    MATCH (e:Event)-[r:Assign]->(f:Feature) 
    WHERE e.Activity = f.Name 
    AND f.Name = "{name}" 
    AND f.label IN {label}
    AND f.Value IN {value}
    WITH id(f) as x, collect(DISTINCT e.Event) AS events
    WITH collect(events) AS allEvents
    with reduce(commonEvents = allEvents[0], events IN tail(allEvents) | apoc.coll.intersection(commonEvents, events)) as value
    UNWIND range(0,size(value)-1) AS i
    MATCH (n )<-[:CORR]-(e:Event)
    where n.Category = "Absolute" and e.Event=value[i] 
    return n.Type, collect(DISTINCT n.ID) as ID
        '''
    print(query1)
    with driver.session() as session:
        record1 = session.run(query1).values()
        #print("record1=", record1)
    compare1 = []
    for item in record1:
        if item[0] in compare:
            compare1.append(item[1])
    print("result=", compare1[0])
    return compare1[0]


#************************** Create Graph: ****************************************************************************
def deleteRelation(tx, relationTypes):
    qDeleteRelation = f'''MATCH ()-[r:DF_C {{Type:"{relationTypes}"}}]->() DELETE r;'''
    print(qDeleteRelation)
    tx.run(qDeleteRelation)

def aggregateDF_RelativeProperty(tx, En1, En2, eID):
    # most basic aggregation of DF: all DF edges between events of the same classifer between the same entity
    qCreateDF_Relative = f'''
        MATCH ( c1 : ActivityPropery ) <-[:MONITORED]- ( e1 : Event ) -[df1:DF]-> ( e2 : Event ) -[:MONITORED]-> ( c2 : ActivityPropery )
        MATCH ( c1 : ActivityPropery ) <-[:MONITORED]- ( e1 : Event ) -[df2:DF]-> ( e2 : Event ) -[:MONITORED]-> ( c2 : ActivityPropery )
        MATCH (e1) -[:CORR] -> (n1:{En1}) <-[:CORR]- (e2)
        MATCH (e1) -[:CORR] -> (n2:{En2}) <-[:CORR]- (e2)
        WHERE c1.Type = c2.Type 
        AND n1.Type = df1.Type  AND n1.ID = df1.ID
        AND n2.Type = df2.Type  AND n2.ID = df2.ID AND n2.ID="{eID}"
        WITH c1,count(df1) AS df_freq,c2, n1.ID as IDT1, n2.ID as IDT2
        MERGE ( c1 ) -[rel2:DF_C {{Type:"RelativeProperty" , count:df_freq , En1_ID:IDT1 ,En2_ID:IDT2 , En1:"{En1}" , En2:"{En2}" , Category:"wProperty" }}]-> ( c2 ) 
        '''


    qTest = f'''
            ######### Testing:######################################
            MATCH rel=( c1 ) -[:DF_C ]-> ( c2 )
            return rel;


            #############################################################
            '''
    print(qCreateDF_Relative)
    Result = tx.run(qCreateDF_Relative).consume().counters
    myNeo.Neo4J_relationship_massage(Result)
    print(qTest)



def DF_RelativePropery(tx):
    # most basic aggregation of DF: all DF edges between events of the same classifer between the same entity
    qCreateDF_All = f'''
        MATCH p1=(c1)-[d:DF_C {{Type:"RelativeProperty" }}]->(c2)
        MATCH p2=(c1)<-[r:MONITORED]-(e1)-[a:Assign]->(f)
        WITH 
        c2,
        d.Category  as Category,
        d.En1  as En1,
        d.En1_ID  as En1_ID,
        d.En2  as En2,
        d.En2_ID  as  En2_ID,
        d.Type  as Type,
        d.count  as count,
        f      
        MERGE ( f ) -[:DF_C {{Category:Category , En1:En1 , En1_ID:En1_ID , En2:En2 , En2_ID:En2_ID , Type:Type , count:count }}]-> ( c2 ) 

            '''

    qTest = f'''
            ######### Testing:######################################
            MATCH rel=( c1 ) -[:DF_C ]-> ( c2 )
            return rel;



            #############################################################
            '''
    print(qCreateDF_All)
    Result = tx.run(qCreateDF_All).consume().counters
    myNeo.Neo4J_relationship_massage(Result)
    print(qTest)


from itertools import chain, permutations
import itertools
import re
import copy
from graphviz import Digraph
#############Intoductory Functions##################################################



def Finading_Entities_ID(driver,entityList,entityListIDproperty,conditionProperty,conditionPropertyValue):

    listFinal=[]
    for i in range(len(entityList)):
        EnityName=entityList[i]
        id = entityListIDproperty[i]
        pro = conditionProperty[i]
        Value = conditionPropertyValue[i]


        #print(EnityName)
        query1 = f'''     
        MATCH p=(e)-[:CORR]->(n:{EnityName})
        where  n.{pro}="{Value}"
        return distinct n.{id}
        '''
        print(query1)
        with driver.session() as session:
            record1 = session.run(query1).values()
            #print("record1=", record1)
            flat_list = [item for sublist in record1 for item in sublist]
            #print("flat_list=", flat_list)
        listFinal.append(flat_list)
    #print(listFinal)
    return listFinal


def Finading_Entities_ID_2(driver,Entity2):
    listFinal=[]
    # print(EnityName)
    query1 = f'''     
            MATCH p=(e)-[:CORR]->(n:{Entity2})
            return distinct n.ID
            '''
    print(query1)
    with driver.session() as session:
        record1 = session.run(query1).values()
        # print("record1=", record1)
        flat_list = [item for sublist in record1 for item in sublist]
        # print("flat_list=", flat_list)
    listFinal.append(flat_list)

    #print(listFinal)
    return listFinal

def relationship_rel(Entity1,Entity2,entityIDlists):
    list1=[Entity1]
    list2=[Entity2]
    list3=list1+list2+entityIDlists
    return list3

def convert_to_list_of_lists(input_list):
    return [[item] for item in input_list]


def EntityOriginValue_Temp(EntityOrgValue, EnNum):
    flat_list = [item for sublist in EntityOrgValue for item in sublist]
    list1 = []
    for i in range(EnNum):
        list1.append(flat_list)

    return list1


def Finading_Reified_Entities_ID2(driver, col1):
    listFinal = []
    for i in range(len(col1)):
        EnityName = col1[i]
        # print(EnityName)

        query1 = f'''     
        MATCH p=(e)-[:CORR]->(n:{EnityName})
        where  n.Category="Relative" 
        return distinct n.ID
        order by n.ID
        '''

        print(query1)

        with driver.session() as session:
            record1 = session.run(query1).values()
            # print("record1=", record1)
            flat_list = [item for sublist in record1 for item in sublist]
            # print("flat_list=", flat_list)

        listFinal.append(flat_list)

    # print(listFinal)
    return listFinal


def combining_IDs_List_func(EnNum, myListA, myListB):
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    myList = []
    for i in range(EnNum):
        k1 = myList1[i]
        k2 = myList2[i]
        k1.extend(k2)
        myList.append(k1)

    return myList


def color_combine(combining_IDs_List):
    k = -1
    list2 = []
    for i in range(len(combining_IDs_List)):
        list1 = []
        for j in range(len(combining_IDs_List[i])):
            list1.append(k + 1)
            k = k + 1
        list2.append(list1)

    return list2


def two_pair_permutations(myList):
    result = list(chain.from_iterable([permutations(myList, x) for x in range(len(myList) + 1)]))
    result = [list(k) for k in result]

    final = []
    for i in result:
        if len(i) == 2:
            final.append(i)

    return final


def discrete_combination_fun(myListA):
    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    myList1 = copy.deepcopy(myListA)
    myList2 = []
    # print(myList1)
    if myList1:
        for i in range(len(myListA)):
            s1 = []
            s2 = []
            s3 = []
            k1 = myList1[i][0]
            k2 = myList1[i][1]
            s1.insert(0, k1)
            s2.insert(0, k2)
            s3.append(s1)
            s3.append(s2)
            myList2.append(s3)
    else:
        myList2 = []

    return myList2


def entity_basedon_column_2(EnNum, myListA, myListB):
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    myList = []
    for i in range(EnNum):
        k1 = myList1[i]
        k2 = myList2[i]
        k1.extend(k2)
        myList.append(k1)

    return myList




def EntityOrgAG3_Func_2(myListA, myListB, myListC):
    # print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    myList3 = copy.deepcopy(myListC)
    # print("myList1=",myList1)
    # print("myList2=", myList2)
    listFinal = []
    for i in range(len(myList2)):
        # print("AAAAAAAAAAAAAAAAAAAAa")
        item1myList2 = myList2[i][0][0]
        # print("item1myList2=", item1myList2)
        for j in range(len(myList1)):
            item1myList1 = myList1[j][0]
            item1myList3 = myList3[j][0]
            # print("item1myList1=", item1myList1)
            if item1myList2 == item1myList1:
                # print("yes")
                myList2[i].append(myList1[j][1:])
                # print(myList2[i])
            if item1myList2 == item1myList3:
                # print("yes")
                myList2[i].append(myList3[j][1:])
                # print(myList2[i])

        listFinal.append(myList2[i])

    return listFinal


def final_DFG_List_func_2(myListA):
    myList1 = copy.deepcopy(myListA)
    # print("myList1=",myList1)
    # print("len(myList1)=", len(myList1))

    if myList1:
        myList = []
        for i in range(len(myList1)):
            k1 = myList1[i][0]
            k2 = myList1[i][1]
            t1 = myList1[i][2]
            s1 = myList1[i][3]

            # print("k1=", k1)
            # print("k2=", k2)
            # print("t3=", t1)
            e3 = list(itertools.product(k1, k2, t1))
            e4 = [list(tup) for tup in e3]
            # print("e4=", e4)

            for f in range(len(e4)):
                e4[f].append(s1[f])

            myList.append(e4)
    else:
        myList = []

    return myList



def final_DFG_List_func_3(myListA):
    myList1 = copy.deepcopy(myListA)
    # print("myList1=",myList1)
    # print("len(myList1)=", len(myList1))

    if myList1:
        myList = []
        for i in range(len(myList1[2])):
            listTemp=[]
            k1 = myList1[0]
            k2 = myList1[1]
            k3 = myList1[2][i]
            k4 = i
            listTemp.append(k1)
            listTemp.append(k2)
            listTemp.append(k3)
            listTemp.append(k4)
            myList.append(listTemp)

    else:
        myList = []

    return myList

#############Intoductory Functions##################################################


def Entity_DF_Show(RelNum, input):
    List1 = []
    for x in range(1, RelNum + 1):
        # print(x)
        moduleVaribale = 'Type5_Rel_' + str(x) + '_DF_Show'
        #print(moduleVaribale)
        if hasattr(input, moduleVaribale) == True:
            moduleVaribale2 = (getattr(input, moduleVaribale))
        else:
            moduleVaribale2 = 0
            #print(moduleVaribale2)
        List1.append(moduleVaribale2)
    # print(dicEntity)
    return List1


def entityFinder(driver):

    query1 = f'''     
    MATCH p=()-[r:DF_C]->()
    where r.Type="Relative"
    RETURN distinct r.En1, r.En2
    '''
    print(query1)
    with driver.session() as session:
        record1 = session.run(query1).values()
        #print("record1=", record1)
        flat_list = [item for sublist in record1 for item in sublist]
        #print("flat_list=", flat_list)
    return flat_list[0], flat_list[1]
