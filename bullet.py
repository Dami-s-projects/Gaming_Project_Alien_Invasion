import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    "A class thaat builds bullet and show them on screen"
    def __init__(self,bullet_setting,screen,ship_1):
        super().__init__()
        self.screen = screen
    
        #Create a bullet rect at (0,0) and then set its correct position.
        self.rect=pygame.Rect(
        0,0,bullet_setting.bullet_width,bullet_setting.bullet_height
        )
        self.rect.centerx = ship_1.rect.centerx
        self.rect.top = ship_1.rect.top

        #Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.colour = bullet_setting.bullet_colour
        self.bullet_speed_factor = bullet_setting.bullet_speed_factor

