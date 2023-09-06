from fastapi import APIRouter, Depends, HTTPException

from daas.service.dajare_service import DajareService
from ..request.eval_request import EvalRequest
from ..response.eval_response import EvalResponse

dajare_service = DajareService()

eval_router = APIRouter()


@eval_router.get('/', status_code=200, response_model=EvalResponse, include_in_schema=False)
@eval_router.get('', status_code=200, response_model=EvalResponse)
async def eval_dajare(request: EvalRequest = Depends()):
    # eval dajare
    try:
        dajare = dajare_service.eval_dajare(request.dajare)
    except Exception:
        raise HTTPException(status_code=500)

    return EvalResponse(
        score=dajare.score,
    )
