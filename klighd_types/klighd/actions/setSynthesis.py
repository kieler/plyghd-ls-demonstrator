# generated by datamodel-codegen:
#   filename:  klighd/actions/setSynthesis.json
#   timestamp: 2024-11-14T11:48:42+00:00

from __future__ import annotations

from enum import Enum

from ...sprotty.actions.action import Action


class Kind(Enum):
    setSynthesis = 'setSynthesis'


class SetSynthesis(Action):
    kind: Kind
    id: str