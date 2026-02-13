# Project Concept: Self-Calibrating Dartboard Scoring System (Single Phone Camera)

# ⚠️ UNDER CONSTRUCTION

🚧 This repository is actively being built.  
It is not production-ready and should not be used or deployed.

Interfaces, architecture, and behavior are subject to change without notice.

___

## Overview

This system enables automatic dart scoring using a single fixed phone camera without requiring pre-trained datasets or large-scale model training. The system improves over time through user-provided voice labels during a training mode. Each dart throw is treated as an independent supervised event.

The objective is not to train a generalized dart-recognition model, but to create a setup-specific adaptive scoring system that calibrates itself to the user’s environment, lighting, and camera placement.

---

## Components

- [Mobile App](mobile_app/README.md)
- [Backend](backend/README.md)
- [Model Service](model_integration/README.md)

## Core Idea

This project is easiest to reason about as 4 sections (not 3):

1) Mobile App (client UX + camera + voice input)
2) CV/Model Service (dart-sense-based inference + calibration + scoring API)
3) Backend (accounts, games, sessions, storage, telemetry, sync)
4) Shared Contracts (schemas, message formats, versioning, error codes)

The adaptive layer is trained using voice-labeled darts during gameplay in training mode.

Each dart throw is treated as an independent event. No assumption is made about dart order (`n` remains unspecified and irrelevant to model training). The only learning objective is:

> Improve the accuracy of the predicted score for a single detected dart impact.

---

## System Architecture

### 1. Board Pose & Geometry Detection

At initialization:

- Detect board circle (or ellipse) from camera feed.  
- Estimate homography mapping image coordinates → normalized board coordinates.  
- Identify board center and outer radius.  
- Establish angular segmentation (20 sectors).  
- Define radial ring thresholds (Single / Double / Triple / Bull).  

Once calibrated, board geometry remains fixed unless re-calibration is triggered.

No training required.

---

### 2. Dart Impact Detection

For each throw:

- Use temporal differencing to detect the newly introduced dart.  
- Extract mask or bounding box of the new object.  
- Estimate shaft direction.  
- Estimate impact point (tip) using geometric heuristics.  

The output is an initial impact coordinate `(x_raw, y_raw)` in board space.

This estimate is deterministic and may contain systematic bias.

---

### 3. Deterministic Score Mapping

Given:

- Corrected board coordinate `(x, y)`  
- Known board geometry  

Compute:

- Radius → determines ring (single, double, triple, bull)  
- Angle → determines base number (1–20)  

Score prediction is fully deterministic once `(x, y)` is accurate.

No learning occurs in this step.

---

### 4. Adaptive Error Correction Layer

#### Purpose

Correct systematic error in impact localization due to:

- Camera angle distortion  
- Tip estimation bias  
- Lighting variation  
- Partial occlusion  

#### Training Mode Operation

For each dart event:

1. System predicts score from `(x_raw, y_raw)`.  
2. User provides voice label for that specific dart.  
3. Store tuple:

