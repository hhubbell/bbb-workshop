# David Leach
# Harrison Hubbell
# An HTTP controller for the BBB Workshop

import BaseHTTPServer
import time

CLIENT_IDS = {}

class TCPHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    
    def ack(self):
        return 0

    def add_client(self):
        CLIENT_IDS[self.client_address[0]] = {}

    def do_GET(self):
        print "ACK"
        self.data = self.headers.items()

        if self.client_address[0] not in CLIENT_IDS.keys():
            self.add_client()
            self.ack()

        print "{} wrote:".format(self.client_address[0])
        print self.data

        self.send_response(201)




if __name__ == "__main__":
    HOST = ""
    PORT = 8888

    httpd   = BaseHTTPServer.HTTPServer((HOST, PORT), TCPHandler)

    httpd.serve_forever()
