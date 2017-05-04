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
    while True:
        client_data = conn.recv(1024)
        print(client_data.decode())
        server_response = input('\033[32;1m>>:\033[0m').strip()
        conn.send(server_response.encode())

    conn.close()

