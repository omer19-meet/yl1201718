from turtle import*
import turtle

import random

colormode(255)

# class Square(Turtle):
# 	"""docstring for Square"""
# 	def __init__(self, size):
# 		Turtle.__init__(self)
# 		self.shape("square")
# 		self.size = (size)
# 		self.pencolor =()

# 	def ran_col(self):
# 		r = random.randint(0,255)
# 		g = random.randint(0,255)
# 		b = random.randint(0,255)
# 		self.color((r,g,b))
# #		turtle.shape(Shape)
# #		turtle.pencolor(pencolor)

# 		#self.omer = Square(20, Square)
# omer = Square(20)
# omer.ran_col()

# print(Square)

# mainloop()

class Rectangel(Turtle):
	
	def __init__(self, width, height):
		Turtle.__init__(self)
		register_shape("rectangel",((0,0) ,(int(width),0) ,(int(width),int(height)),(0,int(height)), (0,0)))
		self.shape("rectangel")
		self.setheading(179)
		# self.width = width
		# self.height = height
		# width = w
		# height = h
class Square(Rectangel):
	def __init__(self,width):
		Rectangel.__init__(self,width,width)

	def fill_col(self,collor):
		Rectangel.color(collor)

she1 = Rectangel(100,30)

gassan = Square(30)
gassan.fill_col(yellow)
mainloop()











