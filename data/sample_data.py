"""
Sample/mock data for VTuber livestream schedules.

Provides realistic mock data for testing the API endpoints
without requiring access to the live Holodex API.
"""

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List

# ---------------------------------------------------------------------------
# Channels
# ---------------------------------------------------------------------------
CHANNELS: List[Dict[str, Any]] = [
    {
        "id": "UC0TXe_LYZ4sca2K1sABgUAw",
        "name": "Gawr Gura",
        "org": "Hololive",
        "branch": "EN",
        "subscriber_count": 4500000,
        "video_count": 580,
        "photo": "https://yt3.ggpht.com/ytc/AIdro_l5fRWjG5J3Nkqhe3R4rMxqPLuL5QbU5RkXwA=s800-c-k-c0x00ffffff-no-rj",
        "description": "The Apex Predator of the Hololive English branch. A descendant of the Lost City of Atlantis.",
        "language": "en",
        "channel_url": "https://youtube.com/channel/UC0TXe_LYZ4sca2K1sABgUAw",
    },
    {
        "id": "UCp6993wxpyDPHUpEvwMTp2Q",
        "name": "Mori Calliope",
        "org": "Hololive",
        "branch": "EN",
        "subscriber_count": 2800000,
        "video_count": 420,
        "photo": "https://yt3.ggpht.com/ytc/AIdro_mJ9nJyYGrJ8XuB3G7H9uXNJ9zYrN1F0Tg=s800-c-k-c0x00ffffff-no-rj",
        "description": "Hololive English's grim reaper apprentice. Raps about death, life, and everything in between.",
        "language": "en",
        "channel_url": "https://youtube.com/channel/UCp6993wxpyDPHUpEvwMTp2Q",
    },
    {
        "id": "UChAnqc_AY5_I3Px5dig3X1Q",
        "name": "Houshou Marine",
        "org": "Hololive",
        "branch": "JP",
        "subscriber_count": 4200000,
        "video_count": 720,
        "photo": "https://yt3.ggpht.com/ytc/AIdro_l_XS0eET9VCRWg8G3nxpRnB8Ozi0zJ8w=s800-c-k-c0x00ffffff-no-rj",
        "description": "A pirate captain VTuber from Hololive 3rd Generation.",
        "language": "ja",
        "channel_url": "https://youtube.com/channel/UChAnqc_AY5_I3Px5dig3X1Q",
    },
    {
        "id": "UCdn5BQ06XqgXoAxI0YqPz3g",
        "name": "Kuzuha",
        "org": "Nijisanji",
        "branch": "JP",
        "subscriber_count": 2100000,
        "video_count": 950,
        "photo": "https://yt3.ggpht.com/ytc/AIdro_lXWQQyEiO7FR5aQ1AAo2bL4yB1O3Q=s800-c-k-c0x00ffffff-no-rj",
        "description": "A vampire lord from Nijisanji, known for gaming and singing streams.",
        "language": "ja",
        "channel_url": "https://youtube.com/channel/UCdn5BQ06XqgXoAxI0YqPz3g",
    },
    {
        "id": "UCmbs8T6MWqU4S1m6zB8TkDw",
        "name": "Koseki Bijou",
        "org": "Hololive",
        "branch": "EN",
        "subscriber_count": 950000,
        "video_count": 210,
        "photo": "https://yt3.ggpht.com/ytc/AIdro_k5O3F0Qr6C3F0Qr6C3F0Qr6C3F0Qr6C3F0Q=s800-c-k-c0x00ffffff-no-rj",
        "description": "A gemstone from the ReGLOSS project, shining brightly in Hololive English.",
        "language": "en",
        "channel_url": "https://youtube.com/channel/UCmbs8T6MWqU4S1m6zB8TkDw",
    },
    {
        "id": "UC8rcEBzJSleTkf_-agPM20g",
        "name": "Shylily",
        "org": "Phase Connect",
        "branch": "EN",
        "subscriber_count": 780000,
        "video_count": 340,
        "photo": "https://yt3.ggpht.com/ytc/AIdro_l8R0vKf1Q2s3R4t5Y6u7I8o9P0a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5=s800-c-k-c0x00ffffff-no-rj",
        "description": "An orca from Phase Connect who loves singing and chatting with viewers.",
        "language": "en",
        "channel_url": "https://youtube.com/channel/UC8rcEBzJSleTkf_-agPM20g",
    },
    {
        "id": "UC9mf_ZVpC5Y6VwQxTqWzqXg",
        "name": "Dokibird",
        "org": "VSpo",
        "branch": "EN",
        "subscriber_count": 620000,
        "video_count": 280,
        "photo": "https://yt3.ggpht.com/ytc/AIdro_k9L0mN1o2P3q4r5s6t7u8v9w0x1y2z3a4b5c6d7e8f9g0h1i2j3k4l5m6=s800-c-k-c0x00ffffff-no-rj",
        "description": "A chaotic bird from VSpo known for high-energy streams and gaming marathons.",
        "language": "en",
        "channel_url": "https://youtube.com/channel/UC9mf_ZVpC5Y6VwQxTqWzqXg",
    },
]

