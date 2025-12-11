class GameStats():
    """Class tracks the statistics for the game"""

    def __init__(self,screen_setting):
        """Initializations of statistics"""
        self.screen_setting = screen_setting

        #Initialized high score attribute, High score should never be reset
        self.high_score =  0
        
        self.reset_stats()

        #Initialize the game active flag

        #Start the game in an inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize the game statistics that will br changing during 
        the game"""
        self.ships_left = self.screen_setting.ship_limit
        #Initialize variable for tracking scroe #It Resets when game restarts
        self.score = 0