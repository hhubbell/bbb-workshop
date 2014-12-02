# David Leach
# Harrison Hubbell
# An HTTP controller for the BBB Workshop

from multiprocessing import Process
import BaseHTTPServer
import json
import time

HOST = ''
CLIENT_PORT = 8888
JSON_PORT = 9999
CLIENTS = {}

class ClientHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def add_client(self):
        CLIENTS[self.client_address[0]] = {}

    def do_GET(self):
        if self.client_address[0] not in CLIENTS.keys():
            self.add_client()
            self.send_response(201)

    def do_POST(self):
        if self.client_address[0] not in CLIENTS.keys():
            self.add_client()
            self.send_response(201)
        #else:
            # Parse data
            # Update CLIENTS with temp
            # send 200


class JSONHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        self.data = self.headers.items()
        self.send_JSON()

    def do_POST(self):
        self.data = self.headers.items()
        self.send_JSON()
        
    def send_JSON(self):
        player_json = json.dumps({'players': CLIENTS})
        self.wfile.write(player_json)

def client_serve(host, port):
    httpd = BaseHTTPServer.HTTPServer((host, port), ClientTCPHandler)
    httpd.serve_forever()

def json_serve(host, port):
    json_httpd = BaseHTTPServer.HTTPServer((host, port), JSONHandler)
    json_httpd.serve_forever()

if __name__ == "__main__":
    client_server = Process(target=client_serve, args=(HOST, CLIENT_PORT))
    client_server.start()

    json_server = Process(target=json_serve, args=(HOST, JSON_PORT))
    json_server.start()
