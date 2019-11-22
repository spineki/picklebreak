from os import path, mkdir
from shutil import rmtree, copyfile
from http import server
import hashlib
from random import choice, random, shuffle

from time import time_ns

from threading import Thread

WEBTREE = {}
F = lambda : int(random() * random() * time_ns()/10000) % 0x100

class HTTPRequestHandler (server.SimpleHTTPRequestHandler):
    
    def do_GET (self):
        data = self.path[1:].split("/")
        
        if data == [""]:
            self.send_response(200)
            self.end_headers()
            a = list(WEBTREE.keys())
            shuffle(a)
            self.wfile.write(bytes("\n".join(a), encoding = "UTF-8"))
        else:
            if data[0] not in WEBTREE:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(bytes("404: Page not found", encoding = "UTF-8"))
            elif len(data) == 1:
                self.send_response(200)
                self.end_headers()
                a = list(WEBTREE[data[0]].keys())
                shuffle(a)
                self.wfile.write(bytes("\n".join(a), encoding = "UTF-8"))
            else:
                if data[1] not in WEBTREE[data[0]]:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(bytes("404: Page not found", encoding = "UTF-8"))
                elif len(data) == 2:
                    self.send_response(200)
                    self.end_headers()
                    a = list(WEBTREE[data[0]][data[1]].keys())
                    shuffle(a)
                    self.wfile.write(bytes("\n".join(a), encoding = "UTF-8"))
                else:
                    if data[2] not in WEBTREE[data[0]][data[1]]:
                        self.send_response(404)
                        self.end_headers()
                        self.wfile.write(bytes("404: Page not found", encoding = "UTF-8"))
                    elif len(data) == 3:
                        self.send_response(200)
                        self.end_headers()
                        a = list(WEBTREE[data[0]][data[1]][data[2]].keys())
                        shuffle(a)
                        self.wfile.write(bytes("\n".join(a), encoding = "UTF-8"))
                    else:
                        if data[3] not in WEBTREE[data[0]][data[1]][data[2]]:
                            self.send_response(404)
                            self.end_headers()
                            self.wfile.write(bytes("404: Page not found", encoding = "UTF-8"))
                        elif len(data) == 4:
                            self.send_response(200)
                            self.end_headers()
                            self.wfile.write(bytes(WEBTREE[data[0]][data[1]][data[2]][data[3]], encoding = "UTF-8"))
                        else:
                            self.send_response(404)
                            self.end_headers()
                            self.wfile.write(bytes("404: Page not found", encoding = "UTF-8"))     

class Server (Thread):
    
    def __init__ (self, serv):
        super().__init__ (daemon = True)
        self.serv = serv
    
    def run (self):
        self.serv.serve_forever()
    
    def exit (self):
        self.serv.shutdown()
        self.serv.server_close()

def gen (key, hints_data, scripts):
    global WEBTREE
    
    new_s = scripts.copy()
    
    if path.isdir("./loaded"):
        rmtree("./loaded")
    
    mkdir("./loaded")
    
    copyfile("./src/res/images/html1.jpg", hints_data[1])
    
    server_address = ("localhost", 8000)
    serv = server.HTTPServer(server_address, HTTPRequestHandler)
    
    new_s[1] = new_s[1].format(*server_address)
    new_s[:-1] = ["\n".join(new_s[:-1])]
    
    for i in range(4):
        st = hashlib.new("sha256")
        st.update(bytes([F(), F()]))
        r = st.hexdigest()[:16]
        WEBTREE[r] = {}
        for j in range(4):
            st = hashlib.new("sha256")
            st.update(bytes([F(), F()]))
            s = st.hexdigest()[:16]
            WEBTREE[r][s] = {}
            for k in range(4):
                st = hashlib.new("sha256")
                st.update(bytes([F(), F()]))
                t = st.hexdigest()[:16]
                WEBTREE[r][s][t] = {}
                for l in range(4):
                    st = hashlib.new("sha256")
                    st.update(bytes([F(), F()]))
                    u = st.hexdigest()[:16]
                    WEBTREE[r][s][t][u] = "Wrong leaf"
    
    key_split = [key[16 * i: 16 * i + 16] for i in range(4)]
    
    a = choice(list(WEBTREE.keys()))
    WEBTREE[key_split[0]] = WEBTREE[a].copy()
    del WEBTREE[a]
    
    a = choice(list(WEBTREE[key_split[0]].keys()))
    WEBTREE[key_split[0]][key_split[1]] = WEBTREE[key_split[0]][a].copy()
    del WEBTREE[key_split[0]][a]
    
    a = choice(list(WEBTREE[key_split[0]][key_split[1]].keys()))
    WEBTREE[key_split[0]][key_split[1]][key_split[2]] = WEBTREE[key_split[0]][key_split[1]][a].copy()
    del WEBTREE[key_split[0]][key_split[1]][a]
    
    a = choice(list(WEBTREE[key_split[0]][key_split[1]][key_split[2]].keys()))
    WEBTREE[key_split[0]][key_split[1]][key_split[2]][key_split[3]] = "You found it. What are the folders?"
    del WEBTREE[key_split[0]][key_split[1]][key_split[2]][a]
    
    th = Server(serv)
    th.start()

    return hints_data.copy(), new_s, [th]

def close (key, objs):
    objs[0].exit()
    
    global WEBTREE
    WEBTREE = {}