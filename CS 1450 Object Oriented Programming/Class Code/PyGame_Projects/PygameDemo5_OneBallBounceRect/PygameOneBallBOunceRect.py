#pygame demo 5 - one image, bounce around the window using rects

# 1 - Import packages
import pygame
import sys
from pygame.locals import *
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 960
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 15

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image, sound, etc.
ballImage = pygame.image.load('images/ball.png')


# 5 - Initialize variables

ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height

ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME


# 6 - Loop forever
while True:

	# 7 - Check for and handle events
	for event in pygame.event.get():
		#Clicked the close button? Quit pygame and end the program
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()



	# 8 - Do any "frame" actions

	if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
		xSpeed = -xSpeed # reverse X direction

	if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
		ySpeed = -ySpeed #reverse Y direction

	#Update the ball's location using the speed in two directions
	ballRect.left = ballRect.left + xSpeed
	ballRect.top = ballRect.top + ySpeed

	# 9 - Clear the window
	window.fill(BLACK)

	# 10 - Draw all window elements
	window.blit(ballImage, ballRect) #draw a ball at position 100 across x and 200 down y

	# 11 - Update the window
	pygame.display.update()

	# 12 - Slow things down a bit
	clock.tick(FRAMES_PER_SECOND)