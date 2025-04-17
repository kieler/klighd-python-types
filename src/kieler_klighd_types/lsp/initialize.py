# generated by datamodel-codegen:
#   filename:  lsp/initialize.json
#   timestamp: 2025-04-17T11:39:47+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, Optional

from pydantic import BaseModel

from .requestMessage import RequestMessage


class Method(Enum):
    initialize = 'initialize'


class ClientInfo(BaseModel):
    name: Optional[str] = None


class ClientDiagramOptions(BaseModel):
    preference: Optional[Dict[str, Any]] = None
    render: Optional[Dict[str, Any]] = None
    synthesis: Optional[Dict[str, Any]] = None


class InitializationOptions(BaseModel):
    clientDiagramOptions: Optional[ClientDiagramOptions] = None


class Params(BaseModel):
    processId: Optional[Any] = None
    workspaceFolders: Optional[Any] = None
    rootUri: Optional[Any] = None
    clientInfo: Optional[ClientInfo] = None
    capabilities: Optional[Dict[str, Any]] = None
    initializationOptions: Optional[InitializationOptions] = None


class Initialize(RequestMessage):
    method: Optional[Method] = 'initialize'
    params: Params
