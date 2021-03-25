import pygame
from game.settings import Settings
from game.image.ship import Ship
from game.game_functions import check_events, update_screen
from pygame.sprite import Group


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen, settings)
    bullets = Group()
    while True:
        check_events(ship, settings, screen, bullets)
        screen.fill(settings.bg_color)
        ship.update()
        ship.blitme()
        pygame.display.flip()
        bullets.update()
        update_screen(bullets, ship, settings, screen)


run_game()
