# PORT SCANOTRON 9000 (working title, patent pending)
# Made by Caleb Brewer
# Started 12/17/20, ended 12/26/20
# Tested on 172.104.20.135

import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('cls', shell=True)
# Clear portscan-log
with open("portscan-log.txt", 'w') as log:
    log.write("")

# Ask for input and get variables
Server = input("Enter a remote host to scan: ")
ServerIP = socket.gethostbyname(Server)

# Print start time, save it as a variable for later
t1 = datetime.now()
print("\nStarting scan at ", t1)

# Nice and fancy divide between code
print("-" * 60)
print("Please wait, scanning host", ServerIP)
print("-" * 60)

# Scans every port from 1 to 1025, prints port as needed
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(.1)    # Speed things up a bit
        result = sock.connect_ex((ServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
            with open("portscan-log.txt", 'a') as log:  # Write open ports to log
                log.seek(0, 2)
                log.write("Port " + str(port) + ": Open\n")
                log.close()
        sock.close()

# Handle any errors and write to log
except socket.gaierror:
    print('Hostname could not be resolved. Exiting.')
    with open("portscan-log.txt", 'w') as log:
        log.seek(0, 2)
        log.write("Hostname could not be resolved.\n")
        log.close()
    sys.exit()
except socket.error:
    print("Couldn't connect to server. Exiting.")
    with open("portscan-log.txt", 'w') as log:
        log.seek(0, 2)
        log.write("Couldn't connect to server.\n")
        log.close()
    sys.exit()

# Print end time and save as variable for later
t2 = datetime.now()
print("\nEnded scan at ", t2)

# Define a variable for the total amount of time
total = t2 - t1

# Print scan time
print('Elapsed time of scan: ', total)

# Write details to log
with open("portscan-log.txt", 'a') as log:
    log.seek(0, 2)
    log.write('Scan started at: ' + str(t1) + '\n')
    log.write('Scan ended at: ' + str(t2) + '\n')
    log.write('Total elapsed time: ' + str(total))
    log.close()
