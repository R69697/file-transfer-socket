# 🔁 Multi-File Transfer System using Python Sockets

This is a **Client-Server File Transfer System** built using Python’s socket programming module. It allows smooth and reliable file transfer between two systems connected over the same **Wi-Fi LAN** network.

The project supports different file formats and accurately handles data transmission using file size detection.

---

## ⚙️ Features

- 📡 Real-time file transfer over a LAN connection  
- 📁 Supports multiple file formats: `.txt`, `.pdf`, `.json`, `.csv`, `.jpg`, etc.  
- 📦 Sends and receives files with correct size tracking  
- 🧵 Multi-threaded handling for efficient performance  

---

## 🛠️ Tech Stack

- **Python 3.13**
- **Socket Programming**
- **Threading**
- **Linux (tested)**

---

## 📁 Project Files

- `server.py` → Starts the server and receives files  
- `client.py` → Sends files to the server  
- `data.txt` → Sample file sent by the client  
- `received_data.txt` → File saved by the server after receiving

---

## 🚀 How to Run

### 1️⃣ First, open a terminal and run the server:
```bash
/usr/local/bin/python3.13 "/home/my/rajani maurya first assinment/server.py"

2️⃣ Then, open a new terminal and run the client:

/usr/local/bin/python3.13 "/home/my/rajani maurya first assinment/client.py"

3️⃣ The client will ask for the filename:

Enter the filename to send: data.txt
✅ Once sent, the server will display:


Connected by (IP address, port)
File 'data.txt' received successfully.
⚙️ How the Code Works
🔹 server.py
Creates a socket and binds it to a host and port

Waits for client connection
Receives the file and saves it locally


🔹 client.py
Connects to the server

Takes a filename as input

Reads and sends the file content

⚠️ Notes
Use the same port number in both scripts

Always start the server first, then the client

Works only within the same local network

Uses Python’s built-in socket module — no external libraries needed

👩‍💻 Author
Rajani Maurya
Made with curiosity, practice, and a love for learning 💻🌱
GitHub: @R69697

