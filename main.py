from http.server import HTTPServer
from server import Server
import os

port = os.getenv("PORT", 1050)
httpd = HTTPServer(("localhost", port), Server)
try:
    httpd.serve_forever()
except:
    pass
httpd.server_close()
