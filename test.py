
import json

searchfor = []
with open('./mini.json', 'r') as f:
    for x in f:
        print(json.loads(x))