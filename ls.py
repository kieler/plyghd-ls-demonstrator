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

import synthesis as plyghd_synthesis
import PlyghdOptions


class KlighdLanguageServer(LanguageServer):
    CMD_SET_PREFERENCES = "keith/preferences/setPreferences"
    CMD_ACCEPT = "diagram/accept"

    def __init__(self, *args):
        super().__init__(*args)


klighd_server = KlighdLanguageServer("klighd-ls-example", "v0.1")


@klighd_server.feature(lsp.INITIALIZE)
def initialize(params: lsp.InitializeParams):
    init_synthesis_options = params.initialization_options["clientDiagramOptions"]["synthesis"]
    for key in PlyghdOptions.plyghd_options:
        try:
            PlyghdOptions.plyghd_options[key] = init_synthesis_options[key]
        except:
            continue


@klighd_server.feature(KlighdLanguageServer.CMD_SET_PREFERENCES)
def set_preferences(ls: KlighdLanguageServer, preferences: dict):
    # we don't care about the preferences set currently.
    # We expect a message such as this one:
    # {
    #     "jsonrpc": "2.0",
    #     "method": "keith/preferences/setPreferences",
    #     "params": {
    #         "diagram.shouldSelectDiagram": false,
    #         "diagram.shouldSelectText": true,
    #         "diagram.incrementalDiagramGenerator": false
    #     }
    # }
    # TODO: cross-reference and explain what these mean and how these could be handled.
    pass


@klighd_server.feature(KlighdLanguageServer.CMD_ACCEPT)
def accept(ls: KlighdLanguageServer, *args):
    print(args[0])
    options = {"requestModel": requestModel}

    try:
        options[args[0].action.kind](args[0].action)
    except:
        print("action kind not supported yet: " + args[0].action.kind)
    

