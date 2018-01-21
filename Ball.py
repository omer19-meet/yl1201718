import turtle 
from turtle import*
colormode(255)
import random
import time

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r):
		Turtle.__init__(self)
		self.pu()
		self.x= xcor()
		self.y= ycor()
		self.dx= dx
		self.dy= dy
		self.r=r
		self.color=color
		self.shape("circle")
		self.shapesize = r/10

		r = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)

		self.color(r,g,b)


	def move(self, screen_w, screen_h):
		current_x = xcor()
		new_x = current_x+dx
		
		current_y  = ycor()
		new_y = current_y+dy

		right_s_ball = new_x+r
		left_s_ball  = new_x-r
		up_s_ball  = new_y+r
		down_s_ball = new_y-r

		Ball.goto(new_x,new_y)

		if right_s_ball > screen_w:
			self.dx = -dx
			Ball.goto(new_x,new_y)

		if left_s_ball < -screen_w:
			self.dx = -dx
			Ball.goto(new_x,new_y)

		if up_s_ball > screen_h:
			self.dy = -dy

		if down_s_ball < screen_h:
			self.dy = -dy

			

