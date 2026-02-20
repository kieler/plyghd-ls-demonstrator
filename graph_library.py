from kieler_klighd_types.klighd.SKGraphSchema import *
from rendering_library import addText

def createGraph(uri):
    graph = SKGraph(id=uri,revision=1)
    return graph

def createNode(parent):
    if (parent.children == None):
        parent.children = []
    nodeId = f"{parent.id}$$N{len(parent.children)}"
    if parent.type == "graph":
        nodeId = "$root"
    node = SKNode(id=nodeId)
    parent.children.append(node)
    return node

def createLabel(parent, text):
    if (parent.children == None):
        parent.children = []
    labelId = f"{parent.id}$$L{len(parent.children)}"
    label = SKLabel(id=labelId, text=text)
    parent.children.append(label)
    addText(label, text)
    return label

# Create an edge from source to target inside the parent.
def createEdge(parent, source, target):
    # TODO: the semantics of the ID might require it to be the index in relation to all edges, not also the nodes. Same in node position if the node contains edges.
    edgeId = f"{source.id}$$E{len(parent.children)}"
    edge = SKEdge(id=edgeId, sourceId=source.id, targetId=target.id)
    parent.children.append(edge)
    return edge

def createPort(parent):
    if (parent.children == None):
        parent.children = []
    portId = f"{parent.id}$$P{len(parent.children)}"
    port = SKPort(id=portId)
    parent.children.append(port)
    port.size = Size.parse_obj({'width': 5.0, 'height': 5.0})
    return port

def addProperty(element, key, value):
    if (element.properties == None):
        element.properties = {}
    element.properties[key] = value