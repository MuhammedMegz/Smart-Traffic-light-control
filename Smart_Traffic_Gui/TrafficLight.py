from tkinter import *
from Car import Car

class TrafficLight:
  def __init__(self, canvas, lightsposition, carPosition, direction):
      self.canvas = canvas

      self.trafficLightImage = []
      self.loadTrafficLightImages()

      self.lightsposition = lightsposition
      self.trafficLightImgID = self.canvas.create_image(self.lightsposition[0], self.lightsposition[1], anchor=NE, image=self.trafficLightImage[0])
      self.currentLight = "R"

      self.timer = 0
      self.timerLabel  = self.createTimerLabel()
      self.startTimer()

      self.car = Car(self.canvas, carPosition, direction)

      self.updated = False
      

  def createTimerLabel(self):
    timerLabel = Label(self.canvas, text = str(self.timer), font=("Impact", "20"))
    timerLabel.pack()
    self.canvas.create_window(self.lightsposition[0]-100, self.lightsposition[1]+75, window=timerLabel)
    return timerLabel

  def startTimer(self):
    self.timer = 60
    self.timerLabel.config(text=str(self.timer))
    self.canvas.after(1000, self.updateTimer)

  def updateTimer(self):
    if self.timer == 5:
      self.timer -= 1
      self.changeToYellow()
    elif self.timer == 0:
      self.timer = 60
      if self.currentLight == "R":
        self.changeToGreen()
      elif self.currentLight == "G":
        self.changeToRed()
    else:
      self.timer -= 1
    self.timerLabel.config(text=str(self.timer))
    self.canvas.after(1000, self.updateTimer)

  def setTimer(self, time):
    self.timer = time
    self.updated = True
    if self.currentLight == "R":
      self.changeToRed()
    elif self.currentLight == "G":
      self.changeToGreen()
      

  def loadTrafficLightImages(self):
    self.trafficLightImage.append(PhotoImage(file="photos/trafficLightsRed.png"))
    self.trafficLightImage.append(PhotoImage(file="photos/trafficLightsYellow.png"))
    self.trafficLightImage.append(PhotoImage(file="photos/trafficLightsGreen.png"))

  def changeToRed(self):
    self.canvas.itemconfig(self.trafficLightImgID, image=self.trafficLightImage[0])
    self.currentLight = "R"
    self.car.stop()
    

  def changeToYellow(self):
    self.canvas.itemconfig(self.trafficLightImgID, image=self.trafficLightImage[1])
    self.updated = False

  def changeToGreen(self):
    self.canvas.itemconfig(self.trafficLightImgID, image=self.trafficLightImage[2])
    self.currentLight = "G"
    self.car.move()

  def getCurrentLight(self):
    return self.currentLight
