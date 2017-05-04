import  sys


class WebServer(object):
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def start(self):
        print('webserver is starting...')

    def stop(self):
        print('webserver is stop.. ')

    def restart(self):
        print('webserver is restarting...')


if __name__ == '__main__':
    server = WebServer('127.0.0.1', 8888)

    if hasattr(server, sys.argv[1]):
        func = getattr(server, sys.argv[1])
        func()