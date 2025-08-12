import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_create_poll(client: AsyncClient):
    response = await client.post("/polls/", json={
        "question": "Test?",
        "options": ["A", "B"]
    })
    assert response.status_code == 200
    data = response.json()
    assert data["question"] == "Test?"