# ---------------------------------------------------------------------------
# Live Streams
# ---------------------------------------------------------------------------
LIVE_STREAMS: List[Dict[str, Any]] = [
    {
        "id": "abc123def45",
        "title": "【SUPER EXPO】hololive SUPER EXPO 2026 EXPO STAGE",
        "status": "live",
        "url": "https://youtube.com/watch?v=abc123def45",
        "live_viewers": 15234,
        "channel_id": "UCp6993wxpyDPHUpEvwMTp2Q",
        "channel_name": "Mori Calliope",
        "org": "Hololive",
        "started_at": (datetime.now(timezone.utc) - timedelta(hours=2, minutes=15)).isoformat(),
        "thumbnail": "https://i.ytimg.com/vi/abc123def45/maxresdefault.jpg",
        "topic": "event",
    },
    {
        "id": "ghi789jkl01",
        "title": "【Karaoke】Late Night Songs & Chill",
        "status": "live",
        "url": "https://youtube.com/watch?v=ghi789jkl01",
        "live_viewers": 8932,
        "channel_id": "UC0TXe_LYZ4sca2K1sABgUAw",
        "channel_name": "Gawr Gura",
        "org": "Hololive",
        "started_at": (datetime.now(timezone.utc) - timedelta(hours=0, minutes=45)).isoformat(),
        "thumbnail": "https://i.ytimg.com/vi/ghi789jkl01/maxresdefault.jpg",
        "topic": "karaoke",
    },
    {
        "id": "mno234pqr56",
        "title": "【APEX】Ranked Grind with viewers",
        "status": "live",
        "url": "https://youtube.com/watch?v=mno234pqr56",
        "live_viewers": 12450,
        "channel_id": "UCdn5BQ06XqgXoAxI0YqPz3g",
        "channel_name": "Kuzuha",
        "org": "Nijisanji",
        "started_at": (datetime.now(timezone.utc) - timedelta(hours=1, minutes=30)).isoformat(),
        "thumbnail": "https://i.ytimg.com/vi/mno234pqr56/maxresdefault.jpg",
        "topic": "gaming",
    },
    {
        "id": "stu789vwx01",
        "title": "【JUST CHATTING】Weekend hangout! Come say hi~",
        "status": "live",
        "url": "https://youtube.com/watch?v=stu789vwx01",
        "live_viewers": 5678,
        "channel_id": "UCmbs8T6MWqU4S1m6zB8TkDw",
        "channel_name": "Koseki Bijou",
        "org": "Hololive",
        "started_at": (datetime.now(timezone.utc) - timedelta(hours=0, minutes=20)).isoformat(),
        "thumbnail": "https://i.ytimg.com/vi/stu789vwx01/maxresdefault.jpg",
        "topic": "chatting",
    },
    {
        "id": "yza234bcd56",
        "title": "【ART】Digital painting - ocean sunset",
        "status": "live",
        "url": "https://youtube.com/watch?v=yza234bcd56",
        "live_viewers": 3456,
        "channel_id": "UC8rcEBzJSleTkf_-agPM20g",
        "channel_name": "Shylily",
        "org": "Phase Connect",
        "started_at": (datetime.now(timezone.utc) - timedelta(hours=3, minutes=0)).isoformat(),
        "thumbnail": "https://i.ytimg.com/vi/yza234bcd56/maxresdefault.jpg",
        "topic": "art",
    },
]

