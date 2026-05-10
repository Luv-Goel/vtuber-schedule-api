"""Tests for VTuber Schedule API sample data."""

from data.sample_data import (
    CHANNELS,
    LIVE_STREAMS,
    UPCOMING_STREAMS,
    get_live_streams,
    get_upcoming_streams,
    get_channels,
)


def test_sample_data_exists():
    assert len(CHANNELS) > 0
    assert len(LIVE_STREAMS) > 0
    assert len(UPCOMING_STREAMS) > 0


def test_get_live_streams_all():
    result = get_live_streams()
    assert len(result) > 0


def test_get_live_streams_filter_org():
    result = get_live_streams(org="Hololive")
    assert all(s["org"] == "Hololive" for s in result)


def test_get_live_streams_min_viewers():
    result = get_live_streams(min_viewers=10000)
    assert all(s["live_viewers"] >= 10000 for s in result)


def test_get_live_streams_limit():
    result = get_live_streams(limit=2)
    assert len(result) <= 2


def test_get_upcoming_streams_all():
    result = get_upcoming_streams()
    assert len(result) > 0


def test_get_upcoming_streams_filter_org():
    result = get_upcoming_streams(org="Hololive")
    assert all(s["org"] == "Hololive" for s in result)


def test_get_channels_all():
    result = get_channels()
    assert len(result) > 0


def test_get_channels_filter_lang():
    result = get_channels(lang="ja")
    assert all(c["language"] == "ja" for c in result)


def test_get_channels_filter_org():
    result = get_channels(org="Nijisanji")
    assert all(c["org"] == "Nijisanji" for c in result)
