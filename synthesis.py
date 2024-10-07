from graph_library import addProperty, createEdge, createLabel, createNode, createGraph
from rendering_library import addPolyline, addRectangle
from synthesis_options import SynthesisOption, SynthesisOptionType




ID = "de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis"

COLOR = SynthesisOption("de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.color", "Color", SynthesisOptionType.TEXT, "0x000000")
LABELS = SynthesisOption("de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.labels", "Labels", SynthesisOptionType.CHECK, True)


class PlyghdKgraphSynthesis:
    def getDisplayedSynthesisOptions(self):
        return [COLOR, LABELS]
    
    def transform(self, uri):
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
        mRect = addRectangle(m)
        oRect = addRectangle(o)

        nLabel = createLabel(n, "nnnn")
        mLabel = createLabel(m, "m")
        oLabel = createLabel(o, "o")

        nmEdge = createEdge(root, n, m)
        noEdge = createEdge(root, n, o)
        
        addPolyline(nmEdge)
        addPolyline(noEdge)

        return graph