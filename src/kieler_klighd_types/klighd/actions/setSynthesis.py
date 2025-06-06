# generated by datamodel-codegen:
#   filename:  klighd/actions/setSynthesis.json
#   timestamp: 2025-04-17T11:51:34+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from ...sprotty.actions.action import Action


class Kind(Enum):
    setSynthesis = 'setSynthesis'


class SetSynthesis(Action):
    kind: Optional[Kind] = 'setSynthesis'
    id: str
