from __future__ import annotations

from pydantic import BaseModel


class ReadingRequest(BaseModel):
    dajare: str
