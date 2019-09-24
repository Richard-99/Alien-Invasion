import sys
import pygame

from pygame.sprite import Group
from ship import Ship
from settings import Settings
from alien import Alien
import game_functions as gf

def run_game():

    # Initiate pygame settings and screen object
    pygame.init()
    ai_settings = Settings() 
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion!")

    # Make a ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets
    bullets = Group()

    # Make a group of aliens
    aliens = Group()

    # Make an alien
    alien = Alien(ai_settings, screen)

    # Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, aliens)

    # Set the background colour
    bg_color = (230, 230, 230)

    # Start the main loop for game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen through each pass of the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
