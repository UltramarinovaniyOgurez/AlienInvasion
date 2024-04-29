import pygame

class Settings():
    '''Класс для хранения всех настроек игры'''
    def __init__(self):
        '''Инициализирует статические настройки игры'''
        #Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (7,7,9)
        #Фон - картинка
        self.background_image = pygame.image.load("images/space.bmp")


        #Настройки корабля

        self.ship_limit = 3


        #Настройки пришельцев

        self.fleet_drop_speed = 10



        # Параметры пуль
#--------------------------------------------------------------------------------------------------
        #Для стрельбы вправо
        # self.bullet_width = 15
        # self.bullet_height = 3
#--------------------------------------------------------------------------------------------------
        #Для вертикальных пуль
        self.bullet_width = 3
        self.bullet_height = 15

        self.bullet_color = 244,22,11
        self.bullets_allowed = 3


        #Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dinamic_settings()


    def initialize_dinamic_settings(self):
        '''Инициализирует настройкиб изменяющиеся в ходе игры'''
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 0.3
        self.bullet_speed_factor = 3
        #1 - вправо, -1 - влево
        self.fleet_direction = 1


    def increase_speed(self):
        '''Увеличивает скорости'''
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor = self.speedup_scale
        self.bullet_speed_factor = self.speedup_scale

