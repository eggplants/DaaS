from __future__ import annotations

from pydantic import BaseModel


class EvalResponse(BaseModel):
    score: float
