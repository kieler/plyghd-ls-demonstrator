from json_schema.kgraph import *
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