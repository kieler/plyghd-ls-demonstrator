# generated by datamodel-codegen:
#   filename:  klighd/messages/diagramOptionsPerformAction.json
#   timestamp: 2024-11-14T11:48:42+00:00

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel

from ...lsp.requestMessage import RequestMessage


class Method(Enum):
    keith_diagramOptions_performAction = 'keith/diagramOptions/performAction'


class Params(BaseModel):
    actionId: str
    uri: str


class KeithDiagramoptionsPerformaction(RequestMessage):
    method: Method
    params: Params
