import asyncio
from contextlib import asynccontextmanager
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.redis import RedisIntegration

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Запуск
    print("🚀 Service started")
    yield
    # Остановка
    await redis_client.close()
    await es.close()
    print("🛑 Service stopped")

app = FastAPI(lifespan=lifespan)

sentry_sdk.init(
    dsn="https://ваш-dsn@sentry.io/проект",
    integrations=[
        FastApiIntegration(),
        RedisIntegration(),
    ],
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)

@app.exception_handler(500)
async def internal_exception_handler(request, exc):
    sentry_sdk.capture_exception(exc)
    return JSONResponse(status_code=500, content={"detail": "Internal error"})