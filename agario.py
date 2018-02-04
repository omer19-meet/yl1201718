import turtle
from turtle import *
from Ball import *
import random
import time
import math

turtle.tracer(0)
turtle.ht()
getscreen().setup(1.0,1.0)
RUNNING = True
SLEEP = 0.007777
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

# INSTRUCTIONS:    									--------------------------------
asd = turtle.clone()
asd.ht()
asd.pu()
asd.goto(-150,150)
asd.write("welcom to omer's Agario game!!!", move=True, align='left', font=('Arial',50,'bold'))

asd.write("U know how to play, no need in long explanation")
time.sleep(2)
asd.clear()

asd.goto
MY_BALL = Ball(-200,200,0,0,15)

SCORE = 0

NUMBER_OF_BALLS = 10
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS= 40
MINIMUM_BALL_DX = -3
MAXIMUM_BALL_DX = 3
MINIMUM_BALL_DY = -3
MAXIMUM_BALL_DY = 3

 ## LISTS-------------------------------------------------

BALLS = []

## MAKE BALLS RANDOMLY: ----------------------------------

for i in range(NUMBER_OF_BALLS):
	screen_xpos = random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH- MAXIMUM_BALL_RADIUS))
	screen_ypos = random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT- MAXIMUM_BALL_RADIUS))
	ball_dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
	ball_dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))
	ball_radius = random.randint(int(MINIMUM_BALL_RADIUS), int(MAXIMUM_BALL_RADIUS))
	new_ball = Ball(screen_xpos, screen_ypos, ball_dx,ball_dy, ball_radius)
	BALLS.append(new_ball)

def move_all_balls():
	for new_ball in BALLS:
		new_ball.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_1,ball_2):
	if ball_1 == ball_2:
		return False
	D = math.sqrt(math.pow(ball_2.xcor()-ball_1.xcor(),2)+ math.pow(ball_2.ycor()-ball_1.ycor(), 2))
	# print(D, ball_1.radius + ball_2.radius )
	if ball_1.radius + ball_2.radius >= D + 10 :
		# print("colided")
		return True

	else:
		return False

def check_all_ball_collision():
	for ball_1 in BALLS :
		for ball_2 in BALLS:
			if collide(ball_1,ball_2):
				ball_1_radius = ball_1.radius 
				ball_2_radius = ball_2.radius
				screen_xpos = random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH- MAXIMUM_BALL_RADIUS))
				screen_ypos = random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT- MAXIMUM_BALL_RADIUS))
				ball_dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))

				while ball_dx == 0:
					ball_dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
				ball_dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))
				while ball_dy==0:
					ball_dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))

				ball_radius = random.randint(int(MINIMUM_BALL_RADIUS), int(MAXIMUM_BALL_RADIUS))
				if ball_1_radius<ball_2_radius:
					#Ball_1(screen_xpos, screen_ypos, ball_dx,ball_dy, ball_radius)
					ball_1.goto(screen_xpos, screen_ypos)
					ball_1.dx = ball_dx
					ball_1.dy = ball_dy
					ball_1.radius = ball_radius
					ball_1.shapesize(ball_radius/10)
					ball_2.radius +=1
					ball_2.shapesize(ball_2.radius/10)

				if ball_2_radius<ball_1_radius:
					#Ball_2(screen_xpos, screen_ypos, ball_dx,ball_dy, ball_radius)
					ball_2.goto(screen_xpos, screen_ypos)
					ball_2.dx = ball_dx
					ball_2.dy = ball_dy
					ball_2.radius = ball_radius
					ball_2.shapesize(ball_radius/10)

					ball_1.radius +=1
					ball_1.shapesize(ball_1.radius/10)
					
def check_myball_collision():
	#creat RANDOM ATRREBUITS: --------------------------------------------------
	screen_xpos = random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH- MAXIMUM_BALL_RADIUS))
	screen_ypos = random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT- MAXIMUM_BALL_RADIUS))
	
	ball_dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
	while ball_dx==0:
		ball_dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
	ball_dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))
	while ball_dy==0:
		ball_dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))

	ball_radius = random.randint(int(MINIMUM_BALL_RADIUS), int(MAXIMUM_BALL_RADIUS))
	
	for otherball in BALLS :
		if collide(MY_BALL, otherball):
			print("collided")
			my_ball_radius = MY_BALL.radius
			otherball_radius = otherball.radius

			if my_ball_radius<otherball_radius:
				global SCORE
				print("game OVER")
				clear()
				pu()
				goto(200,0)
				write("game OVER", align='right', font=('Ariel', 50,'bold'))
				pu()
				goto(180,-50)
				write("your final score:"+str(SCORE), align='right', font=('Arial',20,'normal'))

				return False
			
			else:
				MY_BALL.radius +=1
				
				clear()
				global SCORE
				SCORE +=1
				pu()
				goto(-250,150)
				write(SCORE , align='right', font=('Arial',20, 'normal'))

				MY_BALL.shapesize(MY_BALL.radius/10)

				otherball.goto( screen_xpos, screen_ypos)
				otherball.dx = ball_dx
				otherball.dy = ball_dy
				otherball.radius= ball_radius
				otherball.shapesize(otherball.radius/10)
	return True

def movearound(event):
	MY_BALL.goto(event.x- SCREEN_WIDTH, SCREEN_HEIGHT-event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.getscreen().listen()
# for i in range(200000000):
# 	move_all_balls()
# 	print('hey')
# 	getscreen().update()
while RUNNING==True:
	
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2 :
		SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2

	if SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2 :
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

	move_all_balls()
	check_all_ball_collision()

	MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	RUNNING = check_myball_collision()
	turtle.getscreen().update()
	time.sleep(SLEEP)

turtle.mainloop()