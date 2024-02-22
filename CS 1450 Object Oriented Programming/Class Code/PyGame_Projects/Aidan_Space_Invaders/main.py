"""
A simple Galaga game I made for my Final Project.
Aidan Butcher
CS 1450 - Intro to OOP
2022-12-05
Todo: None.
Bugs: Some aliens are not being reset properly, I think it is due to the loops
      not finishing fast enough, outside of changing how I handled things, I'm
      not sure how to fix this.
"""

# Imports
import sys
from random import randrange, choice
import pygame as pg
from player import Player
from aliens import Bee, Moth, AlienShip
from projectiles import Projectile
import pygwidgets as pw

# Define Unchanging Constants
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 760
FRAMES_PER_SECOND = 90
SHIP_X = 600
SHIP_Y = 680
SHIP_WIDTH = 40
SHIP_HEIGHT = 45
SHIP_LIVES = 3
BEE_X = 500
BEE_Y = 200
BEE_WIDTH = 42
BEE_HEIGHT = 42
MOTH_X = 500
MOTH_Y = 150
MOTH_WIDTH = 42
MOTH_HEIGHT = 41
ASHIP_WIDTH = 44
ASHIP_HEIGHT = 44
ASHIP_X = 500
ASHIP_Y = 100
# BOSS_WIDTH = 44
# BOSS_HEIGHT = 47
# BOSS_X = 0
# BOSS_Y = 130
BULLET_WIDTH = 5
BULLET_HEIGHT = 5
ALIEN_HEALTH = 1
RESTART_TEXT = "Restart?"
QUIT_TEXT = "Quit?"
NUM_PROJ = 20
PROJ_CD = 500  # Cooldown for firing projectiles in ms.
POINTS = 0
MAX_POINTS = 150

# Initialize pygame, surface/window, and a clock for the fps
pg.init()
window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pg.time.Clock()

# Load in assets(images, sounds, etc.)
bg = pg.image.load("images/space_background.jpg")
bg = pg.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

ship = pg.image.load("images/ship.png")
ship = pg.transform.scale(ship, (80, 80))

alien_bee = pg.image.load("images/alien_bee.png")
alien_bee = pg.transform.scale(alien_bee, (40, 40))

alien_moth = pg.image.load("images/alien_moth.png")
alien_moth = pg.transform.scale(alien_moth, (40, 40))

alien_ship = pg.image.load("images/alien_ship.png")
alien_ship = pg.transform.scale(alien_ship, (40, 40))

bullet = pg.image.load("images/bullet.png")
bullet = pg.transform.scale(bullet, (10, 25))

# alien_boss = pg.image.load("images/alien_boss.png")
# alien_boss = pg.transform.scale(alien_boss, (60, 60))

fire_sound = pg.mixer.Sound("sounds/firing_sound.mp3")
adeath_sound = pg.mixer.Sound("sounds/alien_death_sound.mp3")
shipdeath_sound = pg.mixer.Sound("sounds/ship_death.mp3")

game_music = pg.mixer.Sound('music/arcade_night.mp3')
game_music.set_volume(0.3)
menu_music = pg.mixer.Sound('music/nebula.mp3')
menu_music.set_volume(0.3)

restart_button = pw.TextButton(window, (550, 10), RESTART_TEXT, 60, 20)
quit_button = pw.TextButton(window, (625, 10), QUIT_TEXT, 40, 20)

points_text = pw.DisplayText(window, (10, 10), fontSize=25, textColor=WHITE)
lives_text = pw.DisplayText(window, (WINDOW_WIDTH - 75, 10), fontSize=25,
                            textColor=WHITE)
controls_text = pw.DisplayText(window, (450, 30), fontSize=25, textColor=WHITE)
victory_text = pw.DisplayText(window, (500, 380), fontSize=25, textColor=WHITE)

# Initialize variables
player_ship = Player(window, (600, 670), (SHIP_WIDTH, SHIP_HEIGHT), ship,
                     SHIP_LIVES)

# pylint: disable=consider-using-dict-items
alien_dict = {}

for i in range(3):
    column_dict = {}
    for j in range(5):
        if i == 0:
            o_aship = AlienShip(window, (ASHIP_X + j * 50, ASHIP_Y),
                                (ASHIP_WIDTH, ASHIP_HEIGHT),
                                alien_ship, ALIEN_HEALTH)
            #column_dict[j] = [o_aship, 'a']
            column_dict[j] = [o_aship]
        if i == 1:
            o_moth = Moth(window, (MOTH_X + j * 50, MOTH_Y),
                          (MOTH_WIDTH, MOTH_HEIGHT),
                          alien_moth, ALIEN_HEALTH)
            #column_dict[j] = [o_moth, 'a']
            column_dict[j] = [o_moth]
        if i == 2:
            o_bee = Bee(window, (BEE_X + j * 50, BEE_Y),
                        (BEE_WIDTH, BEE_HEIGHT),
                        alien_bee, ALIEN_HEALTH)
            #column_dict[j] = [o_bee, 'a']
            column_dict[j] = [o_bee]
    alien_dict[i] = column_dict

