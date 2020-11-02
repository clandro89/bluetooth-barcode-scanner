import bluetooth
from imutils.video import VideoStream
from pyzbar.pyzbar import decode, ZBarSymbol
import time
import subprocess


print("[INFO] Starting video stream...")
vs = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
time.sleep(2.0)

host = ""
port = 1  # Raspberry Pi uses port 1 for Bluetooth Communication

# Creaitng Socket Bluetooth RFCOMM communication
server = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print('[INFO] Bluetooth Socket Created')

try:
    server.bind((host, port))
    print("[INFO] Bluetooth Binding Completed")
except:
    print("[INFO] Bluetooth Binding Failed")
server.listen(1)  # One connection at a time

while True:
    # BT Discoverable
    subprocess.call(['sudo', 'hciconfig', 'hci0', 'piscan'])

    # Server accepts the clients request and assigns a mac address.
    client, address = server.accept()
    print("[INFO] Connected To", address)
    print("[INFO] Client:", client)
    try:
        while True:
            # Get a frame
            frame = vs.read()

            # find the barcodes in the frame and decode each of the barcodes
            codes = decode(frame, symbols=[ZBarSymbol.QRCODE])

            for code in codes:
                # send qr code + ETX
                client.send(code.data.decode('utf-8') + "\x03")
    except:
        # Closing the client
        client.close()

