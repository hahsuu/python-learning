import socket


host_port = ('127.0.0.1', 9999)
sk = socket.socket()
sk.bind(host_port)
sk.listen(5)

while True:
    print('server is waiting....')
    conn, addr = sk.accept()

    client_data = conn.recv(1024)
    print(client_data.decode())
    conn.send('不要回答，不要回答'.encode())

    conn.close()

