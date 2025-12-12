import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """A class that reports scoring information"""
    def __init__(self,screen_setting,screen,statistics,speed_setting):
        """Initialize score keeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.screen_setting = screen_setting
        self.statistics = statistics
        self.speed_setting = speed_setting

        #(Font settings for colour information

        #Text colour
        self.text_colour = (30, 30, 30)

        #Font type
        self.font = pygame.font.SysFont(None, 48)
        #)

        #Now prepare the score image to be displayed
        self.prepare_score()
        self.prepare_high_score()
        self.prepare_level()
        self.prepare_ships()

    def prepare_score(self):
        """Method turns the score into a rendered image"""
        rounded_score = round(self.statistics.score,-1)
        score_string = str("Score: ")+"{:,}".format(rounded_score)
        self.score_image = self.font.render(score_string,True,
                    self.text_colour,self.screen_setting.bg_colour
        )

        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Displays rendered score text on screen"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        #show level
        self.screen.blit(self.level_image,self.level_number_rect)
        #show ships left
        self.ships.draw(self.screen)

    def prepare_high_score(self):
        """Convert the integer High score to image"""

        #Firstly round it up
        high_score = round(self.statistics.high_score,-1)
        #Secondly, separate it by commas and make it a string
        high_score_str = str("High Score: ")+"{:,}".format(high_score)
        #Thirdly convert the string to image
        self.high_score_image = self.font.render(high_score_str
        ,True,self.text_colour,self.screen_setting.bg_colour)

        #Finally, place the high score at the top center of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def prepare_level(self):
        """Turns the level into a rendered image"""
        level_number = str("Level: ") + str(self.statistics.level)
        self.level_image = self.font.render(
            level_number,True,self.text_colour,self.screen_setting.bg_colour)
        
        #position level number below the score number
        self.level_number_rect = self.level_image.get_rect()
        self.level_number_rect.right = self.score_rect.right
        self.level_number_rect.top = self.score_rect.bottom +20
    
    def prepare_ships(self):
        """function shows number of ships left as images"""
        self.ships = Group()
        #make the ship images number the same as the number on ship left
        for ship_number_count in range(self.screen_setting.ship_limit):
            #create a ship image and add to group
            ship = Ship(self.speed_setting,self.screen)
            #Position each ship at the right next to each other.
            #position is 10 pixels (10px) below the top left 
            ship.rect.y=10
            ship.rect.x = 10 + (ship_number_count *ship.rect.width)
            self.ships.add(ship)