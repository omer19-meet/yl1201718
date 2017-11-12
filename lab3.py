import turtle
# turtle.addshape("redmeat.gif")
# turtle.shape("redmeat.gif")

# turtle.mainloop()
turtle.speed(1000)
for a in range(360):
	turtle.pendown()
	turtle.right(a+1)
	turtle.forward(100)
	turtle.right(50)
	turtle.forward(40)
	turtle.right(90)
	turtle.forward(20)
	turtle.penup()
	turtle.home()
	
turtle.mainloop()