model_uri = ""
def requestModel(action):
    print(action)
    # we expect to receive an action such as this one:
    # {
    #     "kind": "requestModel",
    #     "options": {
    #         "needsClientLayout": true,
    #         "needsServerLayout": false,
    #         "sourceUri": "file:///home/nre/git/models/graphs/small.kgt",
    #         "diagramType": "keith-diagram"
    #     },
    # "requestId": "client_1"
    # }

    # For now, we just remember the model to be generated.
    model_uri = action.options.sourceUri

    # Find out the model file extension to find the available syntheses.
    file_extension = model_uri.split(".")[-1]
    synthesis_ids = PlyghdOptions.plyghd_syntheses[file_extension]

    # Send a message to the client containing the known syntheses.
    send_syntheses(synthesis_ids)

    # We just use the first one as our synthesis.
    synthesis = synthesis_ids[0]

    known_syntheses = {
        plyghd_synthesis.ID: plyghd_synthesis.PlyghdKgraphSynthesis
    }

    if not synthesis in known_syntheses:
        print("synthesis not known. " + synthesis)
        return

    # Send the synthesis-available options.
    synthesis_instance = known_syntheses[synthesis]()
    send_available_options(synthesis_instance)

    # Finally, generate the kgraph from the model file (hardcoded for now) and send it the client.
    model = synthesis_instance.transform(model_uri) # TODO: should load the model.
    print("sending requestBounds")
    klighd_server.send_notification(KlighdLanguageServer.CMD_ACCEPT, {"clientId":"sprotty","action":{"kind":"requestBounds","newRoot": model}})
    # klighd_server.send_notification(KlighdLanguageServer.CMD_ACCEPT, {"clientId":"sprotty","action":{"kind":"requestBounds","newRoot":{"properties":{},"revision":1,"type":"graph","id":"file:///home/nre/git/models/graphs/small.kgt","children":[{"data":[{"renderings":[{"junctionPointRendering":{"type":"KEllipseImpl","styles":[{"type":"KBackgroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False}],"properties":{}},"type":"KPolylineImpl","children":[{"type":"KPolygonImpl","points":[{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KTopPositionImpl","absolute":0.0,"relative":0.0}},{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.4},"y":{"type":"KTopPositionImpl","absolute":0.0,"relative":0.5}},{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KBottomPositionImpl","absolute":0.0,"relative":0.0}},{"x":{"type":"KRightPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KBottomPositionImpl","absolute":0.0,"relative":0.5}}],"children":[],"styles":[{"lineWidth":1.0,"type":"KLineWidthImpl","propagateToChildren":False,"selection":False},{"type":"KForegroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False},{"type":"KBackgroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False},{"lineJoin":1,"miterLimit":10.0,"type":"KLineJoinImpl","propagateToChildren":False,"selection":False}],"properties":{}}],"styles":[{"lineCap":0,"type":"KLineCapImpl","propagateToChildren":False,"selection":False}],"id":"DefaultEdgeRendering","properties":{}},{"junctionPointRendering":{"type":"KEllipseImpl","styles":[{"type":"KBackgroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False}],"properties":{}},"type":"KPolylineImpl","children":[],"id":"DefaultNoArrowPolylineEdgeRendering","properties":{}},{"type":"KSplineImpl","children":[{"type":"KPolygonImpl","points":[{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KTopPositionImpl","absolute":0.0,"relative":0.0}},{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.4},"y":{"type":"KTopPositionImpl","absolute":0.0,"relative":0.5}},{"x":{"type":"KLeftPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KBottomPositionImpl","absolute":0.0,"relative":0.0}},{"x":{"type":"KRightPositionImpl","absolute":0.0,"relative":0.0},"y":{"type":"KBottomPositionImpl","absolute":0.0,"relative":0.5}}],"children":[],"styles":[{"lineWidth":1.0,"type":"KLineWidthImpl","propagateToChildren":False,"selection":False},{"type":"KForegroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False},{"type":"KBackgroundImpl","color":{"red":0,"green":0,"blue":0},"alpha":255,"targetAlpha":255,"gradientAngle":0.0,"propagateToChildren":False,"selection":False},{"lineJoin":1,"miterLimit":10.0,"type":"KLineJoinImpl","propagateToChildren":False,"selection":False}],"properties":{}}],"styles":[{"lineCap":0,"type":"KLineCapImpl","propagateToChildren":False,"selection":False}],"id":"SplineEdgeRendering","properties":{}},{"type":"KSplineImpl","children":[],"id":"NoArrowSplineEdgeRendering","properties":{}},{"cornerWidth":5.0,"cornerHeight":5.0,"type":"KRoundedRectangleImpl","children":[],"styles":[{"type":"KBackgroundImpl","color":{"red":235,"green":246,"blue":250},"alpha":255,"targetColor":{"red":196,"green":227,"blue":243},"targetAlpha":255,"gradientAngle":90.0,"propagateToChildren":False,"selection":False}],"id":"DefaultNodeRendering","properties":{}}],"type":"KRenderingLibraryImpl"}],"properties":{},"direction":0,"selected":False,"hoverFeedback":False,"size":{"width":0.0,"height":0.0},"type":"node","id":"$root","children":[{"data":[{"type":"KRectangleImpl","children":[],"properties":{}}],"properties":{"org.eclipse.elk.nodeSize.constraints":[2],"org.eclipse.elk.nodeLabels.placement":[1,4,6]},"direction":0,"selected":False,"hoverFeedback":False,"size":{"width":0.0,"height":0.0},"type":"node","id":"$root$Nn","children":[{"data":[{"cursorSelectable":False,"editable":False,"type":"KTextImpl","styles":[{"size":8,"scaleWithZoom":False,"type":"KFontSizeImpl","propagateToChildren":False,"selection":False}],"actions":[{"actionId":"de.cau.cs.kieler.klighd.actions.FocusAndContextAction","trigger":0,"altPressed":0,"ctrlCmdPressed":0,"shiftPressed":0}],"properties":{}}],"properties":{},"text":"nnnn","selected":False,"type":"label","id":"$root$Nn$$L0","children":[]}]},{"data":[{"type":"KRectangleImpl","children":[],"properties":{}}],"properties":{"org.eclipse.elk.nodeSize.constraints":[2],"org.eclipse.elk.nodeLabels.placement":[1,4,6]},"direction":0,"selected":False,"hoverFeedback":False,"size":{"width":0.0,"height":0.0},"type":"node","id":"$root$Nm","children":[{"data":[{"cursorSelectable":False,"editable":False,"type":"KTextImpl","styles":[{"size":8,"scaleWithZoom":False,"type":"KFontSizeImpl","propagateToChildren":False,"selection":False}],"actions":[{"actionId":"de.cau.cs.kieler.klighd.actions.FocusAndContextAction","trigger":0,"altPressed":0,"ctrlCmdPressed":0,"shiftPressed":0}],"properties":{}}],"properties":{},"text":"m","selected":False,"type":"label","id":"$root$Nm$$L0","children":[]}]},{"data":[{"type":"KRectangleImpl","children":[],"properties":{}}],"properties":{"org.eclipse.elk.nodeSize.constraints":[2],"org.eclipse.elk.nodeLabels.placement":[1,4,6]},"direction":0,"selected":False,"hoverFeedback":False,"size":{"width":0.0,"height":0.0},"type":"node","id":"$root$No","children":[{"data":[{"cursorSelectable":False,"editable":False,"type":"KTextImpl","styles":[{"size":8,"scaleWithZoom":False,"type":"KFontSizeImpl","propagateToChildren":False,"selection":False}],"actions":[{"actionId":"de.cau.cs.kieler.klighd.actions.FocusAndContextAction","trigger":0,"altPressed":0,"ctrlCmdPressed":0,"shiftPressed":0}],"properties":{}}],"properties":{},"text":"o","selected":False,"type":"label","id":"$root$No$$L0","children":[]}]},{"data":[{"type":"KPolylineImpl","children":[],"properties":{}}],"junctionPoints":[],"properties":{},"sourceId":"$root$Nn","targetId":"$root$Nm","selected":False,"hoverFeedback":False,"type":"edge","id":"$root$Nn$$E0","children":[]},{"data":[{"type":"KPolylineImpl","children":[],"properties":{}}],"junctionPoints":[],"properties":{},"sourceId":"$root$Nn","targetId":"$root$No","selected":False,"hoverFeedback":False,"type":"edge","id":"$root$Nn$$E1","children":[]}]}]}}})


