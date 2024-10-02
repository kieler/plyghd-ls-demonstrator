# generated by datamodel-codegen:
#   filename:  KGraphSchema.json
#   timestamp: 2024-10-02T12:10:57+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Model(BaseModel):
    __root__: Any


class KGraphData(BaseModel):
    properties: Optional[Dict[str, Any]] = None


class KRoundedRectangle(BaseModel):
    __root__: Any


class KPolyLine(BaseModel):
    __root__: Any


class KPolygon(BaseModel):
    __root__: Any


class KSpline(BaseModel):
    __root__: Any


class KImage(BaseModel):
    __root__: Any


class KEllipse(BaseModel):
    __root__: Any


class KArc(BaseModel):
    __root__: Any


class KText(BaseModel):
    __root__: Any


class KPlacementData(BaseModel):
    __root__: Any


class KGraphElement(BaseModel):
    data: Optional[List[KGraphData]] = None
    properties: Optional[Dict[str, Any]] = None
    parent: Optional[KGraphElement] = None
    type: Optional[str] = None


class KLabeledGraphElement(KGraphElement):
    labels: Optional[List[str]] = None


class KLabel(KGraphElement):
    text: Optional[str] = None
    type: str = Field('label', const=True)


class KRendering(KGraphData):
    parent: Optional[KRendering] = None
    placementData: Optional[KPlacementData] = None
    styles: Optional[List] = None
    actions: Optional[List] = None
    type: str = Field('KRenderingImpl', const=True)


class KContainerRendering(KRendering):
    children: Optional[List[KRendering]] = None
    childPlacement: Optional[Any] = None
    type: str = Field('KContainerRenderingImpl', const=True)


class KRectangle(KContainerRendering):
    type: str = Field('KRectangleImpl', const=True)


class KNode(KLabeledGraphElement):
    children: Optional[List[KNode]] = None
    outgoing_edges: Optional[List[KEdge]] = None
    incoming_edges: Optional[List[KEdge]] = None
    ports: Optional[List[KPort]] = None
    type: str = Field('node', const=True)


class KEdge(KGraphElement):
    source: Optional[KNode] = None
    target: Optional[KNode] = None
    source_port: Optional[KPort] = None
    target_port: Optional[KPort] = None
    type: str = Field('edge', const=True)


class KPort(KLabeledGraphElement):
    edges: Optional[List[KEdge]] = None
    type: str = Field('port', const=True)


KGraphElement.update_forward_refs()
KRendering.update_forward_refs()
KNode.update_forward_refs()
KEdge.update_forward_refs()
