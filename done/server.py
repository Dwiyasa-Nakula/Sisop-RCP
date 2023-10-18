import os
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

def upload_file(file_name, file_data):
    try:
        with open(file_name, 'wb') as f:
            f.write(file_data.data)
        return "File uploaded successfully on host machine."
    except Exception as e:
        return str(e)

def download_file(file_name):
    try:
        with open(file_name, 'rb') as f:
            file_data = f.read()
        return {"filename": file_name, "data": xmlrpc.client.Binary(file_data)}
    except Exception as e:
        return str(e)

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(('0.0.0.0', 8000), requestHandler=RequestHandler)

server.register_function(upload_file, 'upload')
server.register_function(download_file, 'download')

print("Server on host machine is ready to accept RPC requests...")
server.serve_forever()