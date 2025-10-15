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

    def update(self):
        """A method that causes the bullet move upward by a cetain unit once
        on each call"""
        #move the bullet y coordinate upwards using the value in the 
        #bullet_speed_factor attribute
        self.y = self.y - self.bullet_speed_factor
        #update the coordinate to the new coordinate
        self.rect.y = self.y
    
    def draw_bullet(self):
        """A method that draws the bullet to the screen using the new 
        coordinates"""
        pygame.draw.rect(self.screen,self.colour,self.rect)

