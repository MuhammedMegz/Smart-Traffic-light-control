from tkinter import *

class Car:
    def __init__(self, canvas, startPos, orientaion):
        self.carImg = PhotoImage(file="photos/car.png")
        self.startPos = startPos
        self.canvas = canvas
        self.carID = self.canvas.create_image(startPos[0], startPos[1], anchor=NE, image=self.carImg, state=HIDDEN)
        self.isMoving = False
        self.orientaion = orientaion

    def move(self):
      self.isMoving = True
      self.moveLoop()

    def stop(self):
      self.isMoving = False
      self.canvas.itemconfig(self.carID, state=HIDDEN)

    def moveLoop(self):
      self.canvas.move(self.carID, -50, 0)
      if self.canvas.coords(self.carID)[0] < 0:
        self.canvas.move(self.carID, self.startPos[0], 0)
      if self.isMoving:
        self.canvas.itemconfig(self.carID, state=NORMAL)
        self.canvas.after(50, self.moveLoop)