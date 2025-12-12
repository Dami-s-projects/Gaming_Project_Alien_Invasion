import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class that adds a ship to screen and sets its position"""

    def __init__(self,speed_setting,screen):
        """initialize the ship and sets its starting position"""
        super(Ship, self).__init__()
        self.screen = screen
        self.speed_setting = speed_setting

        #load the ship image and get its rect
        self.image = pygame.image.load("alien_invasion\images\ship5.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #Store a decimal value for the ship's center
        

        #Start each new ship at the bottom center of the screen
        #By default the image stays at the top left of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.ship_yaxis= float(self.rect.centery)
        self.center = float(self.rect.centerx)

        #Movement flag initialization
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def blit_me(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Update the ship's position based on the movement flag"""
            #update the ship's center value, not the rect, to be precise
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center= self.center + self.speed_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center= self.center - self.speed_setting.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.ship_yaxis = (
                self.ship_yaxis - self.speed_setting.ship_speed_factor
                )
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.ship_yaxis =(
                self.ship_yaxis + self.speed_setting.ship_speed_factor
            )
        # Update rect object from self.center.
        self.rect.centerx = self.center
        self.rect.centery =self.ship_yaxis

    def center_ship(self):
        """Position the ship to the center when called"""
        self.center = self.screen_rect.centerx
        self.ship_yaxis = self.screen_rect.bottom -(
            self.rect.height/2
            )
        
