# README: Shared Contracts (README_contracts.md)

## Purpose
Defines stable schemas between:
- Mobile App ↔ Model Service
- Mobile App ↔ Backend
- Backend ↔ Model Service (optional)

## Must include
- Versioned payload envelopes
- Error codes
- Calibration state machine definitions
- Per-dart event schema (predicted + labeled)
- Idempotency strategy (dart_event_id)

## Core rule
Training is per-dart, independent.
No reliance on “dart index n” or 3-dart totals.
