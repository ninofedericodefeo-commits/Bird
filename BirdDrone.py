from BirdBrain import Finch
import time
import math
F = Finch()
F.setTurn("R",360,10)
def find_opening():
    dy = []
    dx = []
    count = 0
    angle_change = 5
    while True:
        count +=angle_change
        if count > 10 and (dx[-1]-dx[-2] > 10 or dy[-1] - dy[-2] > 10):
            break
        F.setTurn("R",angle_change,10)
        print("count: " + str(count))
        dx.append(F.getDistance()*math.cos(count))
        dy.append(F.getDistance()*math.sin(count))
        time.sleep(.1)
        print("distance: "+ str(F.getDistance()))
    return dx,dy
#dx,dy = find_opening()
print(dx)
print(dy)

F.stopAll()
