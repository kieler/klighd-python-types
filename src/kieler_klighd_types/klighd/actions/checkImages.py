# generated by datamodel-codegen:
#   filename:  klighd/actions/checkImages.json
#   timestamp: 2025-04-17T11:45:50+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from ...sprotty.actions.action import Action


class Kind(Enum):
    checkImages = 'checkImages'


class Image(BaseModel):
    bundleName: str
    imagePath: str


class CheckImages(Action):
    kind: Optional[Kind] = 'checkImages'
    images: List[Image]
