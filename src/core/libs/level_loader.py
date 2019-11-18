import json


fichier = open("file.json",'r')
test = json.load(fichier)
print(test)
