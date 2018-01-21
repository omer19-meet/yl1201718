import turtle
from turtle import *
from Ball import *
import random
import time

turtle.tracer(0)
turtle.ht()

RUNNING = True
SLEEP = 0.007777
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(0,0,5,7,10)

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS= 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5

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

def move_all_balls() :
	for i in range(NUMBER_OF_BALLS):
	new_ball.move(-300,300)

def collide(ball_1,ball_2):
	if ball_1 == ball_2:
		return False
	if ball_1.radius + ball_2.radius + 10 > math.sqrt(math.pow(ball_2.xcor()-ball_1.xcor()),2)+ math.pow((ball_2.ycor()-ball_1.ycor()),2):
		return True
	else:
		return False

def check_all_ball_collision():
	for ball_1 in BALLS :
		for ball_2 in BALLS:
			if collide(ball_1,ball_2):
				ball_1_radius = ball_1.r 
				ball_2_radius = ball_2.r
				screen_xpos = random.randint(int(-SCREEN_WIDTH+MAXIMUM_BALL_RADIUS), int(SCREEN_WIDTH- MAXIMUM_BALL_RADIUS))
				screen_ypos = random.randint(int(-SCREEN_HEIGHT+MAXIMUM_BALL_RADIUS), int(SCREEN_HEIGHT- MAXIMUM_BALL_RADIUS))
				ball_dx = random.randint(int(MINIMUM_BALL_DX), int(MAXIMUM_BALL_DX))
				ball_dy = random.randint(int(MINIMUM_BALL_DY), int(MAXIMUM_BALL_DY))
				ball_radius = random.randint(int(MINIMUM_BALL_RADIUS), int(MAXIMUM_BALL_RADIUS))
				if ball_1_radius<ball_2_radius:
					Ball_1(screen_xpos, screen_ypos, ball_dx,ball_dy, ball_radius)
					ball_2_radius +=1
				if ball_2_radius<ball_1_radius:
					Ball_2(screen_xpos, screen_ypos, ball_dx,ball_dy, ball_radius)
					ball_1_radius +=1
					



