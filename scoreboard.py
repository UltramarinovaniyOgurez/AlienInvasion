import pygame.font


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
        #Подготовка исходного изображения
        self.prep_score()


    def prep_score(self):
        '''Преобразует текущй счет в пикчу'''
        rounded_score = int(round(self.stats.score,-1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #Делает фон табло прозрачным
        self.score_image.set_colorkey((7,7,9))
        #Вывод счет  в правой верхней части экрана
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        '''Выводим счет на экран'''
        self.screen.blit(self.score_image,self.score_rect)
