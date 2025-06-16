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

How to Run
1. First open terminal and run server
/usr/local/bin/python3.13 "/home/my/rajani maurya first assinment/server.py"

2. and again split the terminal and run client
/usr/local/bin/python3.13 "/home/my/rajani maurya first assinment/client.py"

3. Client will ask filename, you type
Enter the filename to send: data.txt

then our data is send to server and server responces connected by (ip address and temp port no) and "File received" with file name

How Code Work server.py it create server socket bind with host and port (I used localhost and 5050) wait for client when client connect, receive file and save

client.py create client socket connect to server ask file name from user open file and send to server

Important use same port number in both client and server first run server then client socket module used this code not for internet, only same PC or same network


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

