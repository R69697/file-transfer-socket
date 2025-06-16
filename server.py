# server.py
import socket
import threading

HOST = '0.0.0.0'
PORT = 5050

def receive_exact(conn, size):
    """Receive exactly `size` bytes"""
    data = b""
    while len(data) < size:
        packet = conn.recv(size - len(data))
        if not packet:
            break
        data += packet
    return data

def handle_client(conn, addr):
    print(f"[+] Connected to {addr}")

    try:
        while True:
            # First 4 bytes = header length
            header_len_data = receive_exact(conn, 4)
            if not header_len_data:
                break

            header_len = int.from_bytes(header_len_data, byteorder='big')
            header_data = receive_exact(conn, header_len).decode()

            if header_data == "END":
                print(f"[✓] All files received from {addr}")
                break

            try:
                filename, file_size = header_data.split("||")
                file_size = int(file_size)
            except ValueError:
                print(f"[x] Invalid header received from {addr}: {header_data}")
                break

            print(f"[{addr}] Receiving: {filename} ({file_size} bytes)")
            file_data = receive_exact(conn, file_size)

            with open("received_" + filename, "wb") as f:
                f.write(file_data)

            print(f"[✓] Received '{filename}' from {addr} ({file_size} bytes)\n")

    except Exception as e:
        print(f"[x] Error: {e}")
    finally:
        conn.close()

def start_server():
    server_socket = socket.socket()
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"[+] Server started on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        print(f"[*] New connection from {addr}")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[=] Active connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()
