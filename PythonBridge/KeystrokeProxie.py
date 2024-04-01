import socket
from ..Settings import PY_PORT


class KeystrokeProxie:
    def __init__(self, host='127.0.0.1', port=PY_PORT):
        self.host = host
        self.port = port

    def send(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))  # Connect to receiver
            s.sendall(message.encode())  # Send the message
            result = s.recv(1024)  # Receive result

    def shutdown(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall("SHUTDOWN".encode())
            s.close()
