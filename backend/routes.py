from fastapi import APIRouter
from .schemas import ModelResponse, DartPrediction
import random

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/infer", response_model=ModelResponse)
def infer():
    # Temporary mock logic.
    # Later: call real model service or internal CV pipeline.
    return ModelResponse(
        calibrated=True,
        dart_detected=True,
        prediction=DartPrediction(
            score=random.choice([20, 5, 1, 60]),
            confidence=0.85,
            impact_point=(0.42, 0.68),
        ),
    )
