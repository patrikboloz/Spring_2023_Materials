#pygame demo 9 - SimpleText, SimpleButton, and Ball classes

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from SimpleButton import * #bring in the SimpleButton class
from Ball import * #bring in the Ball class
from SimpleText import * #bring in the SimpleText class

#2 - Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 960
FRAMES_PER_SECOND = 30

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: images sounds etc


# 5 - Initialize variables
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oRestartButton = SimpleButton(window, (280, 60), 'images/buttonUp.png', 'images/buttonDown.png')
oFrameCountLabel = SimpleText(window, (60, 20), "Program has run  through this many loops:", WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), " ", WHITE)
frameCounter = 0

# 6 - Loop forever
while True:

	# 7 - Check for and handle events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		#Pass the event to the button, see if it has been clicked on
		if oRestartButton.handleEvent(event):
			frameCounter = 0 # clicked button, reset the counter



	# 8 - DO any per frame actions
	oBall.update() # tell the ball to update itself
	frameCounter = frameCounter + 1
	oFrameCountDisplay.setValue(str(frameCounter))	

	# 9 - Clear the window befoire drawing it again
	window.fill(BLACK)

	# 10 - Draw the window elements
	oRestartButton.draw() #tell the Button to draw itself
	oFrameCountDisplay.draw()
	oFrameCountLabel.draw()
	oBall.draw()

	# 11 - Update the window
	pygame.display.update()

	#12 - Slow things down a bit
	clock.tick(FRAMES_PER_SECOND)