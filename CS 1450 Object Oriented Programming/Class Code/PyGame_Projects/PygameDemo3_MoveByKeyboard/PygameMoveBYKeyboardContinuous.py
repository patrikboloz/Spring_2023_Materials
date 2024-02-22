#pygame demo 3b - one image, move by keyboard continuously

# 1 - Import packages
import pygame
import sys
from pygame.locals import *
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 920
FRAMES_PER_SECOND = 30
BALL_WIDTH_HEIGHT = 300
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 10

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image, sound, etc.
ballImage = pygame.image.load('images/ball.png')
targetImage = pygame.image.load('images/target.jpg')


# 5 - Initialize variables
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)


# 6 - Loop forever
while True:

	# 7 - Check for and handle events
	for event in pygame.event.get():
		#Clicked the close button? Quit pygame and end the program
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


	# 8 - Do any "frame" actions
	keyPressedTuple = pygame.key.get_pressed()

	if keyPressedTuple[pygame.K_LEFT]:
		ballX = ballX - N_PIXELS_TO_MOVE
	if keyPressedTuple[pygame.K_RIGHT]:
		ballX = ballX + N_PIXELS_TO_MOVE
	if keyPressedTuple[pygame.K_UP]:
		ballY = ballY - N_PIXELS_TO_MOVE
	if keyPressedTuple[pygame.K_DOWN]:
		ballY = ballY + N_PIXELS_TO_MOVE


	#Check if the ball is colliding with the target
	ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
	if ballRect.colliderect(targetRect):
		print("Ball is touching the target.")

	# 9 - Clear the window
	window.fill(BLACK)

	# 10 - Draw all window elements
	window.blit(ballImage, (ballX, ballY)) #draw a ball at position 100 across x and 200 down y
	window.blit(targetImage, (TARGET_X, TARGET_Y))


	# 11 - Update the window
	pygame.display.update()

	# 12 - Slow things down a bit
	clock.tick(FRAMES_PER_SECOND)