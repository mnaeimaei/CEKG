import copy
def pageSequence(pageNext,List1,goalList,cPage,savingPageSequence):
    copied_goalList = copy.deepcopy(goalList)
    copied_list1 = copy.deepcopy(List1)
    copied_pageNext = copy.deepcopy(pageNext)


    last_item = copied_pageNext[-1]
    last_goal_index = copied_list1.index(last_item)

    copied_pageNext.pop()
    copied_pageNext.insert(0, '0')
    for numb, item in zip(copied_pageNext,copied_goalList):
        for i in copied_list1:
            if i == numb:
                index = copied_list1.index(i)
                copied_list1[index] = item

    copied_list1[last_goal_index] = cPage

    with open(savingPageSequence, 'w') as file:
        file.write(f'''{copied_list1}''')

    return copied_list1


def pageSequence2(pageNext,List1,goalList,cPage,savingPageSequence):
    copied_goalList = copy.deepcopy(goalList)
    copied_list1 = copy.deepcopy(List1)
    copied_pageNext = copy.deepcopy(pageNext)


    last_item = copied_pageNext[-1]
    last_goal_index = copied_list1.index(last_item)

    copied_pageNext.pop()
    copied_pageNext.insert(0, '0')
    for numb, item in zip(copied_pageNext,copied_goalList):
        for i in copied_list1:
            if i == numb:
                index = copied_list1.index(i)
                copied_list1[index] = item

    copied_list1[last_goal_index] = cPage

    if "DK62Neo4jName" in copied_list1:
        copied_list1.remove("DK62Neo4jName")

    if '15' in copied_list1:
        copied_list1.remove('15')

    with open(savingPageSequence, 'w') as file:
        file.write(f'''{copied_list1}''')

    return copied_list1


def pageSequence3(pageNext,List1,goalList,cPage,savingPageSequence):
    copied_goalList = copy.deepcopy(goalList)
    copied_list1 = copy.deepcopy(List1)
    copied_pageNext = copy.deepcopy(pageNext)


    last_item = copied_pageNext[-1]
    last_goal_index = copied_list1.index(last_item)

    copied_pageNext.pop()
    copied_pageNext.insert(0, '0')
    for numb, item in zip(copied_pageNext,copied_goalList):
        for i in copied_list1:
            if i == numb:
                index = copied_list1.index(i)
                copied_list1[index] = item

    copied_list1[last_goal_index] = cPage

    if ['ZZZZZ.py'] in copied_list1:
        copied_list1.remove(['ZZZZZ.py'])

    if '15' in copied_list1:
        copied_list1.remove('15')

    with open(savingPageSequence, 'w') as file:
        file.write(f'''{copied_list1}''')

    return copied_list1