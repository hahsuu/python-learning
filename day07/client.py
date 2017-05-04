import socket

host_port = ('127.0.0.1', 9999)

sk = socket.socket()
sk.connect(host_port)

sk.sendall('请占领地球'.encode())

server_reply = sk.recv(1024)

print(server_reply.decode())
while True:
    user_input = input('>>').strip()
    sk.send(user_input.encode())
    server_reply = sk.recv(1024)
    print(server_reply.decode())
sk.close()