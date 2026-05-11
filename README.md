# 🎥 VTuber Schedule API

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-production-success.svg)
![Response Time](https://img.shields.io/badge/response-<0.4s-brightgreen.svg)
![Uptime](https://img.shields.io/badge/uptime-99.9%25-brightgreen.svg)

> **Official real-time VTuber livestream schedules and channel metadata API**  
> One API to access live streams, upcoming schedules, and channel data across 200+ VTuber organizations.

---

## 🚀 Quick Links

- 📡 **API Marketplace:** <https://rapidapi.com/luvgoel555/api/vtuber-schedule>
- 📚 **Documentation:** <https://vtuberschedule.nexware.top>
- ⚡ **Status:** Production Ready (v1.0.0)

---

## 🛠️ System Architecture

```
┌────────────────────────────────────────────────────────────────────┐
│                  VTuber Schedule API — System Overview                    │
├────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌─────────────────┐  Holodex API   ┌─────────────────┐              │
│  │  Data Collector   │ ──────────▶ │  Redis Cache       │              │
│  │  (background job) │  YouTube API  │  (60s / 5m / 1h)   │              │
│  └─────────────────┘              └──────────┬──────┘              │
│                                                  │                        │
│                                                  ▼                        │
│                               ┌─────────────────┐                       │
│                               │  FastAPI App       │                       │
│                               │  /v1/live          │                       │
│                               │  /v1/upcoming      │                       │
│                               │  /v1/channels      │                       │
│                               └──────────┬──────┘                       │
│                                          │                                │
│                       ┌────────────────┴────────────────┐               │
│                       │           RapidAPI Gateway            │               │
│                       │  (auth, rate limiting, billing, keys) │               │
│                       └──────────┬──────────────────┘               │
│                                  │                                        │
│           ┌───────────────────┴──────────────────┐               │
│           │   API Consumers                              │               │
│           │   Discord Bots | Web Apps | Mobile | Data    │               │
│           └─────────────────────────────────────┘               │
│                                                                            │
└────────────────────────────────────────────────────────────────────┘
```

**Tech Stack:** FastAPI — Redis (tiered TTL caching) — RapidAPI Gateway — Docker — Python

---

## ✨ Features

### 🔴 Live Streams

Get currently live VTuber streams with real-time viewer counts, metadata, and direct video links.

### 📅 Upcoming Schedule

Access scheduled streams for the next 48 hours with accurate start times and automatic timezone conversion.

### 🏢 Multi-Organization Coverage

Official coverage for major VTuber groups and agencies:

- Hololive (JP, EN, ID)
- Nijisanji (Global)
- VSpo
- Phase Connect
- 200+ additional organizations and indie groups

### 🌍 Timezone Conversion

All schedule data can be converted to any IANA timezone:

- `Asia/Kolkata`
- `America/New_York`
- `Europe/London`
- `Asia/Tokyo`
- 200+ other timezones supported

### 📺 Channel Metadata

Unified channel profile data:

- Subscriber counts
- Video counts
- Organization and branch
- Language tags
- Channel photos and descriptions

---

## 📊 Service Performance

| Metric                | Value                                           |
|-----------------------|-------------------------------------------------|
| Average Response Time | **< 0.4 seconds**                               |
| Cache Strategy        | Smart (60s live, 5m upcoming, 1h channels)      |
| Uptime SLA            | **99.9%**                                       |
| Concurrent Requests   | Unlimited (plan-based)                          |
| Data Freshness        | Real-time (up to 60s refresh on live streams)  |

The API is built for production workloads with a focus on reliability, latency, and consistency.

---

## 🎯 Common Use Cases

### Discord Bots

Send alerts when specific VTubers go live.

```python
# Pseudo-code example
streams = api.get_live_streams(org="Hololive", lang="en")
for stream in streams:
    discord.send_notification(f"{stream.title} is live!")
```

### Website Widgets

Embed a "Who's live now?" or "Upcoming streams" section on your site.

```javascript
// Pseudo-code example
fetch('/v1/upcoming?tz=America/New_York&limit=10')
  .then(res => res.json())
  .then(data => displaySchedule(data.streams))
```

### Mobile Apps

Show trending VTuber streams sorted by viewer count.

```swift
// Pseudo-code example
api.getLiveStreams(minViewers: 5000, limit: 20)
  .then { streams in showPopularStreams(streams) }
```

### Analytics Dashboards

Analyze streaming activity by org, language, or time of day.

```sql
-- Pseudo-code example
SELECT org, COUNT(*) AS live_count
FROM live_streams
GROUP BY org;
```

---

## 🔌 REST API Endpoints

### GET `/v1/live`

Returns currently-live VTuber streams.

**Query Parameters**

- `org` – Filter by organization (e.g., Hololive, Nijisanji)
- `lang` – Filter by language (`en`, `ja`, `id`, `ko`, `zh`, ...)
- `min_viewers` – Minimum concurrent viewer count
- `tz` – IANA timezone for the `start_local` field
- `limit` – Max results (1–50, default: 25)
- `offset` – Pagination offset

---

### GET `/v1/upcoming`

Returns VTuber streams scheduled for the next 48 hours.

**Query Parameters**

Same as `/v1/live`.

---

### GET `/v1/channels`

Returns VTuber channel metadata and statistics.

**Query Parameters**

- `org` – Filter by organization
- `lang` – Filter by language
- `limit` – Max results (1–50)
- `offset` – Pagination offset

---

### GET `/ping`

Health-check endpoint.

```json
{
  "status": "ok"
}
```

---

## 📖 Quick Start

### 1. Subscribe on RapidAPI

Get your API key from the RapidAPI marketplace:

- <https://rapidapi.com/luvgoel555/api/vtuber-schedule>

### 2. Make Your First Request

```bash
curl --request GET \
  --url 'https://vtuber-schedule.p.rapidapi.com/v1/live?limit=10' \
  --header 'X-RapidAPI-Host: vtuber-schedule.p.rapidapi.com' \
  --header 'X-RapidAPI-Key: YOUR_API_KEY'
```

### 3. Example Response (Live Streams)

```json
{
  "status": "ok",
  "updated_at": "2026-03-07T05:00:00.000Z",
  "count": 2,
  "streams": [
    {
      "id": "6OPvhDmBPzs",
      "title": "hololive SUPER EXPO 2026 EXPO STAGE",
      "status": "live",
      "url": "https://youtube.com/watch?v=6OPvhDmBPzs",
      "live_viewers": 15234,
      "channel": {
        "name": "hololive",
        "org": "Hololive",
        "subscriber_count": 2500000
      }
    }
  ]
}
```

---

## 🛠️ Integration Examples

### Python (requests)

```python
import requests

url = "https://vtuber-schedule.p.rapidapi.com/v1/live"

params = {
    "org": "Hololive",
    "lang": "en",
    "limit": 10
}

headers = {
    "X-RapidAPI-Key": "YOUR_KEY",
    "X-RapidAPI-Host": "vtuber-schedule.p.rapidapi.com"
}

response = requests.get(url, params=params, headers=headers)
data = response.json()

for stream in data["streams"]:
    print(f"{stream['title']} - {stream['live_viewers']} viewers")
```

### JavaScript (fetch)

```javascript
fetch('https://vtuber-schedule.p.rapidapi.com/v1/upcoming?tz=Asia/Tokyo&limit=5', {
  headers: {
    'X-RapidAPI-Key': 'YOUR_KEY',
    'X-RapidAPI-Host': 'vtuber-schedule.p.rapidapi.com'
  }
})
  .then(res => res.json())
  .then(data => console.log(data.streams));
```

### cURL

```bash
curl -X GET \
  'https://vtuber-schedule.p.rapidapi.com/v1/channels?org=Nijisanji&limit=10' \
  -H 'X-RapidAPI-Key: YOUR_KEY' \
  -H 'X-RapidAPI-Host: vtuber-schedule.p.rapidapi.com'
```

---

## 📚 Full Documentation

Full API reference and advanced guides:

- <https://vtuberschedule.nexware.top>

Includes:

- Detailed endpoint reference
- Request/response schemas
- Error codes and retry strategies
- Usage patterns for bots, dashboards, and apps
- Language-specific snippets
- FAQ and best practices

---

## 🔒 Security & Compliance

- HTTPS-only – All traffic encrypted with modern TLS
- API-key authentication via RapidAPI
- Plan-based rate limiting and fair-usage enforcement
- No user-identifiable request logging by default

For production applications, you should still implement your own access control, logging, and monitoring on top.

---

## 💰 Pricing

Plans are managed through RapidAPI:

| Plan   | Requests / Month | Price        |
|--------|------------------|-------------|
| Free   | Limited          | $0          |
| Basic  | Standard usage   | See RapidAPI|
| Pro    | High volume      | See RapidAPI|
| Ultra  | Very high volume | See RapidAPI|

👉 View live pricing and quotas: <https://rapidapi.com/luvgoel555/api/vtuber-schedule>

---

## ❓ FAQ

### How often is data updated?

- Live streams: typically refreshed every 60 seconds  
- Upcoming schedules: refreshed approximately every 5 minutes  
- Channel metadata: refreshed approximately every hour

### How is VTuber data collected?

The API uses proprietary data collection infrastructure that continuously monitors VTuber channels and schedules across multiple platforms to maintain real-time coverage of 200+ organizations.

### Do you support historical/archived streams?

Current focus is on **live** and **upcoming** streams. Historical data and archive endpoints are planned in future versions.

### Can I use this API in commercial projects?

Yes. The API is designed for production workloads in commercial apps, dashboards, and SaaS products. Make sure your subscription plan on RapidAPI matches your expected traffic.

### Is there a free tier?

Yes. A free tier is available on RapidAPI, suitable for testing, prototypes, and small personal projects.

---

## 🤝 Support & Contact

- API Issues & Q&A: RapidAPI Discussions  
  <https://rapidapi.com/luvgoel555/api/vtuber-schedule/discussions>
- Feature Requests: Submit via RapidAPI or contact via the marketplace page
- Status Check: Call the `/ping` endpoint for a live health check
- Docs: <https://vtuberschedule.nexware.top>

---

## 📈 Roadmap (Planned)

- WebSocket support for push-based live updates
- Historical stream data and analytics
- Advanced filtering (by game, tag, topic, viewer milestones)
- Channel statistics over time (growth, streaming frequency)
- Multi-platform expansion
- Optional GraphQL endpoint

---

## 🌟 Star This Repo

If this API is useful in your project, please consider starring the repository to support ongoing development.

---

## 📄 License

This repository contains public documentation and examples for the VTuber Schedule API.  
The API itself is a commercial service provided through RapidAPI.  
API usage is governed by your RapidAPI subscription and terms of service.

---

<div align="center">
  <p>Built with ❤️ for the VTuber community</p>
  <p>© 2026 VTuber Schedule API</p>
</div>
