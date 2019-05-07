from tkinter import *
from Car import Car
from TrafficLight import TrafficLight
import trafficLightTimerHandler
from Client import SocketClient

canvas_width = 1260
canvas_height = 840

NS_trafficLightPos = [446, 148]
EW_trafficLightPos = [895, 529]

NS_carPos = [666, 834]
EW_carPos = [1243, 354]

def loop():
    while 1:
        data = socket.read()
        if data != "":
            data = data.decode()
            data = data.split(",")
            print("#############################")
            print("Received: NS: " + data[0] + " EW: " + data[1])
            if NS_trafficLight.getCurrentLight() == "G":
                turn = "NS"
            elif EW_trafficLight.getCurrentLight() == "G":
                turn = "EW"
            time = trafficLightTimerHandler.calcTime(int(data[0]), int(data[1]), turn)
            if time != "no change":
                if not NS_trafficLight.updated:
                    print("Reseting traffic light timer from " + str(NS_trafficLight.timer) + " to " + str(time))
                    NS_trafficLight.setTimer(time)
                    EW_trafficLight.setTimer(time)
                else:
                    print("Already updated in this turn!")
            else:
                print("No change.")
        master.update()
        master.update_idletasks()


#######################Init##################
master = Tk()

socket = SocketClient()

#Create canvas
canvas = Canvas(master, width=canvas_width, height=canvas_height)
canvas.pack(expand=YES, fill=BOTH)

#Load and insert road image into the canvas
roadImg = PhotoImage(file="photos/road.png")
canvas.create_image(0,0, anchor=NW, image=roadImg)

#Load and insert traffic lights images
NS_trafficLight = TrafficLight(canvas, NS_trafficLightPos, NS_carPos, "NS")
EW_trafficLight = TrafficLight(canvas, EW_trafficLightPos, EW_carPos, "EW")

#Start with NS road open
NS_trafficLight.changeToGreen()

#start the main loop
loop()

###################################################

