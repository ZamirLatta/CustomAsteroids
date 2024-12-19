import time
from Arduino import Arduino

#get inputs: pin->button->anotherpin
#read input using serial in a loop
#import this file into asteroids to control inputs
#arduino = serial.Serial(baudrate=115200, timeout=.1)

S_IN = 2 # shoot input
T_IN = 3 # thrust input
R_IN = 4 # rotate clockwise input
L_IN = 5 # rotate counterclockwise input
H_IN = 6 # hyperspace input

S_S = 0
T_S = 0
R_S = 0
L_S = 0
H_S = 0

board = Arduino("9600", port="/dev/cu.usbserial-10")
#board.SoftwareSerial.write(" test ")

board.pinMode(S_IN, "INPUT")
board.pinMode(T_IN, "INPUT")
board.pinMode(R_IN, "INPUT")
board.pinMode(L_IN, "INPUT")
board.pinMode(H_IN, "INPUT")

while True:
    S_S = board.digitalRead(S_IN)
    T_S = board.digitalRead(T_IN)
    R_S = board.digitalRead(R_IN)
    L_S = board.digitalRead(L_IN)
    H_S = board.digitalRead(H_IN)

    if(S_S == 1):
        print("1")
        #time.sleep(1)
    elif (S_S == 0):
        print("n")
        #time.sleep(1)
    else:
        print("ERROR")

    if(T_S == 1):
        print("2")
        #time.sleep(1)
    elif (T_S == 0):
        print("n")
        #time.sleep(1)
    else:
        print("ERROR")

    if(R_S == 1):
        print("3")
        #time.sleep(1)
    elif (R_S == 0):
        print("n")
        #time.sleep(1)
    else:
        print("ERROR")

    if(L_S == 1):
        print("4")
        #time.sleep(1)
    elif (L_S == 0):
        print("n")
        #time.sleep(1)
    else:
        print("ERROR")

    if(H_S == 1):
        print("5")
        #time.sleep(1)
    elif (H_S == 0):
        print("n")
        #time.sleep(1)
    else:
        print("ERROR")