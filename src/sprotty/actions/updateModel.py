# generated by datamodel-codegen:
#   filename:  sprotty/actions/updateModel.json
#   timestamp: 2025-04-16T12:40:41+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from ...klighd import SKGraphSchema
from .action import Action


class Kind(Enum):
    updateModel = 'updateModel'


class UpdateModel(Action):
    kind: Optional[Kind] = 'updateModel'
    newRoot: SKGraphSchema.SKGraph
