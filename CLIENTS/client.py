import socket

HOST = "144.22.204.157" # IP Server Address
PORT = 8080 # Port to send requests

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    s.sendall(b"hello world")
    
    data = s.recv(1024)

print("Received", repr(data))