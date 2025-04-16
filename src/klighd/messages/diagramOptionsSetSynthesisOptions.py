# generated by datamodel-codegen:
#   filename:  klighd/messages/diagramOptionsSetSynthesisOptions.json
#   timestamp: 2025-04-16T12:40:41+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel

from ...lsp.requestMessage import RequestMessage
from .. import SynthesisOptionSchema


class Method(Enum):
    keith_diagramOptions_setSynthesisOptions = (
        'keith/diagramOptions/setSynthesisOptions'
    )


class Params(BaseModel):
    synthesisOptions: List[SynthesisOptionSchema.ValuedSynthesisOption]
    uri: Optional[str] = None


class KeithDiagramoptionsSetsynthesisoptions(RequestMessage):
    method: Optional[Method] = 'keith/diagramOptions/setSynthesisOptions'
    params: Params
