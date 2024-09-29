import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any

Book = dict[str, Any]
books: list[Book] = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "1984", "author": "George Orwell"},
    {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {
        "id": 5,
        "title": "Foley Is Good: And the Real World Is Faker Than Wrestling",
        "author": "Mick Foley",
    },
    {
        "id": 6,
        "title": "Hitman: My Real Life in the Cartoon World of Wrestling",
        "author": "Bret Hart",
    },
    {
        "id": 7,
        "title": "Undisputed: How to Become World Champion in 1,372 Easy Steps",
        "author": "Chris Jericho",
    },
    {
        "id": 8,
        "title": "Have A Nice Day: A Tale of Blood and Sweatsocks",
        "author": "Mick Foley",
    },
]


class RequestHandler(BaseHTTPRequestHandler):
    def _handle_get_books(self) -> None:
        self._set_response()
        self.wfile.write(json.dumps(books).encode("utf-8"))

    def _handle_post_book(self) -> None:
        content_length = int(self.headers["Content-Length"])
        if content_length == 0:
            self._set_response(400)
            self.wfile.write(json.dumps({"error": "No data provided"}).encode("utf-8"))
            return
        post_data = self.rfile.read(content_length)
        try:
            new_book: Book = json.loads(post_data)
            if (
                "id" not in new_book
                or "title" not in new_book
                or "author" not in new_book
            ):
                raise ValueError("Missing fields")
            books.append(new_book)
            self._set_response(201)
            self.wfile.write(json.dumps(new_book).encode("utf-8"))
        except (json.JSONDecodeError, ValueError) as e:
            self._set_response(400)
            self.wfile.write(
                json.dumps({"error": "Invalid data", "message": str(e)}).encode("utf-8")
            )

    def _set_response(self, status_code: int = 200) -> None:
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self) -> None:
        if self.path == "/books":
            self._handle_get_books()
        else:
            self._set_response(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode("utf-8"))

    def do_POST(self) -> None:
        if self.path == "/books":
            self._handle_post_book()
        else:
            self._set_response(404)
            self.wfile.write(json.dumps({"error": "Not Found"}).encode("utf-8"))


def run(
    server_class: type[HTTPServer] = HTTPServer,
    handler_class: type[BaseHTTPRequestHandler] = RequestHandler,
    port: int = 8000,
) -> None:
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
