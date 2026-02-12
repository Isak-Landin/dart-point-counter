import requests
from .config import MODEL_SERVICE_URL, TIMEOUT_SECONDS


def send_frame(image_bytes: bytes):
    files = {"frame": image_bytes}
    response = requests.post(
        f"{MODEL_SERVICE_URL}/infer",
        files=files,
        timeout=TIMEOUT_SECONDS,
    )
    response.raise_for_status()
    return response.json()
