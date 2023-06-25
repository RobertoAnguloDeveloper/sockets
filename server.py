import socket

HOST = "127.0.0.1" # Loopback
PORT = 8080 #Ports greater than 1023 are Listening

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        print(f"Connection established with {addr}:")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            conn.sendall(data)