class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializations of game settings"""
        
        #ship setting
        self.ship_speed_factor = 0.5

        #Screen settings
        self.screen_width= 1200
        self.screen_height= 800
        self.bg_colour= (230,230,230)

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3

        