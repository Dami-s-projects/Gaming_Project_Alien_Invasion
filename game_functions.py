import sys                  #These are the modules
import pygame            #that is needed for this particular code file to work
from bullet import Bullet #import bullet class needed for creating a bullet
from alien import Alien
from time import sleep

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



def check_events(
        ship_1,bullet_setting,screen,bullets,statistics,play_button
        ,aliens,screen_setting
        ):
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

            #Check if the mouse button was tapped or double-tapped
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()
                #Check to see whether button was tapped
                check_play_button(statistics,play_button,mouse_x,mouse_y
                                  ,ship_1,aliens,bullets,screen_setting,screen
                                  
                                  )
            

def check_play_button(
        statistics,play_button,mouse_x,mouse_y,ship_1,aliens,bullets
        ,screen_setting,screen
        ):
    """Starts a new game when the player clicks 'Play'. """
    
    #In reality, this code will check whether the tapped region
    #collides with the the space occupied by the play button.
    button_clicked =play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not statistics.game_active:
        #If button was tapped, set game_active to True i.e. Game Starts!!!
        statistics.game_active = True

        #Then reset the game statistics
        statistics.reset_stats()

        #Then Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()

        #Then create a new fleet and center the ship
        create_fleet(screen_setting,screen,aliens,ship_1)
        ship_1.center_ship()

            
                 
                 

def update_screen(
        screen,ship_1,screen_setting,bullets,aliens,statistics,play_button
        ):
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

    #Draw the button if the game is inactive
    if not statistics.game_active:
        play_button.draw_button()
    
    #code that makes the most recently drawn screen (scene) visible
    pygame.display.flip()

def update_bullets(bullets,aliens,screen_setting,screen,ship_1):
    """Move the bullets and get rid of the one that have left screen"""
    bullets.update() #calls the update method of the Bullet class not the
    #one for ship class

    #Call function that checks collision
    check_bullet_and_alien_collision(
        bullets,aliens,screen_setting,screen,ship_1
        )

    #Get rid of bullets that have reached the top of the screen, instead
    #of making it continuously going up while it becomes invisibe in our
    #  sight
    for bullet in bullets.copy():
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

def check_bullet_and_alien_collision(
        bullets,aliens,screen_setting,screen,ship_1
        ):
     #Check collision. Check for any bullet that have hit alien,
    #if so, delete the bullet and the alien.
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if len(aliens) == 0:
    #Destroy existing bullets and create a new fleet
    #when the previous fleet was shot down
        bullets.empty()
        create_fleet(screen_setting,screen,aliens,ship_1)


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

def get_number_rows(alien_height,ship_height,screen_setting):
    """Function determines the number of rows of aliens that fit on 
    the screen"""
    available_height_y = (
        screen_setting.screen_height -( 3 *alien_height) - ship_height
    )
    partial_space =float(0.5 * alien_height)
    number_rows = int(
        (available_height_y/ (alien_height+partial_space))
        )
    return number_rows

def create_alien(screen_setting, screen, aliens, alien_number, row_number):
    """Create an alien and place it in a row"""

    #Please note that i use screen_setting when instantiating the alien
    #It can be confusing, as it should take in speed_setting. But both
    #can do the job as both are instances of settings so they all have 
    #all the attributes in the Settings class. So it is best to
    #think of screen_setting as speed_setting of the alien. The other
    #codes are clear

    alien = Alien(screen_setting,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    #Set the alien horizontal position
    partial_space =float(0.5 * alien_height) #set vertical distance between
                        #each alien to be half of alien height
    alien_x = alien_width + (2 * alien_width *alien_number)
    alien_y = alien_height + (        #Initialize alien new vertical position
        alien_height * row_number +   #to be below the top by the value of
        (row_number *partial_space) ) #alien_height and ensure that there
                                    #is a partial space between alien on
                                    #the first row,second row, and subsequent
                                    # rows.  The row_number determines what
                                    #row the alien is presently duplicated to
                                    #and the for loop will give the row_number
                                    #a value
                            
    alien.rect.x=alien_x
    alien.rect.y = alien_y    #Update the alien position to the initialized
                                #position. Then the next line adds the
                                #alien at this position to the group of aliens
    alien.x =float(alien.rect.x)

    aliens.add(alien)

def create_fleet(screen_setting,screen,aliens,ship_1):
    """A function that creates creates a group of aliens
    and adds them to the screen"""

    #Create an alien and find the number of aliens in a row.
    #The space between each alien is equal to one alien width
    alien = Alien(screen_setting,screen)
    number_aliens_x =get_number_aliens_x(screen_setting,alien.rect.width)
    number_rows = get_number_rows(
        alien.rect.height,ship_1.rect.height,screen_setting
        )
    
    for row_number in range(number_rows): #ensures rows cre created 
        #multiple times
        #Create the first row of alien 
        for alien_number in range(number_aliens_x): 
            #remember range(6):iterates 5x
            #Create an alien and place it in the row
            create_alien(screen_setting,screen,aliens,alien_number,row_number)

def check_fleet_edges(screen_setting,aliens):
    """Function calls change_fleet
     direction if alien hits the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            #calls the check_edges method of the 
            change_fleet_direction(screen_setting,aliens)#alien class
            break

def change_fleet_direction(screen_setting,aliens):
    "Function drops alien down and changes fleet direction"

    #Drops alien
    for alien in aliens.sprites():
        alien.rect.y = alien.rect.y + screen_setting.fleet_drop_speed
        #Changes direction
    screen_setting.fleet_direction = screen_setting.fleet_direction  * -1


def update_aliens(aliens,screen_setting,ship_1,statistics,screen,bullets):
    """Check if alien is at the edge before
    Updating position of alien fleet"""
    check_fleet_edges(screen_setting,aliens)
    aliens.update()
    #look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship_1,aliens):
        #Call ship_hit function when ship collides with aliens
        ship_hit(screen_setting, statistics, screen, ship_1, aliens,bullets)
    #Check to see if any alien has reached the bottom of the screen
    check_aliens_bottom(
        screen_setting,statistics,screen,ship_1,aliens,bullets
        )


def ship_hit(screen_setting, statistics, screen, ship_1, aliens,bullets):
    """Performs operations when ship hits alien"""

    if statistics.ships_left > 1:
        #Firstly, decrement the number of ships left
        statistics.ships_left = statistics.ships_left -1

        #Secondly, Empty the number of aliens and bullets on screen
        aliens.empty()
        bullets.empty()

        #Thirdly, Create a new alien fleet and position the ship at the center
        create_fleet(screen_setting,screen,aliens,ship_1)
        ship_1.center_ship()

        #Fourthly, pause the game for 0.5 second
        sleep(0.5)

        ##Please Note that these code above will only ensure the game pauses,
        # it does the other operations but the next codes in the game main 
        # loop will draw the changes to the screen. Game main
        # loop -(alien_invasion.py)

    else:
        statistics.game_active = False

def check_aliens_bottom(
        screen_setting, statistics, screen, ship_1, aliens,bullets,
        ):
    """Check to see if any alien has reached screen bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #When any alien reaches bottom restart the game (game over)
            #Treat it the same way we treat alien to ship collision.
            ship_hit(screen_setting,statistics,screen,ship_1,aliens,bullets)
            break