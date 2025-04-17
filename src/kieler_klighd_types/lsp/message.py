# generated by datamodel-codegen:
#   filename:  lsp/message.json
#   timestamp: 2025-04-17T11:39:47+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class Jsonrpc(Enum):
    field_2_0 = '2.0'


class Message(BaseModel):
    jsonrpc: Optional[Jsonrpc] = '2.0'
