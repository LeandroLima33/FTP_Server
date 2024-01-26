from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("username", "password", "E:\Curso.Ruby.on.Rails.6", perm="elradfmwMT")


handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("192.168.0.243", 2121), handler)
server.serve_forever()