import turtle 
from turtle import*
colormode(255)
import random

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,r,color,):
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
		self.color(color)


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

			

