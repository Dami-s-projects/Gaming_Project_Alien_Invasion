import asyncio                        #Added module that handles web conversion
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as game_fns
from game_stats import GameStats
from button import Button
from score_board import Scoreboard
from sounds import Sound
from sounds import BackgroundMusic
from touch_controls import TouchControls

####Dami just remember that settings.py is the module name and the second
#is the class name, it is simply #from module_name import Class_name
#or from module_name import function_name, it can be 
#from settings import display_survey_people_names

#added "async", thats what is required for async module to operate"
async def run_game():   
    """Creates Alien Invasion game"""

    #Initialize game and create a screen object.
    pygame.init()
    
    #add clock function call
    clock = pygame.time.Clock()

    screen_setting=Settings()
    speed_setting=Settings()
    bullet_setting=Settings() #instance of setting for bullet
    screen=pygame.display.set_mode(
        (screen_setting.screen_width,screen_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make the play button (i.e. make an innstance of button class)
    play_button = Button(screen_setting,screen,"Play")


    ###########
    # ##The file path needs to change to include the forward slash for web compatibility

    #Instantiance sound class
    shooting_sound_effect=Sound("sounds/bullet_shot.ogg")
    background_music=BackgroundMusic(
        "sounds/alien_invasion_background_music.ogg"
    )

    #make another instance of the background music and pass the other sound
    #as the arguement
    calm_music=BackgroundMusic(
        "sounds/alien_invasion_gameoff_track.ogg"
        )
    
    explosion=Sound("sounds/alien_explosion_sound.ogg")

    #Create an instance to store game statistics and create scoreboard
    statistics = GameStats(screen_setting)
    score_details =Scoreboard(screen_setting,screen,statistics,speed_setting)
    
    #Play the music immediately game begins
    calm_music.play_music()


    #Make a ship
    ship_1=Ship(speed_setting,screen)
    
    #Add touch controls to game (very useful for mobiles)
    touch_controls = TouchControls(screen_setting,screen)

    #Make a group to store bullet in.
    bullets = Group() #but this group is really like an instance of Bullet() 
    
    #Make an Alien
    aliens = Group()

    #Create the fleet of aliens
    game_fns.create_fleet(screen_setting,screen,aliens,ship_1)

    #Start the main while loop of the game
    while game_fns.is_game_running():

        ###code that watches for Keyboard and mouse events
        game_fns.check_events(
            ship_1,bullet_setting,screen,bullets,statistics,play_button
            ,aliens,screen_setting,score_details
            ,shooting_sound_effect,background_music,
            calm_music,touch_controls)  #changes the attribute of 
        if statistics.game_active:
            # Reset movement flags each frame
            ship_1.moving_left = False
            ship_1.moving_right = False
            ship_1.moving_up = False
            ship_1.moving_down = False
            
            # Apply keyboard input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                ship_1.moving_left = True
            if keys[pygame.K_RIGHT]:
                ship_1.moving_right = True
            if keys[pygame.K_UP]:
                ship_1.moving_up = True
            if keys[pygame.K_DOWN]:
                ship_1.moving_down = True
            

            #activate touch control before controlling ship
            touch_controls.apply_to_ship(ship_1)

            #moving right to true
            ship_1.update()   #calls the update method of ship, which ends up
            #moving the ship to the right by 1 px if right key was pressed

            game_fns.update_bullets(bullets,aliens,screen_setting,screen,ship_1
            ,statistics,score_details,explosion)
            game_fns.update_aliens(
                aliens,screen_setting,ship_1,statistics,screen,bullets,
                score_details,background_music,calm_music
                )

        #displays and update screen each iteration
        game_fns.update_screen(
            screen,ship_1,screen_setting,bullets,aliens,statistics,play_button
            ,score_details,touch_controls
            )
        clock.tick(60)
        await asyncio.sleep(0) #code thats needed also


asyncio.run(run_game()) #replace the previous call so ayncio calls the run_game function.

    