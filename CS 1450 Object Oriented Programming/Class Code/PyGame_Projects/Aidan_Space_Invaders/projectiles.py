"""
Projectile class that is used when firing orojectiles
Aidan Butcher
CS 1450 - Intro to OOP
2022-12-07
Todo: None.
Bugs: None.
"""

import pygame as pg


class Projectile():
    """Projectile class for handling projectiles being fired"""
    def __init__(self, window: pg.Surface, loc: tuple, width_height: tuple,
                 image: pg.Surface, direction: str, cool: float = 300):
        self.__window = window
        self.__loc = loc
        self.__orig_loc = loc
        self.__width_height = width_height
        self.__rect = pg.Rect(self.__loc, self.__width_height)
        self.__image = image
        self.__direction = direction.lower()
        self.__speed = 5
        self.__moving = False
        if self.__direction == "d":
            self.__image = pg.transform.flip(self.__image, False, True)
        self.__destroy = False
        self.__last = pg.time.get_ticks()
        self.__cooldown = cool

    def set_last_fire(self, time: float) -> None:
        """Sets the last time the projectile was fired."""
        self.__last = time

    def get_last_fire(self) -> float:
        """Returns the time the projectile was last fired."""
        return self.__last

    def get_cooldown(self) -> float:
        """Returns the cooldown for the projectile."""
        return self.__cooldown

    def set_rect_loc(self, loc: tuple) -> None:
        """Sets the location of the projectile rectangle"""
        self.__rect = pg.Rect(loc, self.__width_height)

    def get_rect(self) -> pg.Rect:
        """Returns the rectangle of the projectile"""
        return self.__rect

    def set_loc(self, loc: tuple) -> None:
        """Sets the location of the projectile"""
        self.__loc = loc
        self.set_rect_loc(loc)

    def get_loc(self) -> tuple:
        """Returns the location of the projectile"""
        return self.__loc

    def reset_loc(self) -> None:
        """Resets the location of the projectile to it's original location"""
        self.__loc = self.__orig_loc
        self.__rect = pg.Rect(self.__loc, self.__width_height)

    def set_direction(self, direct) -> None:
        """Sets the direction of the projectile"""
        if direct == 'u' and self.__direction != 'u':
            self.__direction = 'u'
            self.__image = pg.transform.flip(self.__image, False, True)
        if direct == 'd' and self.__direction != 'd':
            self.__direction = 'd'
            self.__image = pg.transform.flip(self.__image, False, True)

    def get_moving(self) -> bool:
        "Returns if the projectile is moving or not"
        return self.__moving

    def movement(self) -> None:
        """Moves the projectile"""
        m_up = self.__rect.y > 0
        m_down = self.__rect.y < (self.__window.get_height() -
                                  self.__rect.height)
        if self.__direction == 'd':
            if m_down:
                new_y = self.__loc[1] + self.__speed
                self.__loc = (self.__loc[0], new_y)
                self.__rect = pg.Rect(self.__loc, self.__width_height)
                if self.__loc[0] > self.__window.get_width():
                    self.__moving = False
                else:
                    self.__moving = True
            else:
                self.__destroy = True
                self.__moving = False
                self.__rect = pg.Rect(self.__window.get_size(),
                                      self.__width_height)
        if self.__direction == 'u':
            if m_up:
                new_y = self.__loc[1] - self.__speed
                self.__loc = (self.__loc[0], new_y)
                self.__rect = pg.Rect(self.__loc, self.__width_height)
                if self.__loc[0] > self.__window.get_width():
                    self.__moving = False
                else:
                    self.__moving = True
            else:
                self.__destroy = True
                self.__moving = False
                self.__rect = pg.Rect(self.__window.get_size(),
                                      self.__width_height)

    def fire(self, loc: tuple) -> None:
        """Fires the projectile from the given location"""
        self.__loc = loc
        self.set_rect_loc(loc)
        self.__destroy = False
        self.__moving = True

    def draw(self) -> None:
        """Draws the projectile"""
        if not self.__destroy:
            self.__window.blit(self.__image, self.__loc)
