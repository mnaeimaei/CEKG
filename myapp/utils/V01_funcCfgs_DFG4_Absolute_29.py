import copy
from itertools import chain, permutations
import itertools
from graphviz import Digraph
#############Intoductory Functions##################################################


def Entity_DF_Show(EnNum, input):
    List1 = []
    for x in range(1, EnNum + 1):
        # print(x)
        moduleVaribale = 'Type4_Entity' + str(x) + '_DF_Show'
        #print(moduleVaribale)
        if hasattr(input, moduleVaribale) == True:
            moduleVaribale2 = (getattr(input, moduleVaribale))
        else:
            moduleVaribale2 = 0
            #print(moduleVaribale2)
        List1.append(moduleVaribale2)
    # print(dicEntity)
    return List1

def case_Selector(cases):
    txt = " df.En1_ID IN "
    case_selector = txt + str(cases)
    return case_selector, cases



def Finading_Entities_ID(driver,col1,entityListIDproperty,conditionProperty,conditionPropertyValue):
    listFinal=[]
    for i in range(len(col1)):
        EnityName=col1[i]
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

def convert_to_list_of_lists(input_list):

    return [[item] for item in input_list]

def Finading_Reified_Entities_ID2(driver,col1):
    listFinal=[]
    for i in range(len(col1)):
        EnityName=col1[i]
        #print(EnityName)

        query1 = f'''     
        MATCH p=(e)-[:CORR]->(n:{EnityName})
        where  n.Category="Relative" 
        return distinct n.ID
        order by n.ID
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

def final_DFG_List_Absolute_2(EnNum, myListA, myListB, myListC):
    myList1 = copy.deepcopy(myListA)
    myList2 = copy.deepcopy(myListB)
    myList3 = copy.deepcopy(myListC)
    # print("myList1=",myList1)
    # print("myList2=",myList2)
    myList = []
    for i in range(EnNum):
        k1 = myList1[i]
        # print("k1=", k1)
        t1 = myList2[i]
        # print("k3=", t1)
        s1 = myList3[i]
        # print("s1=", s1)
        e3 = list(itertools.product(k1, t1))
        e4 = [list(tup) for tup in e3]
        # print("e4=", e4)
        for f in range(len(e4)):
            e4[f].append(s1[f])
        myList.append(e4)
    return myList