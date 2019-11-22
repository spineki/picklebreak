from os import path, mkdir
from shutil import rmtree, copyfile
from http import server

from threading import Thread

LOADED_KEY = ""

class HTTPRequestHandler (server.SimpleHTTPRequestHandler):
    
    def do_GET (self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(LOADED_KEY, encoding = "UTF-8"))

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
    global LOADED_KEY
    LOADED_KEY = key
    
    new_s = scripts.copy()
    
    if path.isdir("./loaded"):
        rmtree("./loaded")
    
    mkdir("./loaded")
    
    copyfile("./src/res/images/html0.jpg", hints_data[1])
    
    server_address = ("localhost", 8000)
    serv = server.HTTPServer(server_address, HTTPRequestHandler)
    
    new_s[1] = new_s[1].format(*server_address)
    new_s[:-1] = ["\n".join(new_s[:-1])]
    
    th = Server(serv)
    th.start()

    return hints_data.copy(), new_s, [th]

def close (key, objs):
    objs[0].exit()