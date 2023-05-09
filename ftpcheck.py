#CHECK OPEN FTP SERVER
import ftplib
import socket

# Define the range of IP addresses to scan
start_ip = "localhost"
end_ip = "localhost"

# Define the FTP port number
ftp_port = 21

# Loop over each IP address in the range
for i in range(int(start_ip.split(".")[-1]), int(end_ip.split(".")[-1])+1):
    ip = start_ip.rsplit(".", 1)[0] + "." + str(i)
    print("Checking IP:", ip)

    try:
        # Connect to the FTP server
        ftp = ftplib.FTP()
        ftp.connect(ip, ftp_port)
        ftp.login()
        ftp.quit()
        
        # If we get here, the FTP server is open
        print("FTP server is open at", ip)

    except (socket.timeout, ftplib.error_perm):
        # If we get here, the FTP server is not open
        pass

