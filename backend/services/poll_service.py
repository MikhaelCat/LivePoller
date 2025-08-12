from backend.core.cache import cache_get


class PollQueryService:
    async def get_poll(self, poll_id):
        cached = await cache_get(f"poll:{poll_id}")
        if cached:
            return cached
        # ... идти в БД
        return None
