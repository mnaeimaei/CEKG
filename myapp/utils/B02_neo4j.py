

def Neo4J_relationship_massage(result):
    import ast
    output = ast.literal_eval(str(result))
    # print(output)
    if not output:
        output_string = f'''
            (no changes, no records)
        '''
    else:
        property_num = output["properties_set"]
        reltionship_num = output["relationships_created"]
        output_string = f'''
            Set {property_num} properties, created {reltionship_num} relationships
        '''
    return print(output_string)


def Neo4J_relationship_delete(result):
    import ast
    output = ast.literal_eval(str(result))
    #print(output)
    if not output:
        output_string = f'''
            (no changes, no records)
        '''
    else:
        property_num = output["relationships_deleted"]
        output_string = f'''
            Deleted {property_num} relationship
        '''
    return print(output_string)

def Neo4J_relationship_and_Node_delete(result):
    import ast
    output = ast.literal_eval(str(result))
    #print(output)
    if not output:
        output_string = f'''
            (no changes, no records)
        '''
    else:
        rel_del = output["relationships_deleted"]
        node_del = output["nodes_deleted"]
        output_string = f'''
            Deleted {node_del} node, deleted {rel_del} relationship
        '''
    return print(output_string)




def Neo4J_relationship_create(result):
    import ast
    output = ast.literal_eval(str(result))
    #print(output)
    if not output:
        output_string = f'''
            (no changes, no records)
        '''
    else:
        property_num = output["relationships_created"]
        output_string = f'''
            Created {property_num} relationship
        '''
    return print(output_string)


def Neo4J_properties_set(result):
    import ast
    output = ast.literal_eval(str(result))
    #print(output)
    if not output:
        output_string = f'''
            (no changes, no records)
        '''
    else:
        property_num = output["properties_set"]
        output_string = f'''
            Set {property_num} properties
        '''
    return print(output_string)


def Neo4J_label_node_property(result):
    import ast
    output = ast.literal_eval(str(result))
    #print(output)
    if not output:
        output_string = f'''
            (no changes, no records)
        '''
    else:
        property1 = output["labels_added"]
        property2 = output["nodes_created"]
        property3 = output["properties_set"]
        output_string = f'''
            Added {property1} label, created {property2} node, set {property3} properties

        '''
    return print(output_string)


def Neo4J_removingConstraint(result):
    import ast
    output = ast.literal_eval(str(result))
    #print(output)
    if not output:
        output_string = f'''
            (no changes, no records)
        '''
    else:
        property_num = output["constraints_removed"]
        output_string = f'''
            Removed {property_num} constraint

        '''
    return print(output_string)


def Neo4J_creatingConstraint(result):
    import ast
    output = ast.literal_eval(str(result))
    #print(output)
    if not output:
        output_string = f'''
            (no changes, no records)
        '''
    else:
        property_num = output["constraints_added"]
        output_string = f'''
            Added {property_num} constraint

        '''
    return print(output_string)