import pygame.font

class Scoreboard():
    """A class that reports scoring information"""
    def __init__(self,screen_setting,screen,statistics):
        """Initialize score keeping attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.screen_setting = screen_setting
        self.statistics = statistics

        #(Font settings for colour information

        #Text colour
        self.text_colour = (30, 30, 30)

        #Font type
        self.font = pygame.font.SysFont(None, 48)
        #)

        #Now prepare the score image to be displayed
        self.prepare_score()

    def prepare_score(self):
        """Method turns the score into a rendered image"""
        score_string = str(self.statistics.score)
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



        