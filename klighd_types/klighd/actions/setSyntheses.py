# generated by datamodel-codegen:
#   filename:  klighd/actions/setSyntheses.json
#   timestamp: 2024-11-14T11:48:42+00:00

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel

from ...sprotty.actions.action import Action


class Kind(Enum):
    setSyntheses = 'setSyntheses'


class Synthesis(BaseModel):
    id: str
    displayName: str


class SetSyntheses(Action):
    kind: Kind
    syntheses: List[Synthesis]
