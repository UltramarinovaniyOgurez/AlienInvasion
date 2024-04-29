class GameStats():
    '''Отслеживание статистики игры'''
    def __init__(self,ai_settings):
        '''Инициализация статистики'''
        self.ai_settings = ai_settings
        self.reset_stats()
        #Флаг для запуска игры в неактивном состоянии
        self.game_active = False
        # Рекорд
        self.high_score = 0

    def reset_stats(self):
        '''Инициализирует статистику, изменияющуюся по ходу игры'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

