#DOMAIN AUTHORITY CHECKER FOR SEO/SEM MANAGERS
import socket

# Replace "example.com" with the website you want to check
website = "safepro.co.ke"

# Define a list of ports to check
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

# Loop through the ports and check if they are open
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((website, port))
    if result == 0:
        print(f"Port {port} is open")
        try:
            sock.sendall(b"HEAD / HTTP/1.1\r\nHost: " + website.encode() + b"\r\n\r\n")
            response = sock.recv(1024).decode()
            print(f"Connected to port {port} and server responded with:\n{response}")
        except:
            print(f"Failed to connect to port {port}")
    sock.close()

