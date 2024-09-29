import socket
import threading

import pytest

from playground.client_server.client import start_client
from playground.client_server.server import start_server


# Define a fixture for the server
@pytest.fixture(scope="module")
def start_test_server():
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()


# Test function for client-server communication
def test_client_server_communication():
    # Mock the socket methods for testing
    class MockSocket:
        def __init__(self):
            self.data = None

        def connect(self, server_address):
            pass

        def send(self, data):
            self.data = data

        def recv(self, buffer_size):
            return b"Thank you for connecting\r\n"

        def close(self):
            pass

    # Mock the socket creation method for the client
    original_socket = socket.socket
    socket.socket = lambda *args, **kwargs: MockSocket()

    try:
        # Run the client which should make use of the mocked socket
        start_client()
    finally:
        # Restore the original socket creation method
        socket.socket = original_socket
