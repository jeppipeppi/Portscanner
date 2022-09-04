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
except Exception:
    print("Error")
    sys.exit()

diff = tend - tstart

print("Scan completed in " + str(diff))