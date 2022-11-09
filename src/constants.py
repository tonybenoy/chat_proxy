HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:106.0) \
        Gecko/20100101 Firefox/106.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://viru.alphablues.com/",
    "Content-Type": "application/json",
    "Origin": "https://viru.alphablues.com",
    "DNT": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
    "TE": "trailers",
}

URL = "https://bots.alphablues.com/alphachat-ai"

BODY_TEMPLATE = {
    "message": "",
    "type": "message",
    "role": "enduser",
    "sender_role": "enduser",
    "message_id": "",
    "sender": "",
    "api": "alphachat",
    "page_info": {
        "title": "Demo",
        "url": "https://viru.alphablues.com/demos/?id=alphachat-test",
        "language": "de",
    },
}

FAILED_RESPONSE = "Request failed"
