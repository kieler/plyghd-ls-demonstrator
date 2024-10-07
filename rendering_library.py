from json_schema.skgraph import *
def addRectangle(element):
    rectangle = KRectangle()
    if (element.data == None):
        element.data = []
    element.data.append(rectangle)
    return rectangle

def addPolyline(element):
    polyline = KPolyline()
    if (element.data == None):
        element.data = []
    element.data.append(polyline)
    return polyline

def addText(element, theText):
    text = KText()
    text.text = theText
    if (element.data == None):
        element.data = []
    element.data.append(text)
    return text