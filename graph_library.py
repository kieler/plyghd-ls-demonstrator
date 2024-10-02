from json_schema.kgraph import *

def createNode(parent):
    node = KNode()
    if parent:
        parent.children.append(node)
        node.parent = parent
    return node

def createLabel(parent, text):
    label = KLabel(text)
    parent.labels.append(label)
    label.parent = parent
    return label

def createEdge(source, target):
    edge = KEdge()
    edge.source = source
    edge.target = target
    source.outgoing_edges.append(edge)
    target.incoming_edges.append(edge)
    return edge

def addProperty(element, key, value):
    element.properties[key] = value