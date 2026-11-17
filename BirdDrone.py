from BirdBrain import Finch
import time

myFinch = Finch()

def dfs():
    for i in range(10):
        myFinch.setTurn("L",10,10)
        d = myFinch.getDistance()
        print(d)
dfs()

myFinch.playNote(60,0.5)
while myFinch.getDistance() > 25:
    print(myFinch.getDistance())
    myFinch.setMotors(50,50)
myFinch.stop()
myFinch.getDistance()
time.sleep(10)

myFinch.setTurn("R",90,1)

myFinch.stopAll()
