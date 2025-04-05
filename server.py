import socket
import os

from dotenv import load_dotenv

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

load_dotenv()
mac_address = str(os.getenv("SERVER_BLT_MAC"))
server.bind((mac_address, 4)) #using bluetooth port MAC address
server.listen(1) #only allows one connection at a time

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter Message")
        client.send(message.encode('utf-8'))

except OSError as e:
    pass

client.close()
server.close()