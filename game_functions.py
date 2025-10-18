import sys                  #These are the modules
import pygame            #that is needed for this particular code file to work
from bullet import Bullet #import bullet class needed for creating a bullet
from alien import Alien

def fire_bullets(bullet,bullet_setting,screen,ship_1):
    """Fire a bullet if limit is not reached (limit of 3 here)"""
    if len(bullet) < bullet_setting.bullets_allowed:
        # Create a new bullet and add it to the bullets group
        new_bullet = Bullet(bullet_setting,screen,ship_1)
        bullet.add(new_bullet) #add the new bullet to the group

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
        fire_bullets(bullet,bullet_setting,screen,ship_1)
    elif event.key == pygame.K_q:
        sys.exit()

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
            
                 
                 

def update_screen(screen,ship_1,screen_setting,bullets,aliens):
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
    aliens.draw(screen)
    
    #code that makes the most recently drawn screen (scene) visible
    pygame.display.flip()

def update_bullets(bullets):
    """Move the bullets and get rid of the one that have left screen"""
    bullets.update() #calls the update method of the Bullet class not the
    #one for ship class

    #Get rid of bullets that have reached the top of the screen, instead
    #of making it continuously going up while it becomes invisibe in our
    #  sight
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

def get_number_aliens_x(screen_setting,alien_width):
    """Function that determines the number of aliens that fit in a row"""
    #we only want to use the middle space of screen, with two margins
    #at both end. The margin should have a pixel width equivalent
    #to  the width of an alien
    available_space_x = screen_setting.screen_width - (2*alien_width)

    #maths for No of alien that can fit screen width 
    #The math takes into account that there is an alien width pixel kind
    #of space at both sides of the alien
    number_aliens_x = int((available_space_x)/(2*alien_width))
    return number_aliens_x

def create_alien(screen_setting, screen, aliens, alien_number):
    """Create an alien and place it in a row"""

    #Please note that i use screen_setting when instantiating the alien
    #It can be confusing, as it should take in speed_setting. But both
    #can do the job as both are instances of settings so they all have 
    #all the attributes in the Settings class. So it is best to
    #think of screen_setting as speed_setting of the alien. The other
    #codes are clear

    alien = Alien(screen_setting,screen)
    alien_width = alien.rect.width
    #Set the alien horizontal position
    alien_x = alien_width + (2 * alien_width *alien_number)
    alien.rect.x=alien_x
    aliens.add(alien)

def create_fleet(screen_setting,screen,aliens):
    """A function that creates creates a group of aliens
    and adds them to the screen"""

    #Create an alien and find the number of aliens in a row.
    #The space between each alien is equal to one alien width
    alien = Alien(screen_setting,screen)
    number_aliens_x =get_number_aliens_x(screen_setting,alien.rect.width)

    #Create the first row of alien
    for alien_number in range(number_aliens_x):#remember range(6): iterates 5x
        #Create an alien and place it in the row
        create_alien(screen_setting,screen,aliens,alien_number)

       