class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initializations of game settings"""
        
        #ship setting
        self.ship_limit = 3

        #Screen settings
        self.screen_width= 1200
        self.screen_height= 960
        self.bg_colour= (230,230,230)

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = 60, 60, 60
        self.bullets_allowed = 3

        #Alien settings, whole fleet moves together
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 20
        

        #How quickly the game speeds up
        self.speedup_scale = 1.4
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 0.5
        self.alien_speed_factor = 0.2
        self.bullet_speed_factor = 1
        #fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1
        
    def increase_speed(self):
        """Level up the game by increasing the dynamic speed settings"""
        self.ship_speed_factor = (
            self.ship_speed_factor * self.speedup_scale
            )
        self.bullet_speed_factor = (
            self.bullet_speed_factor * self.speedup_scale
        )
        self.alien_speed_factor = (
            self.alien_speed_factor * self.speedup_scale
        )

        