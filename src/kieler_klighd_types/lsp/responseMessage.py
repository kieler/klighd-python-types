# generated by datamodel-codegen:
#   filename:  lsp/responseMessage.json
#   timestamp: 2025-04-17T11:39:47+00:00

from __future__ import annotations

from typing import Any, Optional, Union

from .message import Message


class ResponseMessage(Message):
    id: Optional[Union[float, str]]
    result: Optional[Any] = None
    error: Optional[Any] = None
