
from turtle import*
import turtle
import random
import math
import time
colormode(255)


# RANDOM COLOR:
	# def ran_col(self):
	# 	r = random.randint(0,255)
	# 	g = random.randint(0,255)
	# 	b = random.randint(0,255)
	# 	self.color((r,g,b))
	# 	turtle.shape(Shape)
	# 	turtle.pencolor(pencolor)

	# 	self.omer = Square(20, Square)

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
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.radius = radius

	def jump(self):
		self.goto(self.pos_x+100, self.pos_y-100)
		print("I'M JUMMPIN' TO THE S K Y !     "*10)


	def ran_col(self):
			r = random.randint(0,255)
			g = random.randint(0,255)
			b = random.randint(0,255)
			self.color((r,g,b))
			print(r,g,b)
			self.shape()
			# self.pencolor(pencolor)
	

c1 = ball(5, "yellow", 15, 0, 15)
c2 = ball(3, "blue", 20, 15, 15)

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
	return dis

def check_col(c1, c2):
	if c1.radius+c2.radius < dist(c1,c2) : 
		print(" DANGER! the balls r collaiding!!!             "*50)
		c1.ran_col()
		time.sleep(3)
		c2.ran_col()
		c1.jump()
	else:
		print(" KALLLLLLLLL ")

check_col(c1, c2)

mainloop()
