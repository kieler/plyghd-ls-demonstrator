from graph_library import addProperty, createEdge, createLabel, createNode
from rendering_library import addPolyline, addRectangle
from synthesis_options import SynthesisOption, SynthesisOptionType




ID = "de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis"

COLOR = SynthesisOption("de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.color", "Color", SynthesisOptionType.TEXT, "0x000000")
LABELS = SynthesisOption("de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.labels", "Labels", SynthesisOptionType.CHECK, True)


class PlyghdKgraphSynthesis:
    def getDisplayedSynthesisOptions(self):
        return [COLOR, LABELS]
    
    def transform(self, graph):
        # for now, hard-code a new graph.

        root = createNode()

        n = createNode(root)
        m = createNode(root)
        o = createNode(root)

        addProperty(n, "nodeSize.constraints", [2])
        addProperty(n, "nodeLabels.placement," [1, 4, 6])
        addProperty(m, "nodeSize.constraints", [2])
        addProperty(m, "nodeLabels.placement," [1, 4, 6])
        addProperty(o, "nodeSize.constraints", [2])
        addProperty(o, "nodeLabels.placement," [1, 4, 6])

        nRect = addRectangle(n)
        mRect = addRectangle(m)
        oRect = addRectangle(o)

        nLabel = createLabel(n, "nnnn")
        mLabel = createLabel(m, "m")
        oLabel = createLabel(o, "o")

        nmEdge = createEdge(n, m)
        noEdge = createEdge(n, o)
        
        addPolyline(nmEdge)
        addPolyline(noEdge)

        return root