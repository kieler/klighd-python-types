# generated by datamodel-codegen:
#   filename:  sprotty/actions/action.json
#   timestamp: 2025-04-17T11:51:34+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Action(BaseModel):
    kind: str
    requestId: Optional[str] = None
