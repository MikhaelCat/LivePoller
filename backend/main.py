from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import JSONResponse

import sentry_sdk

from backend.core.cache import redis_client
from backend.services.search_service import es


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Service started")
    yield
    await redis_client.close()
    await es.close()
    print("🛑 Service stopped")


app = FastAPI(lifespan=lifespan)


@app.exception_handler(500)
async def internal_exception_handler(request, exc):
    sentry_sdk.capture_exception(exc)
    return JSONResponse(status_code=500, content={"detail": "Internal error"})
