from graphviz import Digraph


#############Intoductory Functions##################################################

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

def EntityOriginValue_Temp(EntityOrgValue, EnNum):
    flat_list = [item for sublist in EntityOrgValue for item in sublist]
    list1 = []
    for i in range(EnNum):
        list1.append(flat_list)
    return list1


def NumberEntityOriginAbr(EntityOriginValue_First, EnNum):
    dicNumEntOrgAbr = {}
    for s in range(0, EnNum):
        list4 = EntityOriginValue_First[s]
        if not list4:
            moduleVaribale = float("nan")
        else:
            # findingNumber###################################
            x = len(list4)
            result = max(len(x) for x in list4)
            for s2 in range(result):
                final = s2 + 1
                p = []
                for i in range(x):
                    k = list4[i]
                    d = k[:s2 + 1]
                    p.append(d)
                p = list(dict.fromkeys(p))
                if len(p) == x:
                    break
            # findingNumber####################################
            moduleVaribale = final

        dicNumEntOrgAbr["nEnt{0}Org_Abr".format(s + 1)] = moduleVaribale
    return dicNumEntOrgAbr



def Entity_DF_Show(EnNum, input):
    List1 = []
    for x in range(1, EnNum + 1):
        # print(x)
        moduleVaribale = 'Type1_Entity' + str(x) + '_DF_Show'
        # print(moduleVaribale)
        if hasattr(input, moduleVaribale) == True:
            moduleVaribale2 = (getattr(input, moduleVaribale))
        else:
            moduleVaribale2 = 0
            # print(moduleVaribale2)
        List1.append(moduleVaribale2)
    # print(dicEntity)
    return List1


def case_Selector(Attribute, cases):
    concatenated_output = ""
    for i in range(len(Attribute)):
        list1 = ""
        if i ==0:
            txt = " (n1.Type=\"{1}\" AND n1.ID IN {0})"
            case_selector = txt.format(cases[i], Attribute[i])
        else:
            txt = " or (n1.Type=\"{1}\" AND n1.ID IN {0})"
            case_selector = txt.format(cases[i], Attribute[i])
        concatenated_output += case_selector

    return " (" + concatenated_output + " )"


def Domain_colors_creater(DomainValue, NodeColors):
    list1 = []
    for i in range(len(DomainValue)):
        list2 = []
        list2.append(DomainValue[i])
        list2.append(NodeColors[i])
        list1.append(list2)
    return list1


def domainColumn (input):
    dicDomain = {}
    # print(x)
    moduleVaribale = 'ED_Domain'
    # print(moduleVaribale)
    if hasattr(input, moduleVaribale) == True:
        moduleVaribale2 = (getattr(input, moduleVaribale))
        # print(moduleVaribale2)
        dicDomain["Domain"] = moduleVaribale2
    else:
        moduleVaribale2 = float("nan")
        # print(moduleVaribale2)
        dicDomain["Domain"] = moduleVaribale2


    # print(dicEntity)
    return dicDomain



def Finading_DomainValue(driver,col1,domainColTitle):
    domainNode = col1[0]
    # print(EnityName)

    query1 = f'''     

            MATCH (:Activity)-[r:TYPE_OF]->(n:{domainNode}) RETURN distinct n.{domainColTitle} 
            '''

    print(query1)

    with driver.session() as session:
        record1 = session.run(query1).values()
        # print("record1=", record1)
        flat_list = [item for sublist in record1 for item in sublist]
        # print("flat_list=", flat_list)

    return flat_list