# ---------------------------------------------------------------------------
# Upcoming Streams (schedule)
# ---------------------------------------------------------------------------
UPCOMING_STREAMS: List[Dict[str, Any]] = [
    {
        "id": "efg567hij89",
        "title": "【DEBUT】New Outfit Reveal! ✨",
        "status": "upcoming",
        "url": "https://youtube.com/watch?v=efg567hij89",
        "scheduled_start": (datetime.now(timezone.utc) + timedelta(hours=2)).isoformat(),
        "channel_id": "UC0TXe_LYZ4sca2K1sABgUAw",
        "channel_name": "Gawr Gura",
        "org": "Hololive",
        "thumbnail": "https://i.ytimg.com/vi/efg567hij89/maxresdefault.jpg",
        "topic": "debut",
    },
    {
        "id": "klm012nop34",
        "title": "【RUST】Building the Ultimate Base",
        "status": "upcoming",
        "url": "https://youtube.com/watch?v=klm012nop34",
        "scheduled_start": (datetime.now(timezone.utc) + timedelta(hours=4, minutes=30)).isoformat(),
        "channel_id": "UCdn5BQ06XqgXoAxI0YqPz3g",
        "channel_name": "Kuzuha",
        "org": "Nijisanji",
        "thumbnail": "https://i.ytimg.com/vi/klm012nop34/maxresdefault.jpg",
        "topic": "gaming",
    },
    {
        "id": "qrs567tuv89",
        "title": "【UNARCHIVE】The Ancient City - Minecraft Exploration",
        "status": "upcoming",
        "url": "https://youtube.com/watch?v=qrs567tuv89",
        "scheduled_start": (datetime.now(timezone.utc) + timedelta(hours=6)).isoformat(),
        "channel_id": "UCp6993wxpyDPHUpEvwMTp2Q",
        "channel_name": "Mori Calliope",
        "org": "Hololive",
        "thumbnail": "https://i.ytimg.com/vi/qrs567tuv89/maxresdefault.jpg",
        "topic": "gaming",
    },
    {
        "id": "wxy012zab34",
        "title": "【COLLAB】Trash Taste Podcast After Dark",
        "status": "upcoming",
        "url": "https://youtube.com/watch?v=wxy012zab34",
        "scheduled_start": (datetime.now(timezone.utc) + timedelta(hours=8, minutes=15)).isoformat(),
        "channel_id": "UC9mf_ZVpC5Y6VwQxTqWzqXg",
        "channel_name": "Dokibird",
        "org": "VSpo",
        "thumbnail": "https://i.ytimg.com/vi/wxy012zab34/maxresdefault.jpg",
        "topic": "chatting",
    },
    {
        "id": "cde567fgh89",
        "title": "【MUSIC】Original Song Release Party 🎵",
        "status": "upcoming",
        "url": "https://youtube.com/watch?v=cde567fgh89",
        "scheduled_start": (datetime.now(timezone.utc) + timedelta(hours=12)).isoformat(),
        "channel_id": "UChAnqc_AY5_I3Px5dig3X1Q",
        "channel_name": "Houshou Marine",
        "org": "Hololive",
        "thumbnail": "https://i.ytimg.com/vi/cde567fgh89/maxresdefault.jpg",
        "topic": "music",
    },
    {
        "id": "ijk012lmn34",
        "title": "【SUPERCHAT】Reading Stream + Q&A",
        "status": "upcoming",
        "url": "https://youtube.com/watch?v=ijk012lmn34",
        "scheduled_start": (datetime.now(timezone.utc) + timedelta(hours=18)).isoformat(),
        "channel_id": "UC8rcEBzJSleTkf_-agPM20g",
        "channel_name": "Shylily",
        "org": "Phase Connect",
        "thumbnail": "https://i.ytimg.com/vi/ijk012lmn34/maxresdefault.jpg",
        "topic": "chatting",
    },
    {
        "id": "opq567rst89",
        "title": "【ZATSUDAN】Late night conversations under the stars",
        "status": "upcoming",
        "url": "https://youtube.com/watch?v=opq567rst89",
        "scheduled_start": (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat(),
        "channel_id": "UCmbs8T6MWqU4S1m6zB8TkDw",
        "channel_name": "Koseki Bijou",
        "org": "Hololive",
        "thumbnail": "https://i.ytimg.com/vi/opq567rst89/maxresdefault.jpg",
        "topic": "chatting",
    },
]


def get_live_streams(
    org: str = None,
    lang: str = None,
    min_viewers: int = None,
    limit: int = 25,
    offset: int = 0,
) -> List[Dict[str, Any]]:
    """Filter and return live streams."""
    results = list(LIVE_STREAMS)

    if org:
        results = [s for s in results if s["org"].lower() == org.lower()]
    if min_viewers:
        results = [s for s in results if s.get("live_viewers", 0) >= min_viewers]

    # Language filter via channel lookup
    if lang:
        lang_map = {c["name"].lower(): c["language"] for c in CHANNELS}
        results = [
            s for s in results
            if lang_map.get(s["channel_name"].lower(), "") == lang.lower()
        ]

    return results[offset: offset + limit]


def get_upcoming_streams(
    org: str = None,
    lang: str = None,
    limit: int = 25,
    offset: int = 0,
) -> List[Dict[str, Any]]:
    """Filter and return upcoming streams."""
    results = list(UPCOMING_STREAMS)

    if org:
        results = [s for s in results if s["org"].lower() == org.lower()]

    if lang:
        lang_map = {c["name"].lower(): c["language"] for c in CHANNELS}
        results = [
            s for s in results
            if lang_map.get(s["channel_name"].lower(), "") == lang.lower()
        ]

    return results[offset: offset + limit]


def get_channels(
    org: str = None,
    lang: str = None,
    limit: int = 25,
    offset: int = 0,
) -> List[Dict[str, Any]]:
    """Filter and return channel metadata."""
    results = list(CHANNELS)

    if org:
        results = [c for c in results if c["org"].lower() == org.lower()]
    if lang:
        results = [c for c in results if c.get("language", "").lower() == lang.lower()]

    return results[offset: offset + limit]
