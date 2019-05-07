from tkinter import *

class Car:
    def __init__(self, canvas, startPos, orientaion):
      if orientaion == "NS":
        self.carImg = PhotoImage(file="photos/carNS.png")
        self.step = [0, -10]
      elif orientaion == "EW":
        self.carImg = PhotoImage(file="photos/carEW.png")
        self.step = [-10, 0]
      self.startPos = startPos
      self.canvas = canvas
      self.carID = self.canvas.create_image(startPos[0], startPos[1], anchor=CENTER, image=self.carImg, state=HIDDEN)
      self.isMoving = False
      self.orientaion = orientaion

    def move(self):
      self.isMoving = True
      self.moveLoop()

    def stop(self):
      self.isMoving = False
      self.canvas.itemconfig(self.carID, state=HIDDEN)

    def moveLoop(self):
      self.canvas.move(self.carID, self.step[0], self.step[1])
      if self.canvas.coords(self.carID)[0] < 0:
        self.canvas.move(self.carID, self.startPos[0], 0)
      elif self.canvas.coords(self.carID)[1] < 0:
        self.canvas.move(self.carID, 0, self.startPos[1])
      if self.isMoving:
        self.canvas.itemconfig(self.carID, state=NORMAL)
        self.canvas.after(100, self.moveLoop)
