from node import *
import json

def createTree():
    leaf1 = node("leaf1")
    leaf2 = node("leaf2")

    root = node("root", [leaf1, leaf1, leaf2])
    return root

def jRequest(root):
    return doRequest(root)

def buildFromJson(jStr):
    myDict = json.loads(jStr)
    myKeys = list(myDict.keys())
    # Create Nodes
    nodes = {}
    for i in range(len(myDict)):
        nodes[myKeys[i]] = node(myKeys[i])

    # Set children
    for i in myKeys:
        nodes[i].val = myDict[i]["val"]

        auxKeys = myDict[i]["children"].values()
        nodes[i].children = []
        for auxChild in auxKeys:
            nodes[i].children.append(nodes[auxChild])
    return nodes["root"]
