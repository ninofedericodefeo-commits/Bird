from BirdBrain import Finch
import time
import math
F = Finch()

def find_opening():
    d1 = 0
    d2 = 0
    count = 0
    angle_change = 5
    while True:
        count +=angle_change
        if abs(d1 - d2) > 10 and count > 10:
            break
        F.setTurn("R",angle_change,10)
        time.sleep(.1)
        d1=d2
        d2 = F.getDistance()
        print("d1: " + str(d1))
        print("d2: "+ str(d2))
    
find_opening()

F.stopAll()
