# Chat Proxy

This is a simple chat proxy that allows you to connect to a chat server and then gets the response

## Usage
 This project uses poetry for dependency management. To install poetry, run `pip install poetry` and then run `poetry install` to install the dependencies.
 To run the project, run `poetry run python main.py` and then follow the instructions in the terminal.

## API usage
 The end points are as follows:
    - `/message` - Sends the message to the server and gets the response from the server
    The api takes the following parameters:
        - `message` - The message to send to the server
    The api returns the following parameters:
        - `bot` - The message from the server
    The api responds with `Request failed` if the request fails from the server.

The endpoint is deployed at `https://ch.tonybenoy.com/message`
