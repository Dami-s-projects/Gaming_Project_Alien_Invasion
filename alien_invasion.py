import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as game_fns

####Dami just remember that settings.py is the module name and the second
#is the class name, it is simply #from module_name import Class_name
#or from module_name import function_name, it can be 
#from settings import display_survey_people_names

def run_game():
    """Creates Alien Invasion game"""

    #Initialize game and create a screen object.
    pygame.init()
    screen_setting=Settings()
    speed_setting=Settings()
    bullet_setting=Settings() #instance of setting for bullet
    screen=pygame.display.set_mode(
        (screen_setting.screen_width,screen_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make a ship
    ship_1=Ship(speed_setting,screen)

    #Make a group to store bullet in.
    bullets = Group()
    

    #Start the main while loop of the game
    while True:

        ###code that watches for Keyboard and mouse events
        game_fns.check_events(ship_1,bullet_setting,screen,bullets)  #changes the attribute of 
        #moving right to true
        ship_1.update()   #calls the update method of ship, which ends up
        #moving the ship to the right by 1 px if right key was pressed

        #displays and update screen each iteration
        game_fns.update_screen(screen,ship_1,screen_setting,bullets)


run_game()

    