def send_syntheses(synthesis_ids):
    # Send a message like this one, containing the known syntheses.
    # {
    #   "jsonrpc": "2.0",
    #   "method": "diagram/accept",
    #   "params": {
    #     "clientId": "sprotty",
    #     "action": {
    #       "kind": "setSyntheses",
    #       "syntheses": [
    #         {
    #           "id": "de.cau.cs.kieler.graphs.klighd.syntheses.KGraphDiagramSynthesis",
    #           "displayName": "KGraphDiagramSynthesis"
    #         }
    #       ]
    #     }
    #   }
    # }
    syntheses = list(map(lambda id: {"id": id, "displayName": id.split(".")[-1]}, synthesis_ids))
    print("sending setSynthesis")
    klighd_server.send_notification(KlighdLanguageServer.CMD_ACCEPT, {"clientId":"sprotty","action":{"kind":"setSyntheses","syntheses": syntheses}})

def send_available_options(synthesis):
    # Send a message like this one, containing the options of the chosen synthesis:
    # {
    #   "clientId": "sprotty",
    #   "action": {
    #     "kind": "updateOptions",
    #     "valuedSynthesisOptions": [
    #       {
    #         "synthesisOption": {
    #           "id": "e.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.color",
    #           "name": "Color",
    #           "type": 3,
    #           "sourceHash": 42,
    #           "initialValue": "0x000000"
    #         },
    #         "currentValue": "0x000000"
    #       },
    #       {
    #         "synthesisOption": {
    #           "id": "de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.labels",
    #           "name": "Labels",
    #           "type": 0,
    #           "sourceHash": 43,
    #           "initialValue": true
    #         },
    #         "currentValue": true
    #       }
    #     ],
    #     "layoutOptions": [],
    #     "actions": [],
    #     "modelUri": "file:///home/nre/git/models/graphs/small.kgt"
    #   }
    # }

    synthesis_options_json = list(map(lambda option: {
        "synthesisOption": {
            "id": option.id,
            "name": option.name,
            "type": option.type,
            "sourceHash": option.id, # TODO: should be some unique hash value, might not be needed with better API.
            "initialValue": option.initialValue
        },
        "currentValue": option.initialValue # TODO: should be stored and the current value be sent here instead.
    }, synthesis.getDisplayedSynthesisOptions()))



    print("sending updateOptions")
    klighd_server.send_notification(KlighdLanguageServer.CMD_ACCEPT, {"clientId":"sprotty","action":{"kind":"updateOptions","valuedSynthesisOptions": synthesis_options_json, "layoutOptions":[],"actions":[],"modelUri": model_uri}})


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