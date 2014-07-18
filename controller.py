# David Leach
# Harrison Hubbell
# An HTTP controller for the BBB Workshop

import BaseHTTPServer
import json
import time
from threading import Thread

HOST = ""
CLIENT_PORT = 8888
JSON_PORT = 9999
CLIENTS = {}

class ClientTCPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def add_client(self):
        CLIENTS[self.client_address[0]] = {}

    def do_POST(self):
        print "ACK"
        self.data = self.headers.items()
        print self.data

        if self.client_address[0] not in CLIENTS.keys():
            self.add_client()
            self.send_response(201)
        #else:
            # Parse data
            # Update CLIENTS with temp
            # send 200


class JSONHandler(BaseHTTPServer.BaseHTTPRequestHandler):    
    def do_POST(self):
        self.data = self.headers.items()
        self.send_JSON()
        
    def send_JSON(self):
        player_json = json.dumps({'players':CLIENTS})
        self.send(player_json)

def client_serve():
    httpd = BaseHTTPServer.HTTPServer((HOST, CLIENT_PORT), ClientTCPHandler)
    httpd.serve_forever()

def json_serve():
    json_httpd = BaseHTTPServer.HTTPServer((HOST, JSON_PORT), JSONHandler)
    json_httpd.serve_forever()

if __name__ == "__main__":
    client_thread = Thread(target=client_serve)
    client_thread.daemon = True
    client_thread.start()

    json_thread = Thread(target=json_serve)
    json_thread.daemon = True
    json_thread.start()

    while True:
        time.sleep(1)
