# generated by datamodel-codegen:
#   filename:  klighd/actions/refreshLayout.json
#   timestamp: 2024-11-14T11:48:42+00:00

from __future__ import annotations

from enum import Enum

from ...sprotty.actions.action import Action


class Kind(Enum):
    refreshLayout = 'refreshLayout'


class RefreshLayout(Action):
    kind: Kind