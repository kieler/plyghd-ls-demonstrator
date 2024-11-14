# generated by datamodel-codegen:
#   filename:  lsp/requestMessage.json
#   timestamp: 2024-11-14T11:48:42+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from .message import Message


class Method(Enum):
    requestMessage = 'requestMessage'


class RequestMessage(Message):
    id: Optional[Union[float, str]] = None
    method: Method
    params: Optional[Union[List[Any], Dict[str, Any]]] = None
