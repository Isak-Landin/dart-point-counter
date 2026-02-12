from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass
class FrameRequest:
    image_bytes: bytes


@dataclass
class DartPrediction:
    score: int
    confidence: float
    impact_point: Tuple[float, float]


@dataclass
class ModelResponse:
    calibrated: bool
    dart_detected: bool
    prediction: Optional[DartPrediction]
