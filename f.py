import os, json
import pandas as pd

path_to_json = 'C:\Users\SESA454602\Desktop\availibility'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
#print json_files

for js in json_files:
    with open(os.path.join(path_to_json, js)) as json_file:
        print json.load(json_file.read())