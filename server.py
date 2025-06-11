import socket

# Server setup
host = '0.0.0.0'  # Listen on all interfaces
port = 5050

server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(1)
print(f" Server is listening on port {port}...")

conn, addr = server_socket.accept()
print(f" Connected by {addr}")

# Receive filename
filename = conn.recv(1024).decode()
with open(f"received_{filename}", "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print(f" File '{filename}' received successfully.")
conn.close()
server_socket.close()


