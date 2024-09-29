# test_rest_api.py
import json
import threading
from http.client import HTTPConnection
from http.server import HTTPServer

from playground.client_server.rest_api import (
    BOOKS_ENDPOINT,
    BooksRequestHandler,
    books,
)

PORT = 8001


def start_server():
    server_address = ("", PORT)
    httpd = HTTPServer(server_address, BooksRequestHandler)
    httpd.serve_forever()


def setup_module(module):
    # Start the server in a new thread
    server_thread = threading.Thread(target=start_server)

    server_thread.daemon = True
    server_thread.start()


def teardown_module(module):
    # We can't serve_forever without being able to shutdown, so this will just show a proper way to cleanup.
    pass


def test_get_books():
    conn = HTTPConnection("localhost", PORT)
    conn.request("GET", BOOKS_ENDPOINT)
    response = conn.getresponse()
    assert response.status == 200
    data = json.loads(response.read().decode())
    assert len(data["books"]) == len(books.books)
    assert data["books"][0]["title"] == books.books[0].title


def test_post_book():
    new_book = {"id": 9, "title": "Python Testing with Pytest", "author": "Brian Okken"}
    headers = {"Content-type": "application/json"}
    conn = HTTPConnection("localhost", PORT)
    conn.request("POST", BOOKS_ENDPOINT, json.dumps(new_book), headers)
    response = conn.getresponse()
    assert response.status == 201
    data = json.loads(response.read().decode())

    # Ensure book is added
    assert data["id"] == new_book["id"]
    assert data["title"] == new_book["title"]
    assert data["author"] == new_book["author"]

    # Retrieve books and verify the new book is in the list
    conn.request("GET", BOOKS_ENDPOINT)
    response = conn.getresponse()
    assert response.status == 200
    data = json.loads(response.read().decode())
    assert any(book["id"] == new_book["id"] for book in data["books"])


def test_post_book_invalid_data():
    invalid_book = {"id": "invalid_id"}
    headers = {"Content-type": "application/json"}
    conn = HTTPConnection("localhost", PORT)
    conn.request("POST", BOOKS_ENDPOINT, json.dumps(invalid_book), headers)
    response = conn.getresponse()
    assert response.status == 400
    data = json.loads(response.read().decode())
    assert "error" in data
    assert "Invalid data" in data["error"]
