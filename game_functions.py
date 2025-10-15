import sys                  #These are the modules
import pygame            #that is needed for this particular code file to work
from bullet import Bullet #import bullet class needed for creating a bullet

def check_keydown_events(event, ship_1,bullet_setting,bullet,screen):
    """Respond when the key is pressed down"""
    if event.key == pygame.K_RIGHT:
        #move the ship to the right
        ship_1.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship_1.moving_left = True
    elif event.key == pygame.K_UP: #sets the moving up flag to true when 
        ship_1.moving_up = True    #up key is pressed
    elif event.key == pygame.K_DOWN:  #sets the moving down flag to true when
        ship_1.moving_down = True      #down key is pressed
    elif event.key == pygame.K_SPACE: #when user presses space bar
        new_bullet = Bullet(bullet_setting,screen,ship_1)
        bullet.add(new_bullet) #add the new bullet to the group


def check_keyup_events(event, ship_1):
    """Respond when the key is released"""
    if event.key == pygame.K_RIGHT:
        #Release the ship when either right or left keys
        #is released
        ship_1.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship_1.moving_left = False
    elif event.key == pygame.K_UP:  #sets the moving up flag to False when 
        ship_1.moving_up = False   #up key is released
    elif event.key == pygame.K_DOWN:  #sets the moving down flag to False when 
        ship_1.moving_down = False   #down key is released



def check_events(ship_1,bullet_setting,screen,bullets):
    """A function that contains code that responds to key presses 
    and mouse events"""
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #call keydown function for button pressed down
                check_keydown_events(
                    event,ship_1,bullet_setting,bullets,screen
                    )
            elif event.type == pygame.KEYUP:
                #call keyup function for button released
                check_keyup_events(event, ship_1)
            
                 
                 

def update_screen(screen,ship_1,screen_setting,bullets):
    """A function that contains code that displays ship and 
    shows the latest screen(frame) """
     #Redraw the screen each pass through the loop with the 
    # background colour appearing each time at the background
    screen.fill(screen_setting.bg_colour)

    #Redraws the bullet above the background colour and behind the ship 
    # and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #Display ship
    ship_1.blit_me()
    
    #code that makes the most recently drawn screen (scene) visible
    pygame.display.flip()