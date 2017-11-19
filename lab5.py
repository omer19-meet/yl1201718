from turtle import*
import turtle
colormode(255)
import random



class Square(Turtle):
	"""docstring for Square"""
	def __init__(self, size):
		self.Shape = shape("square")
		self.size = size
		self.pencolor = pencolor(random())
	def ran_col():
		turtle.shape(Shape)
		turtle.pencolor(pencolor)

		#self.omer = Square(20, Square)
omer = Square(20)
ran_col()

turtle.mainloop()




		