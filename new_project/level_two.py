import pygame


class Level2:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()
        self.question = pygame.image.load('level_2.jpg')
        self.rect_question = self.question.get_rect()
        self.rect_question.centerx = self.screen_rect.centerx
        self.rect_question.centery = self.screen_rect.centery
        self.right_answer = pygame.image.load('level_True.jpg')
        self.wrong_answer = pygame.image.load('level_False.jpg')

    def pr_next(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button_sound = pygame.mixer.Sound('Sounds/button.wav')
        # print(self.settings.current_level) print(self.settings.current_level == 1 and mouse[0] >
        # self.screen_rect.centerx and mouse[1] > self.screen_rect.centery)
        if self.settings.current_level == 2 and mouse[0] < self.screen_rect.centerx and mouse[1] > self.screen_rect.centery:
            if click[0] == 1:
                self.settings.current_level = 0
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(200)
        elif self.settings.current_level == 2 and mouse[0] > self.screen_rect.centerx and mouse[1] > self.screen_rect.centery:
            print(click[0])
            if click[0] == 1:
                print('qqqqqqqq')
                self.settings.current_level = 3
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(200)

    def show(self):
        self.screen.blit(self.question, self.rect_question)
        self.screen.blit(self.right_answer, (650, 600))
        self.screen.blit(self.wrong_answer, (50, 600))
