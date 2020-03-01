from http.server import HTTPServer
from server import Server
import os

port = int(os.environ.get('PORT', 17995))  # as per OP comments default is 17995

httpd = HTTPServer(('', port), Server)

try:
    httpd.serve_forever()
except:
    pass
httpd.server_close()
