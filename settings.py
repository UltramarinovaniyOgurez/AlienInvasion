

class Settings():
    '''Класс для хранения всех настроек игры'''
    def __init__(self):
        '''Инициализирует настройки игры'''
        #Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (7,7,9)


        #Настройки корабля
        self.ship_speed_factor = 0.5





        #Настройки пришельцев
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 5
        self.fleet_direction = 1


        # Параметры пуль
        self.bullet_speed_factor = 1
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
