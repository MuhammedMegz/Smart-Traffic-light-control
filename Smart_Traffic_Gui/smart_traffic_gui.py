from tkinter import *
from Car import Car
from TrafficLight import TrafficLight
import trafficLightTimerHandler
from Client import SocketClient

canvas_width = 1260
canvas_height = 840

NS_trafficLightPos = [446, 148]
EW_trafficLightPos = [895, 529]

def loop():
    while 1:
        data = socket.read()
        if data != "":
            data = data.decode()
            data = data.split(",")
            if NS_trafficLight.getCurrentLight() == "G":
                turn = "NS"
            elif EW_trafficLight.getCurrentLight() == "G":
                turn = "EW"
            time = trafficLightTimerHandler.calcTime(int(data[0]), int(data[1]), turn)
            NS_trafficLight.setTimer(time)
            EW_trafficLight.setTimer(time)
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
NS_trafficLight = TrafficLight(canvas, NS_trafficLightPos)
EW_trafficLight = TrafficLight(canvas, EW_trafficLightPos)

#Start with NS road open
NS_trafficLight.changeToGreen()

#start the main loop
loop()

###################################################

