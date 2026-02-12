from pydantic import BaseModel
from typing import Optional, Tuple


class DartPrediction(BaseModel):
    score: int
    confidence: float
    impact_point: Tuple[float, float]


class ModelResponse(BaseModel):
    calibrated: bool
    dart_detected: bool
    prediction: Optional[DartPrediction]
