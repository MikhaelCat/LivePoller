from prometheus_client import Counter, Histogram, generate_latest
from fastapi import APIRouter

router = APIRouter()

REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Request latency')

@router.get("/metrics")
async def metrics():
    return generate_latest()

@router.get("/health")
async def health():
    return {"status": "healthy", "service": "poll-service"}