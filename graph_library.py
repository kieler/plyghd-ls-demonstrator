from json_schema.skgraph import *
from rendering_library import addText

def createGraph(uri):
    graph = SKGraph()
    graph.id = uri
    graph.revision = 1
    return graph

def createNode(parent):
    node = SKNode()
    if (parent.children == None):
        parent.children = []
    parent.children.append(node)
    node.id = f"{parent.id}$$N{len(parent.children) - 1}"
    if parent.type == "graph":
        node.id = "$root"
    return node

def createLabel(parent, text):
    label = SKLabel()
    label.text = text
    if (parent.children == None):
        parent.children = []
    parent.children.append(label)
    label.id = f"{parent.id}$$L{len(parent.children) - 1}"

    addText(label, text)
    return label

# Create an edge from source to target inside the parent.
def createEdge(parent, source, target):
    edge = SKEdge()
    edge.sourceId = source.id
    edge.targetId = target.id
    # TODO: the semantics of the ID might require it to be the index in relation to all edges, not also the nodes. Same in node position if the node contains edges.
    edge.id = f"{source.id}$$E{len(parent.children) - 1}"
    parent.children.append(edge)

    return edge

def addProperty(element, key, value):
    if (element.properties == None):
        element.properties = {}
    element.properties[key] = value