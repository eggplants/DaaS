from __future__ import annotations

from pydantic import BaseModel


class JudgeRequest(BaseModel):
    dajare: str
