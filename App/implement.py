import json;

def write_to_json_file(fileName, data):
    with open(fileName, 'w') as fp:
        json.dump(data, fp, indent=4)

def read_from_json_file(fileName):
    with open(fileName, 'r') as fp:
        data = json.load(fp)
    return data
