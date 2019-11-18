
import json
file = "level.json"


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
        print(L)
        maximum = max(L) #Search for maximum to create a new level
        print(maximum)
        dic[str(maximum+1)]={"id":str(maximum+1),"clue":clue,"imports":imports}
    else:
        dic[str(level)]={"id":str(level),"clue":clue,"imports":imports}
    json.dump(dic,fichier,indent=4)

def json_del_level(file,level):
    fichier = open(file,'r')
    dic = json.load(fichier)
    fichier = open(file,'w')
    del dic[str(level)]
    json.dump(dic,fichier,indent=4)

