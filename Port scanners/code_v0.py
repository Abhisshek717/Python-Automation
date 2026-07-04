# Checks whether the port is open or closed or ignored for the specific domain
import socket
import time

host = input("Enter domain name: ")
port = int(input("Enter port number: "))
ip = socket.gethostbyname(host)
connectionRefused = False
timeout = False

# Validating the port if it comes under the range 0 - 65535
if (port >= 0 and port <= 65535):
        print("port number is valid")
        # Resolving the DNS
        print(f"{host}:{ip}")
        # Creating a tcp socket
        tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # time: start point
        startPoint = time.perf_counter()
        try:
                tcpSock.connect((ip, port))
        except  ConnectionRefusedError:
                connectionRefused = True
        except  TimeoutError:
                print("Connection timed out")
        # time: end point
        endPoint = time.perf_counter()

        # measure the time duration in seconds. to get milliseconds multiply coutnDuration (value) with 1000
        countDuration = endPoint - startPoint

        if(connectionRefused == True):
                print("connection is refused")
        else:
                print("Port is open")
                print(f"timetaken: {countDuration*1000:.6f} ms")

        tcpSock.close()
