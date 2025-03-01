import logging
import time


from fastapi import FastAPI
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.responses import Response

from app.core.resources import Resources
from app.core.settings import Settings
from app.routers import router

logger = logging.getLogger("uvicorn")

settings = Settings()


def init_app(settings: Settings) -> FastAPI:
    exception_handlers = {
        RequestValidationError: invalid_data,
        Exception: internal_error,
    }

    app = FastAPI(
        title=settings.api_name,
        version=settings.api_version,
        openapi_url=settings.prefix + "/openapi.json",
        docs_url=settings.prefix + "/docs",
        redoc_url=None,
        on_startup=[startup],
        exception_handlers=exception_handlers,
    )
    print(settings.prefix + "/docs")
    app.include_router(router)
    return app


async def invalid_data(_: Request, exc: Exception) -> Response:
    return JSONResponse(status_code=422, content={"error": str(exc)})


async def internal_error(_: Request, exc: Exception) -> Response:
    return JSONResponse(status_code=500, content={"error": str(exc)})


async def startup():
    logger.info("Initializing resources...")
    begin = time.time()
    Resources()
    end = time.time()
    timer = float(end - begin)
    logger.info(f"Resources initialization took {timer:.3f} seconds")
