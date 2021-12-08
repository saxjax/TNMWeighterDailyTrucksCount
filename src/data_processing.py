import pandas as pd
import json
# import random
# from pandas.core.frame import DataFrame

## --------------------- FUNCTION DEFINITIONS FROM JSON --------------------- ##

def preprocess_tnm(tnm):
    # data = json.load(tnm)
    # data = json.dumps(data)
    # json_acceptable_string = data.replace("'", "\"")
    d = json.loads(tnm, strict=False)
    return d

def extract_node_data(d):
    node_data = []
    # Node data
    for node in d['nodes']:
        node_data.append(d['nodes'][node]['data'])
    return node_data

def extract_edge_data(d):
    edge_data = []
    for node in d['nodes']:
        for edge in d['nodes'][node]['edges']:
            edge_data.append(d['nodes'][node]['edges'][edge]['data'])
    return edge_data

def get_from_node_ids(d):
    edge_from_node_id = []
    # Edge from_node_id
    for node in d['nodes']:
        for edge in d['nodes'][node]['edges']:
            edge_from_node_id.append(d['nodes'][node]['edges'][edge]['from_node_id'])
    return edge_from_node_id

def get_to_node_ids(d):
    edge_to_node_id = []
    # Edge to_node_id
    for node in d['nodes']:
        for edge in d['nodes'][node]['edges']:
            edge_to_node_id.append(d['nodes'][node]['edges'][edge]['to_node_id'])
    return edge_to_node_id


def add_from_and_to_node_ids_to_edges(edge_data, edge_from_node_id, edge_to_node_id):
    # Adding from_node_id to the edge data 
    for x in range(len(edge_from_node_id)):
        edge_data[x].update( {'from_node_id' : edge_from_node_id[x]})

    # Adding to_node_id to the edge data 
    for x in range(len(edge_to_node_id)):
        edge_data[x].update( {'to_node_id' : edge_to_node_id[x]})

    return edge_data

def extract_node_ids(d):
    node_ids = []
    for node in d['nodes']:
        node_ids.append(node)
    return node_ids

def extract_edge_ids(d):
    edge_ids = []
    for node in d['nodes']:
        for edge in d['nodes'][node]['edges']:
            edge_ids.append(d['nodes'][node]['edges'][edge]['id'])
    return edge_ids

## Create dictionaries with node_ids and edge_ids as keys and node_data and edge_data as values
def set_up_dictionary_for_df(edge_dictionary, edge_ids):
    
    ## Set up lists and keys for final dictionary
    id = []
    from_node_id = []
    to_node_id = []
    length = []
    slope = []
    type = []
    type_max_speed = []
    set_max_speed = []
    # recommend_speed = []
    mean_speed = []
    daily_year = []
    daily_july = []
    daily_trucks = []
    daily_10_axle = [] 
    fuel_station = []
    max_axle_load = []
    max_height = []
    max_length = []
    max_weight = []


    complete_dict = { 'id' : None, 'from_node_id' : None, 'to_node_id': None, 'length' : None, 'slope' : None, 'type' : None, 
    'type_max_speed' : None, 'set_max_speed' : None, 'recommended_speed' : None, 'mean_speed' : None, 'daily_year' : None, 
    'daily_july' : None, 'daily_trucks' : None, 'daily_10_axle' : None, 'fuel_station' : None, 'max_axle_load' : None,
    'max_height' : None, 'max_length' : None, 'max_weight' : None}

    keys = ['id', 'from_node_id', 'to_node_id', 'length', 'slope', 'type', 'type_max_speed', 'set_max_speed', 'mean_speed', 'daily_year',
    'daily_july', 'daily_trucks', 'daily_10_axle', 'fuel_station',
    'max_axle_load', 'max_height', 'max_length', 'max_weight' ]

    values = [id, from_node_id, to_node_id, length, slope, type, type_max_speed, set_max_speed, mean_speed, daily_year, daily_july,
    daily_trucks, daily_10_axle, fuel_station, max_axle_load, max_height, max_length, max_weight]

    # Populate value-lists with values from dictionaries
    for x in edge_ids:
        id.append(x)
        from_node_id.append(edge_dictionary[x]['from_node_id'])
        to_node_id.append(edge_dictionary[x]['to_node_id'])
        length.append(edge_dictionary[x]['length'])
        slope.append(edge_dictionary[x]['slope'])
        type.append(edge_dictionary[x]['type'])
        type_max_speed.append(edge_dictionary[x]['type_max_speed'])
        set_max_speed.append(edge_dictionary[x]['set_max_speed'])
        # recommend_speed.append(edge_dictionary[x]('recommend_speed'))
        mean_speed.append(edge_dictionary[x]['mean_speed'])
        daily_year.append(edge_dictionary[x]['daily_year'])
        daily_july.append(edge_dictionary[x]['daily_july'])
        daily_trucks.append(edge_dictionary[x]['daily_trucks'])
        daily_10_axle.append(edge_dictionary[x]['daily_10_axle'])
        fuel_station.append(edge_dictionary[x]['fuel_station'])
        max_axle_load.append(edge_dictionary[x]['max_axle_load'])
        max_height.append(edge_dictionary[x]['max_height'])
        max_length.append(edge_dictionary[x]['max_length'])
        max_weight.append(edge_dictionary[x]['max_weight'])

    ## Build final dictionary
    for x in range(len(keys)):
        complete_dict[keys[x]] = values[x]

    return complete_dict

