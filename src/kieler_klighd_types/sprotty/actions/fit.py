# generated by datamodel-codegen:
#   filename:  sprotty/actions/fit.json
#   timestamp: 2025-04-17T11:51:34+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from .action import Action


class Kind(Enum):
    fit = 'fit'


class Fit(Action):
    kind: Optional[Kind] = 'fit'
    elementIds: List[str]
    maxZoom: float
    animate: bool
