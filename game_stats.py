class GameStats():
    """Class tracks the statistics for the game"""

    def __init__(self,screen_setting):
        """Initializations of statistics"""
        self.screen_setting = screen_setting
        self.reset_stats()

    def reset_stats(self):
        """Initialize the game statistics that will br changing during 
        the game"""
        self.ships_left = self.screen_setting.ship_limit