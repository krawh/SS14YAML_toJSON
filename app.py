import requests
import yaml
import json

def getYAML():
    r = requests.get('https://raw.githubusercontent.com/space-wizards/space-station-14/master/Resources/Prototypes/Recipes/Reactions/medicine.yml')
    r.headers['Content-Type']
    content = r.content.decode("utf-8")
    return yaml.safe_load(content)

def convertYAMLtoJSON(yamlContent):
    with open('chemicals.json', 'w') as json_file:
        json.dump(yamlContent, json_file, indent=2)

if "__main__" == __name__:
    convertYAMLtoJSON(getYAML())

