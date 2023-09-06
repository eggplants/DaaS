from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from daas import __version__
from daas.api.controller.eval_controller import eval_router
from daas.api.controller.judge_controller import judge_router
from daas.api.controller.reading_controller import reading_router


def create_app() -> FastAPI:
    app = FastAPI()

    # middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # routing
    app.include_router(judge_router, prefix="/judge", tags=["dajare"])
    app.include_router(eval_router, prefix="/eval", tags=["dajare"])
    app.include_router(reading_router, prefix="/reading", tags=["dajare"])

    # index
    @app.get("/")
    def index():
        return "Hello, World!"

    # OpenAPI
    app.title = "DaaS API"
    app.description = "This is a document of DaaS."
    app.version = __version__

    app.openapi_tags = [{"name": "dajare", "description": "Operation with dajare _(ダジャレ)_ ."}]

    return app
