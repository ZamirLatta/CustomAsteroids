import serial
import time
from Arduino import arduino

'''
get inputs: pin->button->anotherpin
read input using serial in a loop
import this file into asteroids to control inputs
'''

S_IN = 2
T_IN = 3
S_IN = 4
T_IN = 5
A_IN = 6

S_OUT = 2
T_OUT = 3
R_OUT = 4
L_OUT = 5
A_OUT = 6

board = Arduino()
