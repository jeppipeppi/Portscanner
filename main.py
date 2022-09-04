import socket
import sys


print("1 for IP, 2 for Website")
dec = str(input("1/2?: "))

if dec == "1":
    targetIP = raw_input("IP: ")

if dec == "2":
    target = raw_input("Link: ")
    targetIP = socket.gethostbyname(target)



try:
    for p in range(1, 45000):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = sock.connect_ex((targetIP, p))
        if res == 0:
            print("Open Port: " + str(p))
        sock.close()
except KeyboardInterrupt:
    print("\nClosing...")
    sys.exit()
except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()
except socket.error:
    print("\nNo response from server? Is the IP or link valid?")
    sys.exit()

diff = tend - tstart

print("Scan completed in " + str(diff))
