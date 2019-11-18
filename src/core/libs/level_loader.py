import json
file = "level.json"
level = "1"

def json_reader(file,level):
    fichier = open(file,'r')
    dic = json.load(fichier)
    print(dic[level])

def json_writer(file,clue=None,level=None,imports=[]):
    fichier = open(file,'r')
    dic = json.load(fichier)
    fichier = open(file,'w')
    if level == None: #Create a new level if level == None
        L = list(dic.keys())
        for i in range(len(L)):
            L[i] = int(L[i])
        maximum = max(L) #Search for maximum to create a new level
        dic[str(maximum)]={"id":str(maximum),"clue":clue,"imports":imports}
    else:
        dic[str(level)]={"id":str(level),"clue":clue,"imports":imports}
    json.dump(file,dic)
        


json_writer(file,clue="new clue")
