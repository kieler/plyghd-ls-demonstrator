# generated by datamodel-codegen:
#   filename:  klighd/actions/setDiagramPiece.json
#   timestamp: 2024-11-14T11:48:42+00:00

from __future__ import annotations

from enum import Enum

from ...sprotty.actions.action import Action
from .. import SKGraphSchema


class Kind(Enum):
    setDiagramPiece = 'setDiagramPiece'


class SetDiagramPiece(Action):
    kind: Kind
    diagramPiece: SKGraphSchema.SKNode
