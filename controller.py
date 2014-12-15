# David Leach
# Harrison Hubbell
# An HTTP controller for the BBB Workshop

from multiprocessing import Process
import BaseHTTPServer
import json
import time

CLIENTS = {}

class TCPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def add_client(self, addr):
        CLIENTS[addr] = {}

    def do_GET(self):
        if self.client_address[0] not in CLIENTS.keys():
            self.add_client(self.client_address[0])
            self.send_response(201)

    def do_POST(self):
        if self.client_address[0] not in CLIENTS.keys():
            self.add_client(self.client_address[0])
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
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'players': CLIENTS}))

def client_serve(host, port):
    httpd = BaseHTTPServer.HTTPServer((host, port), TCPHandler)
    httpd.serve_forever()

def json_serve(host, port):
    json_httpd = BaseHTTPServer.HTTPServer((host, port), JSONHandler)
    json_httpd.serve_forever()

if __name__ == "__main__":
    HOST = ''
    HTTP_PORT = 80
    JSON_PORT = 888

    client_server = Process(target=client_serve, args=(HOST, HTTP_PORT))
    client_server.start()

    json_server = Process(target=json_serve, args=(HOST, JSON_PORT))
    json_server.start()
