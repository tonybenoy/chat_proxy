from src.utils import get_bot_response, parse_response


def test_get_bot_response():
    response = get_bot_response("Hello")
    assert len(response) > 0


def test_parse_response():
    response = []
    assert parse_response(response) != "Request failed"
