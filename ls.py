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
from synthesis_options import SynthesisOption


class KlighdLanguageServer(LanguageServer):
    CMD_SET_PREFERENCES = "keith/preferences/setPreferences"
    CMD_ACCEPT = "diagram/accept"
    CMD_SET_SYNTHESIS_OPTIONS = "keith/diagramOptions/setSynthesisOptions"

    def __init__(self, *args):
        super().__init__(*args)


klighd_server = KlighdLanguageServer("klighd-ls-example", "v0.1")

current_options = {}


def getOption(current_options: dict, option: SynthesisOption):
    if (option.id in current_options):
        return current_options[option.id]
    else:
        return option.initialValue


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
        function = options[args[0].action.kind]
    except:
        print("action kind not supported yet: " + args[0].action.kind)
        return
    function(args[0].action)

@klighd_server.feature(KlighdLanguageServer.CMD_SET_SYNTHESIS_OPTIONS)
def set_synthesis_options(ls: KlighdLanguageServer, params: dict):
    print(params)
    # store the current synthesis options.
    for option in params.synthesisOptions:
        current_options[option.id] = option.currentValue

    doRequestModel(params.uri)
    

def requestModel(action):
    print(action)
    doRequestModel(action.options.sourceUri)

model_uri = ""
def doRequestModel(sourceUri):
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
    global model_uri
    model_uri = sourceUri

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
    model = synthesis_instance.transform(model_uri, current_options) # TODO: should load the model.
    print("sending requestBounds")
    klighd_server.send_notification(KlighdLanguageServer.CMD_ACCEPT, {"clientId":"sprotty","action":{"kind":"requestBounds","newRoot": model}})


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
    global model_uri

    synthesis_options_json = list(map(lambda option: {
        "synthesisOption": {
            "id": option.id,
            "name": option.name,
            "type": option.type,
            "sourceHash": option.id, # TODO: should be some unique hash value, might not be needed with better API.
            "initialValue": option.initialValue
        },
        "currentValue": getOption(current_options, option) # TODO: should be stored and the current value be sent here instead.
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