from graph_library import addProperty, createEdge, createLabel, createNode, createGraph, createPort
from ls import getOption
from rendering_library import addAction, addChildText, addPolyline, addRectangle, addText, getId, setId
from kieler_klighd_types.klighd.SynthesisOptionSchema import CheckSynthesisOption
from kieler_klighd_types.klighd.SKGraphSchema import KRectangle



ID = "de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis"

LABELS = CheckSynthesisOption(id="de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.labels", sourceHash="de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.labels", name="Labels", initialValue=True)


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
        
        mPort = createPort(m)

        # nmEdge = createEdge(root, n, m)
        nmEdge = createEdge(root, n, mPort)
        noEdge = createEdge(root, n, o)

        if (getOption(current_options, LABELS)):
            nLabel = createLabel(n, "nnnn")
            mLabel = createLabel(m, "m")
            oLabel = createLabel(o, "o")
            mPortRect = addRectangle(mPort)
            # mPortLabel = createLabel(mPort, "10000000000")
            # addProperty(m, "org.eclipse.elk.portLabels.placement", [0])
            mnEdgeLabelHead = createLabel(nmEdge, "Head")
            addProperty(mnEdgeLabelHead, "org.eclipse.elk.edgeLabels.placement", 1)
            mnEdgeLabelTail = createLabel(nmEdge, "Tail")
            addProperty(mnEdgeLabelTail, "org.eclipse.elk.edgeLabels.placement", 2)
            mnEdgeLabelCenter = createLabel(nmEdge, "Center")
            addProperty(mnEdgeLabelCenter, "org.eclipse.elk.edgeLabels.placement", 0)
        
        addPolyline(nmEdge)
        addPolyline(noEdge)


        # a hierarchical node featuring a key rendering for smart zoom
        # TODO: for this feature to work correctly, the client micro layout needs to set the text bounds properties.
        hierarchicalNode = createNode(root)
        hierarchicalNodeRect = addRectangle(hierarchicalNode)
        scalingText = addChildText(hierarchicalNodeRect, "Scaling Text")
        addProperty(scalingText, "klighd.isNodeTitle", True)
        # TODO: specific placement data classes not yet in schema
        scalingText.placementData = {
            "type": "KPointPlacementDataImpl",
            "referencePoint": {
                "x": {
                    "type": "KLeftPositionImpl",
                    "absolute": 0.0,
                    "relative": 0.5,
                },
                "y": {
                    "type": "KTopPositionImpl",
                    "absolute": 0.0,
                    "relative": 0.0,
                }
            },
            "horizontalAlignment": 1,
            "verticalAlignment": 0,
            "horizontalMargin": 0,
            "verticalMargin": 0,
            "minWidth": 0,
            "minHeight": 0,
        }
        #  it.setPointPlacementData(createKPosition(LEFT, 0, 0.5f, TOP, 0, 0), H_CENTRAL, V_TOP, 0, 0, 0, 0);
        # KPosition referencePoint, HorizontalAlignment horizontalAlignment, VerticalAlignment verticalAlignment, float horizontalMargin, float verticalMargin, float minWidth, float minHeight)

        childNode1 = createNodeWithLabel(hierarchicalNode, "1")
        childNode2 = createNodeWithLabel(hierarchicalNode, "2")
        childNode3 = createNodeWithLabel(hierarchicalNode, "3")
        childNode4 = createNodeWithLabel(hierarchicalNode, "4")
        childNode5 = createNodeWithLabel(hierarchicalNode, "5")
        edge12 = createEdge(hierarchicalNode, childNode1, childNode2)
        edge23 = createEdge(hierarchicalNode, childNode2, childNode3)
        edge14 = createEdge(hierarchicalNode, childNode1, childNode4)
        edge15 = createEdge(hierarchicalNode, childNode1, childNode5)
        edge35 = createEdge(hierarchicalNode, childNode3, childNode5)
        edge45 = createEdge(hierarchicalNode, childNode4, childNode5)

        # a node with a custom proxy rendering.
        nodeWithProxyRendering = createNode(root)
        nodeWithProxyRenderingRect = addRectangle(nodeWithProxyRendering)
        addChildText(nodeWithProxyRenderingRect, "Node with proxy rendering")
        addProperty(nodeWithProxyRendering, "de.cau.cs.kieler.klighd.proxyView.renderNodeAsProxy", True)
        proxyRenderingRect = KRectangle()
        setId(proxyRenderingRect, nodeWithProxyRendering.id + "-proxy")
        # TODO: styles not yet in schema
        proxyRenderingRect.styles = [{"type": "KInvisibilityImpl", "invisible": True, "propagateToChildren": False, "selection": False}]
        addChildText(proxyRenderingRect, "Proxy Rendering")
        addProperty(nodeWithProxyRendering, "de.cau.cs.kieler.klighd.proxyView.proxyRendering", [proxyRenderingRect])

        # a node with a custom tag for semantic filtering.
        taggedNode = createNodeWithLabel(root, "Tagged Node with the Tag \"customTag\"")
        addProperty(taggedNode, "de.cau.cs.kieler.klighd.semanticFilter.tags", [{
            "tag": "customTag",
        }])

        return graph


def createNodeWithLabel(parent, text):
    theNode = createNode(parent)
    addRectangle(theNode)
    addProperty(theNode, "org.eclipse.elk.nodeSize.constraints", [2])
    addProperty(theNode, "org.eclipse.elk.nodeLabels.placement", [1, 4, 6])
    createLabel(theNode, text)
    return theNode
