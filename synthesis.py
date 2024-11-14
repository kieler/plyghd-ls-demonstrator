from graph_library import addProperty, createEdge, createLabel, createNode, createGraph
from ls import getOption
from rendering_library import addAction, addPolyline, addRectangle
from synthesis_options import SynthesisOption, SynthesisOptionType




ID = "de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis"

LABELS = SynthesisOption("de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.labels", "Labels", SynthesisOptionType.CHECK, True)


class PlyghdKgraphSynthesis:
    def getDisplayedSynthesisOptions(self):
        return [LABELS]
    
    def transform(self, uri, current_options: dict):
        # TODO: add an action and use it.
        # for now, hard-code a new graph.
        graph = createGraph(uri)

        root = createNode(graph)

        n = createNode(root)
        m = createNode(root)
        o = createNode(root)

        addProperty(n, "org.eclipse.elk.nodeSize.constraints", [2])
        addProperty(n, "org.eclipse.elk.nodeLabels.placement", [1, 4, 6])
        addProperty(m, "org.eclipse.elk.nodeSize.constraints", [2])
        addProperty(m, "org.eclipse.elk.nodeLabels.placement", [1, 4, 6])
        addProperty(o, "org.eclipse.elk.nodeSize.constraints", [2])
        addProperty(o, "org.eclipse.elk.nodeLabels.placement", [1, 4, 6])

        nRect = addRectangle(n)

        # TODO: actions not yet in schema
        addAction(nRect, {
            "actionId": f"{ID}.foo",
            "trigger": 1, # 0 = click, 1 = doubleclick, 2 = single or multiclick, 3-5 same for middle mouse button
            "altPressed": 2, # 0 = don't care, 1 = pressed, 2 = not pressed
            "ctrlCmdPressed": 2,
            "shiftPressed": 2
        })
        mRect = addRectangle(m)
        oRect = addRectangle(o)

        if (getOption(current_options, LABELS)):
            nLabel = createLabel(n, "nnnn")
            mLabel = createLabel(m, "m")
            oLabel = createLabel(o, "o")

        nmEdge = createEdge(root, n, m)
        noEdge = createEdge(root, n, o)
        
        addPolyline(nmEdge)
        addPolyline(noEdge)

        return graph
