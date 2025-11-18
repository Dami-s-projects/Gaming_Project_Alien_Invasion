import pygame.font

class Button():
    """A class that creates a button"""

    def __init__(self,screen_setting,screen,msg):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #Set the dimensions and properties of the button
        self.width= 200
        self.height= 50
        self.button_colour= (238,1,1) #button colour is red
        self.text_colour  = (255, 255, 255) #Text colour is white
        self.font = pygame.font.SysFont(None,48)

        #Build the Button's rect and centre it
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        #Call the prep msg method
        self.prep_msg(msg)

    def prep_msg(self,msg):
        """Turn msg into a rendered image and center text on button"""
        self.msg_image = self.font.render(
            msg,True,self.text_colour,self.button_colour
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw blank button and the text message on screen"""
        self.screen.fill(self.button_colour,self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)



