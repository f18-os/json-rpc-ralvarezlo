import json
class node:
    def __init__(self, name, children = []):
        self.name = name
        self.children = children
        self.val = 0
    def show(self, level=0):
        print("%s%s val=%d:" % (level*"  ", self.name, self.val))
        for c in self.children:
            c.show(level + 1)

def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

def outDict(graph, myDict = {}):
    childArr = {}
    for i in range(len(graph.children)):
        childArr[i] = graph.children[i].name
        myDict = outDict(graph.children[i], myDict)

    auxArr = {"val":graph.val, "children":childArr}
    myDict.update({graph.name:auxArr})
    return myDict


def doRequest(graph):
    myDict = outDict(graph)

    file = open("json.request", "w")
    jString = json.dumps(myDict)
    file.write(jString)
    return jString
