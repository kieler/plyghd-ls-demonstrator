# #  KIELER - Kiel Integrated Environment for Layout Eclipse RichClient
#  
#  http://rtsys.informatik.uni-kiel.de/kieler
#  
#  Copyright 2024 by
#  + Kiel University
#    + Department of Computer Science
#      + Real-Time and Embedded Systems Group
#  
#  This program and the accompanying materials are made available under the
#  terms of the MIT License which is available at
#  https://opensource.org/license/mit.
#  #  SPDX-License-Identifier: MIT

import argparse

from lsprotocol import types as lsp

from pygls.server import LanguageServer


class KlighdLanguageServer(LanguageServer):
    CMD_SET_PREFERENCES = "keith/preferences/setPreferences"
    CMD_ACCEPT = "diagram/accept"

    def __init__(self, *args):
        super().__init__(*args)


klighd_server = KlighdLanguageServer("klighd-ls-example", "v0.1")


@klighd_server.feature(lsp.INITIALIZE)
def initialize(params: lsp.InitializeParams):
    print(params.initialization_options)


@klighd_server.feature(KlighdLanguageServer.CMD_SET_PREFERENCES)
def set_preferences(ls: KlighdLanguageServer, preferences: dict):
    print(preferences)


@klighd_server.feature(KlighdLanguageServer.CMD_ACCEPT)
def accept(ls: KlighdLanguageServer, *args):
    print(args)

    print("sending setSynthesis")
    ls.send_notification(KlighdLanguageServer.CMD_ACCEPT, {"clientId":"sprotty","action":{"kind":"setSyntheses","syntheses":[{"id":"de.cau.cs.kieler.graphs.klighd.syntheses.KGraphDiagramSynthesis","displayName":"KGraphDiagramSynthesis"},{"id":"de.cau.cs.kieler.klighd.ide.syntheses.EObjectFallbackSynthesis","displayName":"EObjectFallbackSynthesis"},{"id":"de.cau.cs.kieler.kicool.ui.klighd.syntheses.XtextSerializationSynthesis","displayName":"XtextSerializationSynthesis"}]}})

    print("sending updateOptions")
    ls.send_notification(KlighdLanguageServer.CMD_ACCEPT, {"clientId":"sprotty","action":{"kind":"updateOptions","valuedSynthesisOptions":[{"synthesisOption":{"id":"de.cau.cs.kieler.graphs.klighd.syntheses.KGraphDiagramSynthesis.CHOICE227839009","name":"Default Values","type":1,"sourceHash":1506798321,"values":["As in Model","On","Off"],"initialValue":"As in Model"},"currentValue":"As in Model"},{"synthesisOption":{"id":"de.cau.cs.kieler.graphs.klighd.syntheses.KGraphDiagramSynthesis.CHECK-1675366116","name":"Suppress Edge Adjustement","type":0,"sourceHash":1197289400,"initialValue":True},"currentValue":True},{"synthesisOption":{"id":"de.cau.cs.kieler.graphs.klighd.syntheses.AbstractStyledDiagramSynthesis.CHOICE80227729","name":"Style","type":1,"sourceHash":909454519,"values":["Boring","Stylish","Hello Kitty","Patrick"],"initialValue":"Stylish"},"currentValue":"Stylish"},{"synthesisOption":{"id":"de.cau.cs.kieler.graphs.klighd.syntheses.AbstractStyledDiagramSynthesis.CHOICE577556810","name":"Label Shortening Strategy","type":1,"sourceHash":128256047,"values":["No Labels","Truncate","Soft Word Wrapping","Full Labels"],"initialValue":"Full Labels"},"currentValue":"Full Labels"}],"layoutOptions":[],"actions":[],"modelUri":"file:///home/nre/git/models/graphs/small.kgt"}})

    print("sending requestBounds")
    ls.send_notification(KlighdLanguageServer.CMD_ACCEPT, {"clientId":"sprotty","action":{"kind":"requestBounds","newRoot":{"properties":{},"revision":1,"type":"graph","id":"file:///home/nre/git/models/graphs/small.kgt","children":[{"data":[{"renderings":[{"junctionPointRendering":{"type":"KEllipseImpl","styles":[{"type":"KBackgroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False}],"properties":{}},"type":"KPolylineImpl","children":[{"type":"KPolygonImpl","points":[{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KTopPositionImpl","absolute":0.0,"relative":0.0}},{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.4},"y":{"type":"KTopPositionImpl","absolute":0.0,"relative":0.5}},{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KBottomPositionImpl","absolute":0.0,"relative":0.0}},{"x":{"type":"KRightPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KBottomPositionImpl","absolute":0.0,"relative":0.5}}],"children":[],"styles":[{"lineWidth":1.0,"type":"KLineWidthImpl","propagateToChildren":False,"selection":False},{"type":"KForegroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False},{"type":"KBackgroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False},{"lineJoin":1,"miterLimit":10.0,"type":"KLineJoinImpl","propagateToChildren":False,"selection":False}],"properties":{}}],"styles":[{"lineCap":0,"type":"KLineCapImpl","propagateToChildren":False,"selection":False}],"id":"DefaultEdgeRendering","properties":{}},{"junctionPointRendering":{"type":"KEllipseImpl","styles":[{"type":"KBackgroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False}],"properties":{}},"type":"KPolylineImpl","children":[],"id":"DefaultNoArrowPolylineEdgeRendering","properties":{}},{"type":"KSplineImpl","children":[{"type":"KPolygonImpl","points":[{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KTopPositionImpl","absolute":0.0,"relative":0.0}},{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.4},"y":{"type":"KTopPositionImpl","absolute":0.0,"relative":0.5}},{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KBottomPositionImpl","absolute":0.0,"relative":0.0}},{"x":{"type":"KRightPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KBottomPositionImpl","absolute":0.0,"relative":0.5}}],"children":[],"styles":[{"lineWidth":1.0,"type":"KLineWidthImpl","propagateToChildren":False,"selection":False},{"type":"KForegroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False},{"type":"KBackgroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False},{"lineJoin":1,"miterLimit":10.0,"type":"KLineJoinImpl","propagateToChildren":False,"selection":False}],"properties":{}}],"styles":[{"lineCap":0,"type":"KLineCapImpl","propagateToChildren":False,"selection":False}],"id":"SplineEdgeRendering","properties":{}},{"type":"KSplineImpl","children":[],"id":"NoArrowSplineEdgeRendering","properties":{}},{"cornerWidth":5.0,"cornerHeight":5.0,"type":"KRoundedRectangleImpl","children":[],"styles":[{"type":"KBackgroundImpl","color":{"red":235,"green":246,"blue":250},"alpha":255,"targetColor":{"red":196,"green":227,"blue":243},"targetAlpha":255,"gradientAngle":90.0,"propagateToChildren":False,"selection":False}],"id":"DefaultNodeRendering","properties":{}}],"type":"KRenderingLibraryImpl"}],"properties":{},"direction":0,"selected":False,"hoverFeedback":False,"size":{"width":0.0,"height":0.0},"type":"node","id":"$root","children":[{"data":[{"type":"KRectangleImpl","children":[],"properties":{}}],"properties":{"org.eclipse.elk.nodeSize.constraints":[2],"org.eclipse.elk.nodeLabels.placement":[1,4,6]},"direction":0,"selected":False,"hoverFeedback":False,"size":{"width":0.0,"height":0.0},"type":"node","id":"$root$Nn","children":[{"data":[{"cursorSelectable":False,"editable":False,"type":"KTextImpl","styles":[{"size":8,"scaleWithZoom":False,"type":"KFontSizeImpl","propagateToChildren":False,"selection":False}],"actions":[{"actionId":"de.cau.cs.kieler.klighd.actions.FocusAndContextAction","trigger":0,"altPressed":0,"ctrlCmdPressed":0,"shiftPressed":0}],"properties":{}}],"properties":{},"text":"nnnn","selected":False,"type":"label","id":"$root$Nn$$L0","children":[]}]},{"data":[{"type":"KRectangleImpl","children":[],"properties":{}}],"properties":{"org.eclipse.elk.nodeSize.constraints":[2],"org.eclipse.elk.nodeLabels.placement":[1,4,6]},"direction":0,"selected":False,"hoverFeedback":False,"size":{"width":0.0,"height":0.0},"type":"node","id":"$root$Nm","children":[{"data":[{"cursorSelectable":False,"editable":False,"type":"KTextImpl","styles":[{"size":8,"scaleWithZoom":False,"type":"KFontSizeImpl","propagateToChildren":False,"selection":False}],"actions":[{"actionId":"de.cau.cs.kieler.klighd.actions.FocusAndContextAction","trigger":0,"altPressed":0,"ctrlCmdPressed":0,"shiftPressed":0}],"properties":{}}],"properties":{},"text":"m","selected":False,"type":"label","id":"$root$Nm$$L0","children":[]}]},{"data":[{"type":"KRectangleImpl","children":[],"properties":{}}],"properties":{"org.eclipse.elk.nodeSize.constraints":[2],"org.eclipse.elk.nodeLabels.placement":[1,4,6]},"direction":0,"selected":False,"hoverFeedback":False,"size":{"width":0.0,"height":0.0},"type":"node","id":"$root$No","children":[{"data":[{"cursorSelectable":False,"editable":False,"type":"KTextImpl","styles":[{"size":8,"scaleWithZoom":False,"type":"KFontSizeImpl","propagateToChildren":False,"selection":False}],"actions":[{"actionId":"de.cau.cs.kieler.klighd.actions.FocusAndContextAction","trigger":0,"altPressed":0,"ctrlCmdPressed":0,"shiftPressed":0}],"properties":{}}],"properties":{},"text":"o","selected":False,"type":"label","id":"$root$No$$L0","children":[]}]},{"data":[{"type":"KPolylineImpl","children":[],"properties":{}}],"junctionPoints":[],"properties":{},"sourceId":"$root$Nn","targetId":"$root$Nm","selected":False,"hoverFeedback":False,"type":"edge","id":"$root$Nn$$E0","children":[]},{"data":[{"type":"KPolylineImpl","children":[],"properties":{}}],"junctionPoints":[],"properties":{},"sourceId":"$root$Nn","targetId":"$root$No","selected":False,"hoverFeedback":False,"type":"edge","id":"$root$Nn$$E1","children":[]}]}]}}})


def add_arguments(parser):
    parser.description = "simple KLighD diagram server example"

    parser.add_argument("--host", default="127.0.0.1", help="Bind to this address")
    parser.add_argument("--port", type=int, default=5007, help="Bind to this port")


def main():
    parser = argparse.ArgumentParser()
    add_arguments(parser)
    args = parser.parse_args()

    klighd_server.start_tcp(args.host, args.port)


if __name__ == "__main__":
    main()