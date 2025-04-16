# generated by datamodel-codegen:
#   filename:  lsp/textDocumentDocumentHighlight.json
#   timestamp: 2025-04-16T12:40:41+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel

from . import range
from .requestMessage import RequestMessage


class Method(Enum):
    textDocument_documentHighlight = 'textDocument/documentHighlight'


class TextDocument(BaseModel):
    uri: Optional[str] = None


class Params(BaseModel):
    textDocument: Optional[TextDocument] = None
    position: Optional[range.EditorPositionModel] = None


class TextdocumentDocumenthighlight(RequestMessage):
    method: Optional[Method] = 'textDocument/documentHighlight'
    params: Params
