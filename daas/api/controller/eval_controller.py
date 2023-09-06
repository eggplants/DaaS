from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from daas.api.request.eval_request import EvalRequest
from daas.api.response.eval_response import EvalResponse
from daas.service.dajare_service import DajareService

dajare_service = DajareService()

eval_router = APIRouter()


@eval_router.get("/", status_code=200, response_model=EvalResponse, include_in_schema=False)
@eval_router.get("", status_code=200, response_model=EvalResponse)
async def eval_dajare(request: EvalRequest = Depends()) -> EvalResponse:
    # eval dajare
    try:
        dajare = dajare_service.eval_dajare(request.dajare)
    except Exception:  # noqa: BLE001
        raise HTTPException(status_code=500)

    return EvalResponse(
        score=dajare.score,
    )
