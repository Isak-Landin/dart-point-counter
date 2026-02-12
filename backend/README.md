# README: Backend (README_backend.md)

## Purpose
System-of-record for sessions, games, training data, and analytics.

## Responsibilities
- User identity (optional for MVP)
- Game sessions and rules (x01, cricket, training-only, etc.)
- Event storage:
  - per-dart events (detections + labels)
  - calibration sessions
  - correction outcomes / confirmations
- Training dataset accumulation (from real play):
  - store labels per dart
  - store associated detection metadata
- Issuing configuration to CV service (if centralized):
  - model service endpoints
  - versioning/compatibility checks
- Telemetry/monitoring:
  - detection success rates
  - calibration stability
  - latency

## Data model (minimum)
- Session
- DartEvent (predicted score + optional user label)
- CalibrationSession
- Device/CameraConfig (optional)

## Interfaces
- REST endpoints for app:
  - create session
  - submit labeled dart event
  - fetch session state/history
- Optional: backend ↔ model-service coordination endpoints
