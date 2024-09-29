import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from pydantic import BaseModel

# Constants
BOOKS_ENDPOINT = "/books"
CONTENT_TYPE = "Content-type"
JSON_CONTENT = "application/json"


class Book(BaseModel):
    id: int
    title: str
    author: str


class BookList(BaseModel):
    books: list[Book]


books = BookList(
    books=[
        Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald"),
        Book(id=2, title="To Kill a Mockingbird", author="Harper Lee"),
        Book(id=3, title="1984", author="George Orwell"),
        Book(id=4, title="The Catcher in the Rye", author="J.D. Salinger"),
        Book(
            id=5,
            title="Foley Is Good: And the Real World Is Faker Than Wrestling",
            author="Mick Foley",
        ),
        Book(
            id=6,
            title="Hitman: My Real Life in the Cartoon World of Wrestling",
            author="Bret Hart",
        ),
        Book(
            id=7,
            title="Undisputed: How to Become World Champion in 1,372 Easy Steps",
            author="Chris Jericho",
        ),
        Book(
            id=8,
            title="Have A Nice Day: A Tale of Blood and Sweatsocks",
            author="Mick Foley",
        ),
    ]
)


class BooksRequestHandler(BaseHTTPRequestHandler):
    def _handle_get_books(self) -> None:
        """Handle GET request for books."""
        self._set_response()
        self.wfile.write(books.model_dump_json().encode("utf-8"))

    def _handle_post_book(self) -> None:
        """Handle POST request to add a new book."""
        content_length = int(self.headers["Content-Length"])
        if content_length == 0:
            self._send_error_response(400, "No data provided")
            return
        post_data = self.rfile.read(content_length)
        try:
            new_book = Book.model_validate_json(post_data)
            books.books.append(new_book)
            self._set_response(201)
            self.wfile.write(new_book.model_dump_json().encode("utf-8"))
        except ValueError as e:
            self._send_error_response(400, f"Invalid data: {str(e)}")

    def _set_response(self, status_code: int = 200) -> None:
        """Set the response headers."""
        self.send_response(status_code)
        self.send_header(CONTENT_TYPE, JSON_CONTENT)
        self.end_headers()

    def _send_error_response(self, status_code: int, message: str) -> None:
        """Send an error response."""
        self._set_response(status_code)
        self.wfile.write(json.dumps({"error": message}).encode("utf-8"))

    def do_GET(self) -> None:
        """Handle GET requests."""
        if self.path == BOOKS_ENDPOINT:
            self._handle_get_books()
        else:
            self._send_error_response(404, "Not Found")

    def do_POST(self) -> None:
        """Handle POST requests."""
        if self.path == BOOKS_ENDPOINT:
            self._handle_post_book()
        else:
            self._send_error_response(404, "Not Found")


def run(
    server_class: type[HTTPServer] = HTTPServer,
    handler_class: type[BaseHTTPRequestHandler] = BooksRequestHandler,
    port: int = 8000,
) -> None:
    """Run the HTTP server."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting books server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
