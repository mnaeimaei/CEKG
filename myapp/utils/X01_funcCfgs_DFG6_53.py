def node1Finder(driver):
    query1 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE NOT EXISTS {{ (x)-[:INCLUDED]->(n) }} and n.Category="Absolute"
    RETURN  COLLECT (distinct LABELS(n))
    '''
    #print(query1)
    with driver.session() as session:
        record1 = session.run(query1).values()
        #print("record1=", record1)
        flat_list = record1[0][0]
        flattened_list = [label for sublist in flat_list for label in sublist]

    return flattened_list[0]


def nodeOtherRandomFinder(driver):


    query1 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE NOT EXISTS {{ (x)-[:INCLUDED]->(n) }} and n.Category="Absolute"
    RETURN  COLLECT (distinct LABELS(n))
    '''
    #print(query1)
    with driver.session() as session:
        record1 = session.run(query1).values()
        #print("record1=", record1)
        flat_list = record1[0][0]
        flattened_list = [label for sublist in flat_list for label in sublist]



    query2 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE NOT EXISTS {{ (z)-[:INCLUDED]->(y) }} and z.Category="Absolute"
    RETURN  COLLECT (distinct LABELS(z))
    '''
    #print(query1)
    with driver.session() as session:
        record2 = session.run(query2).values()
        #print("record1=", record1)
        flat_list2 = record2[0][0]
        flattened_list2 = [label for sublist in flat_list2 for label in sublist]




    query3 = f'''     
    MATCH (n)-[:INCLUDED]->(z)
    WHERE z.Category="Absolute" and n.Category="Absolute"
    RETURN COLLECT(DISTINCT LABELS(z)) + COLLECT(DISTINCT LABELS(n)) AS combinedLabels
    '''
    #print(query1)
    with driver.session() as session:
        record3 = session.run(query3).values()
        #print("record3=", record3)
        flat_list3 = record3[0][0]
        flattened_list3 = [label for sublist in flat_list3 for label in sublist]
        no_duplicates_list = list(set(flattened_list3))

    #print(no_duplicates_list)

    result1 = [item for item in no_duplicates_list if item not in flattened_list]
    result2 = [item for item in result1 if item not in flattened_list2]

    #print(result2)

    import random
    random_item = random.choice(result2)
    return random_item



from graphviz import Digraph
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

def case_Selector(cases):
    txt = " where r.sourceID in "
    case_selector = txt + str(cases)
    return case_selector

def create_color(list1, list2):
    list3 = []
    for item in list2:
        index = int(item) - 1  # Subtract 1 to convert 1-based index to 0-based index
        if 0 <= index < len(list1):
            list3.append(list1[index])
        else:
            list3.append(None)  # Handle the case where index is out of bounds
    return list3

def create_color_2(list1, list2):
    list3 = []
    for item in list2:
        index = int(item[1]) - 1  # Subtract 1 to convert 1-based index to 0-based index
        if 0 <= index < len(list1):
            item.append(list1[index])
            list3.append(item)
        else:
            list3.append(None)  # Handle the case where index is out of bounds
    return list3

###################Graph Functions"""""""""""""""""""""""""""""""""""