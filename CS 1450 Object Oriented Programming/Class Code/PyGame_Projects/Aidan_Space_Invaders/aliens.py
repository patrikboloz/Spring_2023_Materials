"""
Alien class(es) that will handle all the aliens and their stuff.
Aidan Butcher
CS 1450 - Intro to OOP
2022-12-06
Todo: None.
Bugs: None.
"""

from abc import ABC, abstractmethod
import pygame as pg


# pylint: disable=arguments-differ
class Aliens(ABC):
    """General alien that will then be inherited to specific aliens"""
    def __init__(self, window: pg.Surface, loc: tuple, width_height: tuple,
                 image: pg.Surface, health: int):
        self._window = window
        self._loc = loc
        self._orig_loc = loc
        self._width_height = width_height
        self._rect = pg.Rect(self._loc, self._width_height)
        self._image = image
        self._health = health
        self._orig_health = health
        self._x_speed = 4
        self._y_speed = 50
        self._dir = 'r'

    def side_movement(self):
        """Handles alien's back and forth movement and when to move down'"""
        max_right = self._rect.x >= self._window.get_width() - self._rect.width
        max_left = self._rect.x <= 0
        if self._dir == 'r':
            new_x = self._loc[0] + self._x_speed
            self._loc = (new_x, self._loc[1])
            self._rect = pg.Rect(self._loc, self._width_height)
            if max_right:
                self._dir = 'l'
                self.down_movement()
        if self._dir == 'l':
            new_x = self._loc[0] - self._x_speed
            self._loc = (new_x, self._loc[1])
            self._rect = pg.Rect(self._loc, self._width_height)
            if max_left:
                self._dir = 'r'
                self.down_movement()

    @abstractmethod
    def down_movement(self):
        """Abstract method for alien's moving down"""
        raise NotImplementedError

    def handle_collision(self, proj_rect) -> bool:
        """Handles projectiles colliding with aliens"""
        if self._rect.colliderect(proj_rect):
            self._health -= 1
            return True
        return False

    def set_loc(self, loc: tuple) -> None:
        """Sets the location of the alien"""
        self._loc = loc

    def get_loc(self) -> tuple:
        """Returns the location of the alien"""
        return self._loc

    def set_health(self, health) -> None:
        """Sets the health of the alien"""
        self._health = health

    def get_health(self) -> int:
        """Returns the health of the alien"""
        return self._health

    def set_rect_loc(self, loc: tuple) -> None:
        """Sets the location of the rect"""
        self._rect = pg.Rect(loc, self._width_height)

    def get_rect(self) -> pg.Rect:
        """Gets the rectangle of the alien"""
        return self._rect

    def reset(self, direct='r') -> None:
        """Resets all aliens to their original health and position"""
        self._loc = self._orig_loc
        self._health = self._orig_health
        self._dir = direct

    def draw(self) -> None:
        """Draws the alien to the window"""
        if self._health > 0:
            self._window.blit(self._image, self._loc)


class Bee(Aliens):
    """Bee alien and it's movement"""
    def down_movement(self) -> None:
        """Will handle the movement of the bee alien"""
        max_down = self._rect.y < self._window.get_height() - self._rect.height
        if max_down:
            new_y = self._loc[1] + self._y_speed
            self._loc = (self._loc[0], new_y)
            self._rect = pg.Rect(self._loc, self._width_height)


class Moth(Aliens):
    """Moth alien and it's movement"""
    def down_movement(self) -> None:
        """Will handle the movement of the moth alien"""
        max_down = self._rect.y < self._window.get_height() - self._rect.height
        if max_down:
            new_y = self._loc[1] + self._y_speed
            self._loc = (self._loc[0], new_y)
            self._rect = pg.Rect(self._loc, self._width_height)


class AlienShip(Aliens):
    """Alien ship, it's movement, and firing"""
    def __init__(self, window, loc, width_height, image, health):
        super().__init__(window, loc, width_height, image, health)
        self._health += 1
        self._orig_health = self._health

    def down_movement(self):
        """Will handle the movement of the alien ship"""
        max_down = self._rect.y < self._window.get_height() - self._rect.height
        if max_down:
            new_y = self._loc[1] + self._y_speed
            self._loc = (self._loc[0], new_y)
            self._rect = pg.Rect(self._loc, self._width_height)

    def reset(self, direct='r') -> None:
        self._loc = self._orig_loc
        self._health = self._orig_health
        self._dir = direct

# Scrapped due to time limitations.
# pylint: disable=pointless-string-statement
"""
    def shoot(self):
        ""Will handle the alien ship shooting.""
        raise NotImplementedError
"""

# Scrapping the boss fight since it's gonna be too much work.
"""class Boss(Aliens):
    ""Alien boss, it's movement, firing, and health""
    def __init__(self, window, loc, width_height, image, health):
        super().__init__(window, loc, width_height, image, health)
        self.__xoff = 8  # X offset for properly fitting rectangle
        self.__yoff = 7  # Y offset for properly fitting rectangle
        self._rect = pg.Rect((self._loc[0] + self.__xoff,
                              self._loc[1] + self.__yoff), self._width_height)
        self._health += 9

    def movement(self):
        ""Will handle the movement of the alien boss""
        max_down = self._rect.y < self._window.get_height() - self._rect.height
        if max_down:
            new_y = self._loc[1] + self._y_speed
            self._loc = (self._loc[0], new_y)
            self._rect = pg.Rect((self._loc[0] + self.__xoff,
                                  self._loc[1] + self.__yoff),
                                 self._width_height)

    def shoot(self):
        ""Will handle the alien ship shooting""
        raise NotImplementedError"""
