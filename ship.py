import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        '''Инициализирует корабль и задает его первоначальную позицию'''
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузка изображения корабля и получение прямоугольника
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.centerx = self.screen_rect.centerx
        #Присвоение кораблю координаты центра экрана поп оси У
        # self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom
        #Сохранение вещественной координаты центра корабля
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        #Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''Обновляет позицию корабля с помощью флага'''
        #проверка на то, что правый край корабля не достиг правого края экрана
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        #аналогично для левого края
        if self.moving_left and self.rect.left >0:
            self.centerx -= self.ai_settings.ship_speed_factor
       #Так же для верха и низа
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
    def bltime(self):
        '''Рисует корабль в текущей позиции'''
        self.screen.blit(self.image,self.rect)