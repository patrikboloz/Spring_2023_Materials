"""
Player class that will handle all player stuff.
Aidan Butcher
CS 1450 - Intro to OOP
2022-12-06
Todo: None.
Bugs: None.
"""

import pygame as pg


class Player():
    """Will handle all player movement and whatnot"""
    def __init__(self, window: pg.Surface, loc: tuple, width_height: tuple,
                 image: pg.Surface, lives: int):
        self.__window = window
        self.__loc = loc
        self.__xoff = 19  # X offset to properly fit rectangle
        self.__yoff = 11  # Y offset to properly fit rectangle
        self.__width_height = width_height
        self.__rect = pg.Rect((self.__loc[0] + self.__xoff,
                               self.__loc[1] + self.__yoff),
                              self.__width_height)
        self.__image = image
        self.__speed = 4
        self.__lives = lives

    def get_loc(self) -> None:
        """Returns the location of the ship"""
        return self.__loc

    def get_lives(self) -> int:
        """Returns the number of lives the player has"""
        return self.__lives

    def set_lives(self, lives: int) -> None:
        """Sets the player lives"""
        self.__lives = lives

    def get_rect(self) -> pg.Rect:
        """Returns the rectangle"""
        return self.__rect

    def movement(self, key_press: tuple) -> None:
        """Will handle player moving and firing"""
        m_left = self.__rect.x > 0
        m_right = self.__rect.x < self.__window.get_width() - self.__rect.width
        if key_press[pg.K_a]:
            if m_left:
                new_xloc = self.__loc[0] - self.__speed
                self.__loc = (new_xloc, self.__loc[1])
                self.__rect = pg.Rect((self.__loc[0] + self.__xoff,
                                       self.__loc[1] + self.__yoff),
                                      self.__width_height)
        if key_press[pg.K_d]:
            if m_right:
                xloc = self.__loc[0] + self.__speed
                self.__loc = (xloc, self.__loc[1])
                self.__rect = pg.Rect((self.__loc[0] + self.__xoff,
                                       self.__loc[1] + self.__yoff),
                                      self.__width_height)

    def handle_collision(self, other_rect):
        """Handles the player colliding with other objects."""
        if self.__rect.colliderect(other_rect):
            self.__lives -= 1
            return True
        return False

    def draw(self) -> None:
        """Draws the ship and it's rectangle"""
        if self.__lives > 0:
            self.__window.blit(self.__image, self.__loc)
