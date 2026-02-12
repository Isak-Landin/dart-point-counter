# README: CV/Model Service (README_model_integration.md)

## Purpose
Real-time computer vision service that turns a single camera stream into:
- board pose calibration
- dart impact localization
- normalized board coordinates
- deterministic score output

This service is based on bnww/dart-sense (YOLOv8 detection + calibration-point transform + score mapping).

## Responsibilities (signed off from dart-sense)
- Detect board calibration points (e.g., corners of specific segments)
- Compute transform into a standardized dartboard reference frame
- Detect darts in the frame and estimate their coordinates
- Compute score from normalized coordinates (ring + sector)
- Emit per-dart results suitable for gameplay

## Responsibilities (project-specific additions)
- “Dart event” gating (identify new dart vs existing darts; debounce; stable detection window)
- Confidence scoring and “unknown / needs confirmation” behavior
- Optional debug overlay rendering for the app
- Optional lightweight correction layer hooks (if used)

## Inputs
- Video stream or frames from the mobile app
- Calibration commands: start, lock, reset
- Optional: manual calibration assist (user tap to identify “20” direction, if needed)

## Outputs
- Calibration state: {uncalibrated, calibrating, calibrated, degraded}
- Board transform parameters (internal)
- Per-dart detection result:
  - timestamp
  - dart_id (generated event id)
  - (x_img, y_img)
  - (x_norm, y_norm)
  - score prediction
  - confidence
  - debug fields (optional)

## Dependency: Model Weights
- Requires the YOLO weights that dart-sense expects.
- This is a hard gating item: weight availability + license must be validated before productizing.

## What this service does NOT do
- No user accounts, no long-term storage
- No game rules (unless explicitly reused)
- No voice recognition (mobile app handles voice)

## Files from bnww/dart-sense to reuse/port
- video_processing.py (frame pipeline / orchestration)
- get_scores.py (coordinate → score mapping)
- (optional) game_logic.py (only if reusing their game rules)
Do not reuse GUI files.

## Deployment options
- Local on a LAN machine (mobile connects to local IP)
- Remote hosted service (mobile uploads frames; higher latency)
