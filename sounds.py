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
        """Reduces the sound volume, makes it a bit lower (50 percent)"""
        self.sound.set_volume(0.5)

class BackgroundMusic(Sound):
    def __init__(self, filename):
        super().__init__(filename)
        self.filename = filename

    def play_music(self):
        """Plays background music"""
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.play(-1)

    def stop_music(self):
        """Stop background music"""
        pygame.mixer.music.stop()