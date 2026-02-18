
import json

def load_test_data(file_path):
    with open(file_path) as json_file:
        return json.load(json_file)

