import socket

HOST = "10.0.0.243" # Loopback
PORT = 65123 #Ports greater than 1023 are Listening

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