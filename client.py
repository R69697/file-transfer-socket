# client.py
import socket
import os

HOST = 'localhost'
PORT = 5050

def send_file(sock, filename):
    if not os.path.exists(filename):
        print(f"[x] File not found: {filename}")
        return

    file_size = os.path.getsize(filename)
    header = f"{filename}||{file_size}"
    header_bytes = header.encode()
    header_len = len(header_bytes)

    print(f"[>] Sending: {filename} ({file_size} bytes)")

    # Send header length (4 bytes)
    sock.sendall(header_len.to_bytes(4, byteorder='big'))
    # Send header
    sock.sendall(header_bytes)

    # Send file content
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            sock.sendall(chunk)

    print(f"[✓] File '{filename}' sent successfully.\n")

def main():
    filenames = input("Enter file names to send (comma-separated): ").split(",")

    client_socket = socket.socket()
    try:
        client_socket.connect((HOST, PORT))
        print(f"[+] Connected to server at {HOST}:{PORT}")

        for file in filenames:
            file = file.strip()
            if file:
                send_file(client_socket, file)

        # Send END marker
        end_header = "END".encode()
        client_socket.sendall(len(end_header).to_bytes(4, byteorder='big'))
        client_socket.sendall(end_header)

    except Exception as e:
        print(f"[x] Error: {e}")
    finally:
        client_socket.close()
        
        

if __name__ == "__main__":
    main()  
