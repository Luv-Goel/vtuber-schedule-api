"""Tests for VTuber Schedule API."""

import pytest
from httpx import AsyncClient, ASGITransport

from api import app


@pytest.fixture
def client():
    transport = ASGITransport(app=app)
    return AsyncClient(transport=transport, base_url="http://test")


@pytest.mark.asyncio
async def test_ping(client):
    resp = await client.get("/ping")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "timestamp" in data


@pytest.mark.asyncio
async def test_root(client):
    resp = await client.get("/")
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "VTuber Schedule API"


@pytest.mark.asyncio
async def test_list_streams(client):
    resp = await client.get("/v1/streams")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "streams" in data
    assert data["count"] > 0


@pytest.mark.asyncio
async def test_list_streams_with_filters(client):
    resp = await client.get("/v1/streams?org=Hololive")
    assert resp.status_code == 200
    data = resp.json()
    for s in data["streams"]:
        assert s["org"] == "Hololive"


@pytest.mark.asyncio
async def test_list_streams_min_viewers(client):
    resp = await client.get("/v1/streams?min_viewers=5000")
    assert resp.status_code == 200
    data = resp.json()
    for s in data["streams"]:
        assert s["live_viewers"] >= 5000


@pytest.mark.asyncio
async def test_list_schedule(client):
    resp = await client.get("/v1/schedule")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "streams" in data
    assert data["count"] > 0


@pytest.mark.asyncio
async def test_list_schedule_with_filters(client):
    resp = await client.get("/v1/schedule?org=Nijisanji")
    assert resp.status_code == 200
    data = resp.json()
    for s in data["streams"]:
        assert s["org"] == "Nijisanji"


@pytest.mark.asyncio
async def test_list_channels(client):
    resp = await client.get("/v1/channels")
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "channels" in data
    assert data["count"] > 0


@pytest.mark.asyncio
async def test_list_channels_with_filters(client):
    resp = await client.get("/v1/channels?org=Hololive")
    assert resp.status_code == 200
    data = resp.json()
    for c in data["channels"]:
        assert c["org"] == "Hololive"


@pytest.mark.asyncio
async def test_pagination(client):
    resp = await client.get("/v1/streams?limit=1")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data["streams"]) <= 1


@pytest.mark.asyncio
async def test_language_filter(client):
    resp = await client.get("/v1/channels?lang=en")
    assert resp.status_code == 200
    data = resp.json()
    for c in data["channels"]:
        assert c.get("language") == "en"
