import pygame
pygame.mixer.init()

"""module will contain a class that controls sounds"""

class Sound():
    """play sounds"""
    def __init__(self,filename):
        self.filename = filename

    
    def play_shooting_sound(self):
        """Plays the shooting sound"""
        sound = pygame.mixer.Sound(self.filename)
        sound.play()