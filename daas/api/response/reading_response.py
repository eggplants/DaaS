from __future__ import annotations

from pydantic import BaseModel


class ReadingResponse(BaseModel):
    reading: str
