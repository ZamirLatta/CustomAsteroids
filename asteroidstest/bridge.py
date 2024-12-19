import time
import serial

arduinoData = serial.Serial('/dev/cu.usbserial-10', 115200)
time.sleep(1)

realCode = ["a", "b", "c", "d"]
inp_code = []
n = 0

#print(inp_code)

a = True
while a == True:
    while(arduinoData.inWaiting()==0):
        pass

    dataPack=arduinoData.readline()
    dataPack =str(dataPack, 'utf', errors='ignore')
    dataPack = dataPack.strip('\r\n')
    splitPack = dataPack.split(",")

    for chars in splitPack:
        if chars != "0":
            if (chars == "1"):
                inp_code.append("a")
            elif (chars == "2"):
                inp_code.append("b")
            elif (chars == "3"):
                inp_code.append("c")
            elif (chars == "4"):
                inp_code.append("d")
            elif (chars == "5"):
                inp_code.append("e")

            else: print("error")

    
    if len(inp_code) > 3:
        a = False

    
print(inp_code)

if inp_code == realCode:
    print("entry granted!")
else:
    print("entry denied!")
    

