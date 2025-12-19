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
    
    def save_and_stop_music(self):
        """This method should save the time at which a music was stopped
        snd then stop the music, the saved time ensures
        that the music can continue where it left off."""

        # update attribute to get the time the music stop.
        self.music_time_stamp = pygame.mixer.music.get_pos()/1000 
        #divided by 1000 converts the timestamp of the music from
        #the default milliseconds that would have been detected to seconds.

        #Stop music
        pygame.mixer.music.stop()