from dotenv import load_dotenv

import socket
import os

client = socket.soket(socket.AF_BLUETOOTH, socket.SOCK_DGRAM, socket.BTPROTO_RFCOMM)

load_dotenv()
mac_address = string(os.getenv("SERVER_BLT_MAC"))
client.connect((mac_address), 4)

try:
    while True:
        message = input("enter message")

        client.send(message.encode('utf-8'))

        data = client.recv(1024)

        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")

except OSError as e:
    pass

client.close()