import uuid
from typing import Any, Dict, List

import httpx

from src.constants import BODY_TEMPLATE, FAILED_RESPONSE, HEADERS, URL


def get_bot_response(message: str) -> List[Dict[str, Any]]:
    body = BODY_TEMPLATE
    body.update(
        {
            "message": message,
            "message_id": str(uuid.uuid4()),
            "sender": str(uuid.uuid4()),
        }
    )
    try:
        with httpx.Client() as client:
            response = client.post(
                URL,
                headers=HEADERS,
                json=body,
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as exc:
        print(exc)
        return []


def parse_response(response: List[Dict[str, Any]]) -> str:
    if len(response) > 0:
        return response[0].get("text", FAILED_RESPONSE)
    return "Request failed"
