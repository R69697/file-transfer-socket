# Client and Server File Transfer using Python


This is simple file transfer project. In this project, client send file to server using socket in python. I made this for learning socket and how real file sending working.

---

# Files in Project

`server.py` → this file for server side, it receive file from client
`client.py` → this send file to server
`data.txt` → this is example file which I send
`received_data.txt` → when server receive file, it make this file

# How to Run

# 1. First open terminal and run server
 /usr/local/bin/python3.13 "/home/my/rajani maurya first assinment/server.py"

# 2. and again split the terminal and run client
/usr/local/bin/python3.13 "/home/my/rajani maurya first assinment/client.py"

# 3. Client will ask filename, you type

Enter the filename to send: data.txt

then our data is send to server and server responces connected by (ip address and temp port no) and "File received" with file name 



How Code Work
server.py
it create server socket
bind with host and port (I used localhost and 5002)
wait for client
when client connect, receive file and save


client.py
create client socket
connect to server
ask file name from user
open file and send to server

Important
use same port number in both client and server
first run server then client
socket module used
this code not for internet, only same PC or same network


