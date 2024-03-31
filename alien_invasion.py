import pygame
from pygame.sprite import Group

from settings import Settings
# from ship import Ship
from side_shooting.side_ship import Ship
import game_function as gf
def run_game():
    # Инициализирует пайгейм,настройки и объект экрана
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    #Создание корабля
    ship = Ship(ai_settings,screen)
    #Создание группы для пуль
    bullets = Group()
    #Запуск основного цикла игры
    while True:
        # Проверка событий клавиатуры
        gf.check_events(ai_settings,screen,ship,bullets)
        # Обновление позиции корабля
        ship.update()
        # обновление позиций пуль
        gf.update_bullets(bullets)
        # Обновление экрана
        gf.update_screen(ai_settings,screen,ship,bullets)


run_game()
