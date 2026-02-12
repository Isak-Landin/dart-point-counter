# Project Concept: Self-Calibrating Dartboard Scoring System (Single Phone Camera)

## Overview

This system enables automatic dart scoring using a single fixed phone camera without requiring pre-trained datasets or large-scale model training. The system improves over time through user-provided voice labels during a training mode. Each dart throw is treated as an independent supervised event.

The objective is not to train a generalized dart-recognition model, but to create a setup-specific adaptive scoring system that calibrates itself to the user’s environment, lighting, and camera placement.

---

## Core Idea

The system does not attempt to “understand darts” in a semantic sense. Instead, it separates the problem into three deterministic components and one adaptive correction layer:

- Board Pose & Geometry Detection  
- Dart Impact Localization  
- Deterministic Score Mapping  
- Setup-Specific Error Correction (Adaptive Layer)

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

