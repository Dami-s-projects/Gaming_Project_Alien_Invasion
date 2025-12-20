import pygame
from pygame.sprite import Sprite

class Alien(Sprite): #class inherits form Sprite class
    """A class to represent a single alien in the fleet"""

    def __init__(self, speed_setting,screen):
        """A method containing all initialization of alien attributes,
        as well as setting its starting position """
        super().__init__()

        self.screen = screen
        self.speed_setting = speed_setting

        #Load the alien and set its rect attribute.
        self.image=pygame.image.load("./alien_invasion/images/alienship.bmp")
        self.rect=self.image.get_rect()

        #sets its x position by certain pixels away from
        # the origin(top-left ). The pixels is equivalent to the width of the
        #image
        self.rect.x = self.rect.width
        #sets its y position by certain pixels away from the top. The pixels
        #is equivalent to the height of the image
        self.rect.y = self.rect.height

        #Store the alien's exact position
        self.x = float(self.rect.x)

    def blit_me(self):
        """A method that draws the alien at its exact location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Function moves Alien fleet to the right"""
        self.x = (
            self.x +(
                self.speed_setting.alien_speed_factor *
                self.speed_setting.fleet_direction
                )
        )
        #use the updated coordinate
        self.rect.x = self.x

    def check_edges(self):
        "Function returns True if an alien has reached the edge of the screen"
        screen_rect= self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True