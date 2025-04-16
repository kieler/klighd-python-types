# generated by datamodel-codegen:
#   filename:  lsp/requestMessage.json
#   timestamp: 2025-04-16T12:40:41+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from .message import Message


class Method(Enum):
    requestMessage = 'requestMessage'


class RequestMessage(Message):
    id: Optional[Union[float, str]] = None
    method: Optional[Method] = 'requestMessage'
    params: Optional[Union[List[Any], Dict[str, Any]]] = None
