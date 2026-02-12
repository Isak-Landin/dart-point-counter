import random


def infer_mock():
    return {
        "calibrated": True,
        "dart_detected": True,
        "prediction": {
            "score": random.choice([20, 5, 1, 60]),
            "confidence": 0.82,
            "impact_point": (0.43, 0.71),
        },
    }
