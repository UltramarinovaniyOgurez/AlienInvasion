import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    '''Класс для вывода игровой инфы'''

    def __init__(self, ai_settings, screen, stats):
        '''Инициализирует атрибуты для подсчета очков'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #Настройка шрифта для вывода счета
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        #Подготовка изображений счетов
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_ships(self):
        '''Сообщаеь количество кораблей'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.top = self.level_rect.bottom
            self.ships.add(ship)




    def prep_level(self):
        self.level_txt = f'Уровень {self.stats.level}'
        self.level_image = self.font.render(self.level_txt, True, self.text_color, self.ai_settings.bg_color)
        # Делает фон табло прозрачным
        self.level_image.set_colorkey(self.ai_settings.bg_color)
        # Выводим его под счетом
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left
        self.level_rect.top = 20

    def prep_score(self):
        '''Преобразует текущй счет в пикчу'''
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #Делает фон табло прозрачным
        self.score_image.set_colorkey(self.ai_settings.bg_color)
        #Вывод счет  в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        high_score = int(round(self.stats.high_score,-1))
        high_score_str = "{:,}".format(high_score)
        #Преобразуем текст в изображение
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        # Делает фон табло прозрачным
        self.high_score_image.set_colorkey(self.ai_settings.bg_color)
        # Выравниваем по центру верхней части экрана
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        '''Выводим счет на экран'''
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        # Вывод кораблей
        self.ships.draw(self.screen)
