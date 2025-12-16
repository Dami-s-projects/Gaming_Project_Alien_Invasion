import pygame
pygame.mixer.init()

"""module will contain a class that controls sounds"""

class Sound():
    """play sounds"""
    def __init__(self,filename):
        self.filename = filename
        self.sound = pygame.mixer.Sound(self.filename)

    
    def play_shooting_sound(self):
        """Plays the shooting sound"""
        self.sound.play()
    
    def decrease_sound_volume(self):
        """Reduces the sound volume, makes it a bit lower (20 percent)"""
        self.sound.set_volume(0.2)