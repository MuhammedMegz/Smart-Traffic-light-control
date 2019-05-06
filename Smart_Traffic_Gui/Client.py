import socket
import sys
import errno
import fcntl, os

class SocketClient:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 50007
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))
        self.sock.setblocking(False)

    def read(self):
        try:
            data = self.sock.recv(16)
        except socket.error as e:
            err = e.args[0]
            if (err == errno.EAGAIN or err == errno.EWOULDBLOCK):
                return ""
            else:
                # a "real" error occurred
                print(e)
                sys.exit(1)
        else:
        # got a message, do something
            return data