class Settings():
    '''Класс для хранения всех настроек игры'''
    def __init__(self):
        '''Инициализирует настройки игры'''
        #Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (225,67,248)
        #Настройки корабля
        self.ship_speed_factor = 1.5
        #Параметры пуль
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 244,22,11