import asyncio
import json

import tornado.web

from src.constants import FAILED_RESPONSE
from src.utils import get_bot_response, parse_response


class MainHandler(tornado.web.RequestHandler):
    async def post(self):
        self.set_header("Content-Type", "application/json")
        request_json = json.loads(self.request.body)
        response = get_bot_response(request_json["message"])
        if len(response) > 0:
            self.write({"bot": parse_response(response)})
        else:
            self.write({"bot": FAILED_RESPONSE})

    def prepare(self):
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None


def make_app():
    return tornado.web.Application(
        [
            (r"/message", MainHandler),
        ]
    )


async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
