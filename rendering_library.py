from json_schema.skgraph import *
def addRectangle(element):
    rectangle = KRectangle()
    if (element.data == None):
        element.data = []
    element.data.append(rectangle)
    # hardcode ID for now. TODO: needs to be hierarchical once we have real hiearchical renderings.
    # TODO: id needs to be in schema as well.
    rectangle.id = "R0"
    return rectangle

def addPolyline(element):
    polyline = KPolyline()
    if (element.data == None):
        element.data = []
    element.data.append(polyline)
    polyline.id = "R0"
    return polyline

def addText(element, theText):
    text = KText()
    text.text = theText
    if (element.data == None):
        element.data = []
    element.data.append(text)
    text.id = "R0"
    return text

def addAction(element, action):
    if (element.actions == None):
        element.actions = []
    element.actions.append(action)