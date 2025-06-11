# 📂 Client and Server File Transfer using Python (Socket Programming)

This is a simple file transfer project where a **client sends a file to a server** using Python's `socket` module.  
I created this project to learn how socket communication and file transfer work in real time.

---

## 📁 Project Files

- `server.py` → Runs the server, receives files from the client.
- `client.py` → Sends a file to the server.
- `data.txt` → Sample file used for testing (sent by the client).
- `received_data.txt` → File saved by the server after receiving.

---

## 🚀 How to Run

### 1️⃣ First, open a terminal and run the server:
```bash
/usr/local/bin/python3.13 "/home/my/rajani maurya first assinment/server.py"
2️⃣ Then, split the terminal (or open a new one) and run the client:


/usr/local/bin/python3.13 "/home/my/rajani maurya first assinment/client.py"
3️⃣ Client will ask for a filename to send:


Enter the filename to send: data.txt
After this, the client will send the file, and the server will show:


Connected by (IP address, port)
File 'data.txt' received successfully.
⚙️ How the Code Works
🔹 server.py
Creates a server socket

Binds it to a host and port (e.g., localhost:5050)

Listens for client connections

Receives file and saves it

🔹 client.py
Creates a client socket

Connects to the server

Takes filename input from user

Reads file and sends to server

⚠️ Important Notes
Use the same port number in both client.py and server.py

Run the server first, then run the client

Uses Python’s built-in socket module

This code is for local machine or same network (LAN); not for internet transfer

🧠 Author
Rajani Maurya
Made for learning & practice 💻🌱
GitHub: @R69697