# proj = Projectile(window, (100, 100), (10, 25), bullet, 'd')
last_fire = pg.time.get_ticks()
proj_list = []
for i in range(NUM_PROJ):
    o_proj = Projectile(window, window.get_size(), (10, 25), bullet, 'd',
                        PROJ_CD)
    proj_list.append(o_proj)

game_music.play(-1)
points_text.setValue(f"Points: {POINTS}")
lives_text.setValue(f"Lives: {player_ship.get_lives()}")
controls_text.setValue("Press 'A' and 'D' to move and 'Space' to fire.")

# While loop to keep the program running until it is told to close
GAME_FLAG = True
while True:
    # Check to see if the user is attempting to close the game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if quit_button.handleEvent(event):
            pg.quit()
            sys.exit()
        if restart_button.handleEvent(event):
            dir_list = ['r', 'l']
            dir_choice = choice(dir_list)
            game_music.fadeout(1000)
            menu_music.fadeout(1000)
            game_music.play(-1)
            player_ship.set_lives(SHIP_LIVES)
            for proj in proj_list:
                proj.reset_loc()
            for key in alien_dict:
                for key2 in alien_dict[key]:
                    alien_dict[key][key2][0].reset(dir_choice)
                    #alien_dict[key][key2][1] = 'a'
            GAME_FLAG = True
            POINTS = 0
            points_text.setValue(f"Points: {POINTS}")
            lives_text.setValue(f"Lives: {player_ship.get_lives()}")

    # Most of the game's logic is in this if block.
    if GAME_FLAG:
        if POINTS == MAX_POINTS:
            GAME_FLAG = False
            victory_text.setValue("Congratulations! You won!")
        key_pressed_tuple = pg.key.get_pressed()    
        for key in alien_dict:
            for key2 in alien_dict[key]:
                alien = alien_dict[key][key2][0]
                alien_dict[key][key2][0].side_movement()
                for proj in proj_list:
                    if alien.handle_collision(proj.get_rect()):
                        # Used instead of reset() because of random alien death
                        proj.set_loc((window.get_width() + 50,
                                      window.get_height() + 50))
                        proj.set_rect_loc(proj.get_loc())
                        if alien.get_health() == 0:
                            alien.set_loc((window.get_width() + 50, 0))
                            adeath_sound.play()
                            alien.set_rect_loc(alien.get_loc())
                            POINTS += 10
                            points_text.setValue(f"Points: {POINTS}")
                if player_ship.handle_collision(alien.get_rect()):
                    alien.set_health = 0
                    alien.set_loc((window.get_width() + 50, 0))
                    adeath_sound.play()
                    alien.set_rect_loc(alien.get_loc())
                    POINTS += 10
                    points_text.setValue(f"Points: {POINTS}")
                    lives_text.setValue(f"Level: {player_ship.get_lives()}")
                    victory_text.setValue("Defeat! The aliens have defeated"
                                          + " you!")

    # Everything involving firing projectiles.
        player_ship.movement(key_pressed_tuple)
        if key_pressed_tuple[pg.K_SPACE]:
            now = pg.time.get_ticks()
            proj_choice = randrange(0, NUM_PROJ)
            if not proj_list[proj_choice].get_moving():
                if now - last_fire >= PROJ_CD:
                    last_fire = now
                    player_loc = player_ship.get_loc()
                    proj_list[proj_choice].set_direction('u')
                    proj_list[proj_choice].fire((player_loc[0] + 33,
                                                 player_loc[1] - 20))
                    fire_sound.play()
        for proj in proj_list:
            proj.movement()
        if player_ship.get_lives() <= 0:
            shipdeath_sound.play()
            GAME_FLAG = False
            game_music.fadeout(1000)
            menu_music.play(-1)

    # Reset the display
    window.fill(BLACK)

    # Draw all images to the surface/window
    window.blit(bg, (0, 0))
    restart_button.draw()
    quit_button.draw()
    points_text.draw()
    controls_text.draw()
    lives_text.draw()
    player_ship.draw()
    for proj in proj_list:
        proj.draw()
    for key in alien_dict:
        for key2 in alien_dict[key]:
            if alien_dict[key][key2][0].get_health() > 0:
                alien_dict[key][key2][0].draw()
    if not GAME_FLAG:
        victory_text.draw()

    # Update the display
    pg.display.update()

    # Link the game to the fps
    clock.tick(FRAMES_PER_SECOND)
