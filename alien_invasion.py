import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
# для корабля внизу экрана
from ship import Ship
from alien import Alien
import game_function as gf


#-----------------------------------------------------------------------------------------------------
# для корабля слева
# from side_shooting.side_ship import Ship
#-----------------------------------------------------------------------------------------------------


def run_game():
    # Инициализирует пайгейм,настройки и объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    #Создание экземпляра для хранения игровой статистики
    stats = GameStats(ai_settings)


#-----------------------------------------------------------------------------------------------------------------------
    #Создание группы фоновых звезд
    # stars = Group()
    # gf.create_stars(ai_settings,screen,stars)
#--- -------------------------------------------------------------------------------------------------------------------


    #Создание корабля
    ship = Ship(ai_settings,screen)
    #Создание группы для пуль
    bullets = Group()
    #Создание флота пришельцев
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #
    #Запуск основного цикла игры
    while True:
        # Проверка событий клавиатуры
        gf.check_events(ai_settings,screen,ship,bullets)
        # Обновление позиции корабля
        ship.update()
        # обновление позиций пуль
        gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
        #Обновление позиций пришельцев
        gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
        # Обновление экрана
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)


run_game()
