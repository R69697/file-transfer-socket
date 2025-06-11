import socket

host = 'localhost'
port = 5050  

# Create client socket
client_socket = socket.socket()

try:
    # Connect to the server
    client_socket.connect((host, port))
    print(f" Connected to server at {host}:{port}")
    
    
    filename = input("Enter the filename to send: ").strip()
    
    client_socket.send(filename.encode())
    
    with open(filename, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            client_socket.send(data)

    print(f" File '{filename}' sent successfully.")

except FileNotFoundError:
    print(" File not found. Please check the filename and try again.")
except ConnectionRefusedError:
    print("Server not running or port is wrong.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    client_socket.close()
