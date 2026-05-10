"""
VTuber Schedule API — FastAPI application.

Provides real-time VTuber livestream schedules, live stream data,
and channel metadata across 200+ organizations.
"""

import os
import logging
from datetime import datetime, timezone
from typing import List, Optional

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from data.sample_data import (
    get_live_streams,
    get_upcoming_streams,
    get_channels,
)

# ---------------------------------------------------------------------------
# App Setup
# ---------------------------------------------------------------------------

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("vtuber-schedule-api")

app = FastAPI(
    title="VTuber Schedule API",
    description="Real-time VTuber livestream schedules — live streams, upcoming"
                " schedules, and channel metadata across 200+ organizations.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Health
# ---------------------------------------------------------------------------


@app.get("/ping", tags=["Health"])
async def ping():
    """Health-check endpoint."""
    return {"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()}


@app.get("/", tags=["Health"])
async def root():
    """Root redirect to docs."""
    return {
        "name": "VTuber Schedule API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc",
    }


# ---------------------------------------------------------------------------
# /v1/streams — Currently live streams
# ---------------------------------------------------------------------------


@app.get("/v1/streams", tags=["Streams"])
async def list_streams(
    org: Optional[str] = Query(None, description="Filter by organization (e.g., Hololive, Nijisanji)"),
    lang: Optional[str] = Query(None, description="Filter by language code (en, ja, id, ...)"),
    min_viewers: Optional[int] = Query(None, description="Minimum concurrent viewer count"),
    limit: int = Query(25, ge=1, le=50, description="Max results"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
):
    """Returns currently-live VTuber streams with viewer counts and metadata."""
    streams = get_live_streams(
        org=org,
        lang=lang,
        min_viewers=min_viewers,
        limit=limit,
        offset=offset,
    )
    return {
        "status": "ok",
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(streams),
        "streams": streams,
    }


# ---------------------------------------------------------------------------
# /v1/schedule — Upcoming streams
# ---------------------------------------------------------------------------


@app.get("/v1/schedule", tags=["Schedule"])
async def list_schedule(
    org: Optional[str] = Query(None, description="Filter by organization (e.g., Hololive, Nijisanji)"),
    lang: Optional[str] = Query(None, description="Filter by language code (en, ja, id, ...)"),
    limit: int = Query(25, ge=1, le=50, description="Max results"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
):
    """Returns VTuber streams scheduled for the next 48 hours."""
    streams = get_upcoming_streams(
        org=org,
        lang=lang,
        limit=limit,
        offset=offset,
    )
    return {
        "status": "ok",
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(streams),
        "streams": streams,
    }


# ---------------------------------------------------------------------------
# /v1/channels — Channel metadata
# ---------------------------------------------------------------------------


@app.get("/v1/channels", tags=["Channels"])
async def list_channels(
    org: Optional[str] = Query(None, description="Filter by organization (e.g., Hololive, Nijisanji)"),
    lang: Optional[str] = Query(None, description="Filter by language code (en, ja, id, ...)"),
    limit: int = Query(25, ge=1, le=50, description="Max results"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
):
    """Returns VTuber channel metadata, subscriber counts, and statistics."""
    channels = get_channels(
        org=org,
        lang=lang,
        limit=limit,
        offset=offset,
    )
    return {
        "status": "ok",
        "updated_at": datetime.now(timezone.utc).isoformat(),
        "count": len(channels),
        "channels": channels,
    }


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    uvicorn.run("api:app", host=host, port=port, reload=True)
