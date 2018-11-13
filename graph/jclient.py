# minimalistic client example from
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
import node
import json
import localDemo

# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()
# Execute in server:
root = localDemo.createTree()
root.show()
jStr = localDemo.jRequest(root)
#increases tree from the server
jStr = server.incTree(jStr)
#build new tree
root = localDemo.buildFromJson(jStr)
print("printing tree returned from server")
root.show()

rpc.close() # Closes the socket 's' also
