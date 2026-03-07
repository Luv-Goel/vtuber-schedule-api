# Changelog

All notable changes to the VTuber Schedule API will be documented here.

## [1.0.0] - 2026-03-07

### Added
- Initial production release
- `/v1/live` endpoint for currently-live streams
- `/v1/upcoming` endpoint for scheduled streams
- `/v1/channels` endpoint for channel metadata
- Multi-organization support (200+ VTuber agencies)
- Timezone conversion (200+ IANA timezones)
- Smart caching system for optimal performance
- RapidAPI integration with secure authentication
- Comprehensive documentation site

### Performance
- Average response time: <0.4 seconds
- 99.9% uptime SLA
- Real-time data updates (60s refresh)

### Security
- HTTPS-only access
- RapidAPI authentication required
- Rate limiting per subscription plan
- Direct access blocked (403 error)