## --------------------- FUNCTION DEFINITIONS TO JSON --------------------- ##



    

### --------------------- MAIN PROGRAM ------------------------ ###

# Open and load JSON file
#f = open('/Users/rasmushenriksen/Desktop/BACHELOR-SOFTWARE/femte_og_sjette/femte_semester/Project/Python/src/Data_set/tnm.json')

class DataProcesser:
    def __init__(self):
        pass
    
    def prepare_data_frame(self, file):
        d = preprocess_tnm(file)

        ## Extracting META data from TNM
        meta_data = d['meta_data']

        vehicle_data = d['vehicle']

        ## Extraxting node and edge data from TNM
        node_data = extract_node_data(d)
        edge_data = extract_edge_data(d)
        edge_from_node_id = get_from_node_ids(d)
        edge_to_node_id = get_to_node_ids(d)

        edge_data = add_from_and_to_node_ids_to_edges(edge_data, edge_from_node_id, edge_to_node_id)

        #  ## Extracting node_ids and edge_ids from TNM
        node_ids = extract_node_ids(d)
        edge_ids = extract_edge_ids(d)

        edges_dict = dict(zip(edge_ids, edge_data))
        nodes_dict = dict(zip(node_ids, node_data))

        complete_dictionary = set_up_dictionary_for_df(edges_dict, edge_ids)

        ## Create pandas Datafram and return the nodes_dictionary as well as the meta_data for later use
        df = pd.DataFrame(complete_dictionary)
        return df, nodes_dict, meta_data, d


    def update_tnm_dictionary(self, tnm, predicted_weights, nodes, meta_data):
        tnm_ready = tnm
        normalized_predicted_weights = DataProcesser._normalize_weights(self, predicted_weights, meta_data)
        for node_id in nodes:
            if tnm_ready['nodes'][str(node_id)]['edges']:
                for edge_key in tnm_ready['nodes'][str(node_id)]['edges']:
                    if tnm_ready['nodes'][str(node_id)]['edges'][edge_key]:
                        if normalized_predicted_weights[str(edge_key)]:
                            new_value = normalized_predicted_weights[str(edge_key)]
                            tnm_ready['nodes'][str(node_id)]['edges'][edge_key]['weight'] = new_value
    
        return tnm_ready

    def _normalize_weights(self, weights, meta):
        normalized_weights = {}
        for key, value in weights.items():
            normalized_weight = value / meta['max_daily_trucks']
            normalized_weights[key] = normalized_weight
        
        return normalized_weights
