from __future__ import annotations

from pydantic import BaseModel


class JudgeResponse(BaseModel):
    is_dajare: bool
    applied_rule: str
