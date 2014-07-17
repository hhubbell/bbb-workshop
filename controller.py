# David Leach
# Harrison Hubbell
# An HTTP controller for the BBB Workshop

import SimpleHTTPServer
import SocketServer


class TCPHandler(SocketServer.BaseRequestHandler):
    
    def handle(self):
        self.data = self.request.recv(1024).strip()
        
        print "{} wrote:".format(self.client_address[0])
        print self.data

        self.request.sendall(self.data.upper()) 


if __name__ == "__main__":
    HOST = ""
    PORT = 8888

    #handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd   = SocketServer.TCPServer((HOST, PORT), TCPHandler)

    httpd.serve_forever()
