# README: Mobile App (README_mobile.md)

## Purpose
The mobile app is the user-facing client. It captures the camera feed, drives the training workflow (voice labels per dart), and renders scoring/game UI.

## Responsibilities
- Camera capture (single fixed phone camera)
- “Training Mode” workflow:
  - after each throw: listen for a per-dart voice label (no dart index `n`)
  - allow undo/relabel
- “Play Mode” workflow:
  - no voice required
  - display predicted per-dart score + confidence
- Manual correction fallback (tap/confirm score or tap impact point, depending on UX choice)
- Streaming frames to the CV/Model Service (or sending periodic keyframes)
- Receiving inference results:
  - calibration status
  - dart detections
  - normalized coordinates
  - computed score per dart
  - confidence + debug overlays (optional)

## What the mobile app does NOT do
- It does not run YOLO training.
- It does not own the board calibration math (delegated to the CV/Model service).
- It does not decide long-term game persistence (delegated to backend).

## Key Flows
### Calibration
1) Start camera
2) Send frames until CV service reports "calibrated"
3) Show overlay + “calibration locked” indicator

### Training Mode
For each detected new dart event:
1) display predicted score
2) prompt for voice label (per dart)
3) send label to backend (and/or CV service depending on training design)
4) store event for later correction model training

### Play Mode
- Only consume CV results and update UI/game state.

## Integration
- API endpoints used (see Shared Contracts)
- Streaming method (HTTP MJPEG/RTSP/WebRTC/upload frames)
- Required permissions (camera, microphone)
