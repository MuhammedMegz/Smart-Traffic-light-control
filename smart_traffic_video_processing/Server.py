import socket

class SocketServer:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 50007
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()

    def send(self, data):
        self.conn.send(data.encode())


    def close(self):
        self.sock.close()
