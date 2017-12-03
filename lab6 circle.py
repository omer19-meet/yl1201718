
from turtle import*
import turtle
import random
import math

class ball(Turtle):
	def __init__( self, radius, color, speed, pos_x, pos_y):
		Turtle.__init__(self)
		self.penup()
		self.goto(pos_x,pos_y)
		self.pendown()
		self.shape("circle")
		self.shapesize(radius)
		self.color(color)
		self.speed(speed)
		self.Radius(radius)
		# self.turtle.goto(int(pos_x),int(pos_y))

	# def position():
	# 	turtle.goto((pos_x),(pos_y))


c1 = ball(5, "yellow", 15, 0, 15)
c2 = ball(3, "blue", 20, 133, 100)

pos_c1_ = []
pos_c2 = []

def dist( c1, c2 ):
	y1 = c1.ycor()
	x1 = c1.xcor()

	y2 = c2.ycor()
	x2 = c2.xcor()

##  the PITAGORAS equaitoin:
	dis = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
	print(dis)

def check_col(c1, c2):
	if c1.Radius+c2.Radius > dist() : 
		print(" DANGER! the balls r collaiding!!!")

dist(c1, c2)
check_col(c1, c2)
mainloop()
