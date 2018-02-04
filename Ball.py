import turtle 
from turtle import*
colormode(255)
import random
import time

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius):
		Turtle.__init__(self)
		self.pu()
		# self.x= x
		# self.y= y
		self.goto(x,y)
		self.dx= dx
		self.dy= dy
		self.radius=radius
		self.shape("circle")
		self.shapesize(radius/10)

		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)

		self.color(r,g,b)


	def move(self, screen_w, screen_h):
		current_x = self.xcor()
		new_x = current_x+self.dx
		
		current_y  = self.ycor()
		new_y = current_y+self.dy

		right_s_ball = new_x+self.radius
		left_s_ball  = new_x-self.radius
		up_s_ball  = new_y+self.radius
		down_s_ball = new_y-self.radius

		self.goto(new_x,new_y)

		if right_s_ball >= screen_w:
			self.dx = self.dx*-1
			# Ball.goto(new_x,new_y)

		if left_s_ball <= -screen_w:
			self.dx = self.dx*-1
			# Ball.goto(new_x,new_y)

		if up_s_ball >= screen_h:
			self.dy = self.dy*-1

		if down_s_ball <= -screen_h:
			self.dy = self.dy*-1

			

