from json_schema.kgraph import *

def createNode(parent = None):
    node = KNode()
    if not parent:
        node.id = "$root"
    if parent:
        if (parent.children == None):
            parent.children = []
        parent.children.append(node)
        node.id = f"{parent.id}$$N{len(parent.children)}"
    return node

def createLabel(parent, text):
    label = KLabel()
    label.text = text
    if (parent.children == None):
        parent.children = []
    parent.children.append(label)
    label.id = f"{parent.id}$$L{len(parent.children)}"
    return label

def createEdge(source, target):
    edge = KEdge()
    # TODO: there should be no source and target / outgoing and incoming edges, but only sourceId and targetId, see SKGraph
    edge.sourceId = source.id
    edge.targetId = target.id
    edge.id = f"{source.id}$$E{len(source.outgoing_edges)}"
    return edge

def addProperty(element, key, value):
    if (element.properties == None):
        element.properties = {}
    element.properties[key] = value