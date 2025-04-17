# generated by datamodel-codegen:
#   filename:  klighd/actions/setSyntheses.json
#   timestamp: 2025-04-17T11:39:47+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from ...sprotty.actions.action import Action


class Kind(Enum):
    setSyntheses = 'setSyntheses'


class Synthesis(BaseModel):
    id: str
    displayName: str


class SetSyntheses(Action):
    kind: Optional[Kind] = 'setSyntheses'
    syntheses: List[Synthesis]
