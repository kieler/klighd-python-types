# generated by datamodel-codegen:
#   filename:  klighd/actions/checkedImages.json
#   timestamp: 2025-04-17T11:51:34+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from ...sprotty.actions.action import Action


class Kind(Enum):
    checkedImages = 'checkedImages'


class NotCachedImage(BaseModel):
    k: str
    v: str


class CheckedImages(Action):
    kind: Optional[Kind] = 'checkedImages'
    notCached: List[NotCachedImage]
    responseId: str
