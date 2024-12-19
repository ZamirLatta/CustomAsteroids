from serial.tools import list_ports
import serial
import time
import csv

arduino = serial.Serial(port='/dev/cu.usbserial-10', baudrate=115200, timeout=.1)

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portlist = []

for port in ports:
    portlist.append(str(port))
    print(str(port))

'''val = input("select port: ")


for x in range(0,len(portlist)):
    if portlist[x].startswith("/dev/cu.usb" + str(val)):
        portVar = "/dev/cu.usb" + str(val)
        print(portlist[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
'''

f = open('data.csv',"w", newline='')
f.truncate

serialCom = serial.Serial('/dev/cu.usbserial-10', 115200)

'''while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode('utf '))'''

x = 4
#for num in range(x):
    
