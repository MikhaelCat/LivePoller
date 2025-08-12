import redis.asyncio as redis

redis_client = redis.from_url("redis://localhost:6379", decode_responses=True)

async def cache_get(key: str):
    return await redis_client.get(key)

async def cache_set(key: str, value: str, expire: int = 300):
    await redis_client.setex(key, expire, value)