import serial
import time

arduinoData = serial.Serial('/dev/cu.usbserial-10', 115200)

while True:
    while(arduinoData.inWaiting()==0):
        pass

    dataPack=arduinoData.readline()
    dataPack =str(dataPack, 'utf', errors='ignore')
    dataPack = dataPack.strip('\r\n')
    splitPack = dataPack.split(",")
    
    print(splitPack)
    
    x = splitPack[0]