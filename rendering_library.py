from json_schema.kgraph import *
def addRectangle(element):
    rectangle = KRectangle()
    element.data.append(rectangle)
    return rectangle

def addPolyline(element):
    polyline = KPolyline()
    element.data.append(polyline)
    return polyline