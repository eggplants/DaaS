from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException

from daas.api.request.reading_request import ReadingRequest
from daas.api.response.reading_response import ReadingResponse
from daas.service.dajare_service import DajareService

dajare_service = DajareService()

reading_router = APIRouter()


@reading_router.get("/", status_code=200, response_model=ReadingResponse, include_in_schema=False)
@reading_router.get("", status_code=200, response_model=ReadingResponse)
async def reading_dajare(request: ReadingRequest = Depends()):
    # convert reading
    try:
        dajare = dajare_service.convert_reading(request.dajare)
    except Exception:  # noqa: BLE001
        raise HTTPException(status_code=500)

    return ReadingResponse(
        reading=dajare.reading,
    )
