from klighd_types.klighd.SKGraphSchema import *
def addRectangle(element):
    rectangle = KRectangle()
    if (element.data == None):
        element.data = []
    element.data.append(rectangle)
    # hardcode ID for now. TODO: needs to be hierarchical once we have real hiearchical renderings.
    setId(rectangle, "R0")
    return rectangle

def addPolyline(element):
    polyline = KPolyline()
    if (element.data == None):
        element.data = []
    element.data.append(polyline)
    setId(polyline, "R0")
    return polyline

def addText(element, theText):
    text = KText()
    text.text = theText
    if (element.data == None):
        element.data = []
    element.data.append(text)
    setId(text, "R0")
    return text

def addAction(element, action):
    if (element.actions == None):
        element.actions = []
    element.actions.append(action)


def setId(element, id):
    addProperty(element, "klighd.lsp.rendering.id", id)

def addProperty(element, key, value):
    if (element.properties == None):
        element.properties = {}
    element.properties[key] = value