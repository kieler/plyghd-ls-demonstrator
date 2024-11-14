# generated by datamodel-codegen:
#   filename:  lsp/range.json
#   timestamp: 2024-11-14T11:48:42+00:00

from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class EditorPosition(BaseModel):
    line: int
    character: int


class EditorPositionModel(BaseModel):
    __root__: Any


class Range(BaseModel):
    start: EditorPosition
    end: EditorPosition