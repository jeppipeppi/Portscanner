from shutil import ExecError
import socket
import subprocess
import sys
from datetime import datetime

target = "scanme.nmap.org"
targetIP = socket.gethostbyname(target)

tstart = datetime.now()

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

tend = datetime.now()
diff = tend - tstart

print("Scan completed in " + str(diff))