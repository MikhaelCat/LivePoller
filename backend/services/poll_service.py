from backend.core.cache import cache_get, cache_set

class PollQueryService:
    async def get_poll(self, poll_id):
        cached = await cache_get(f"poll:{poll_id}")
        if cached:
            return cached

class PollCommandService:
    async def create_poll(self, poll_data, db):
        # Запись в БД
        pass


