from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from daas.api.request.judge_request import JudgeRequest
from daas.api.response.judge_response import JudgeResponse
from daas.service.dajare_service import DajareService

dajare_service = DajareService()

judge_router = APIRouter()


@judge_router.get("/", status_code=200, response_model=JudgeResponse, include_in_schema=False)
@judge_router.get("", status_code=200, response_model=JudgeResponse)
async def judge_dajare(request: JudgeRequest = Depends()) -> JudgeResponse:
    # judge dajare
    try:
        dajare = dajare_service.judge_dajare(request.dajare)
    except Exception:  # noqa: BLE001
        raise HTTPException(status_code=500)

    return JudgeResponse(
        is_dajare=dajare.is_dajare,
        applied_rule=dajare.applied_rule,
    )
