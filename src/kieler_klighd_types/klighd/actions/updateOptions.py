# generated by datamodel-codegen:
#   filename:  klighd/actions/updateOptions.json
#   timestamp: 2025-04-17T11:51:34+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from ...sprotty.actions.action import Action
from .. import SynthesisOptionSchema


class Kind(Enum):
    updateOptions = 'updateOptions'


class UpdateOptions(Action):
    kind: Optional[Kind] = 'updateOptions'
    valuedSynthesisOptions: Optional[
        List[SynthesisOptionSchema.ValuedSynthesisOption]
    ] = []
    layoutOptions: Optional[List] = []
    actions: Optional[List] = []
    modelUri: str
