import pygame


class Button:
    def __init__(self, screen, settings):
        img = pygame.image.load('play_.jpg')
        self.scrren = screen
        self.settings = settings
        self.image = img
        self.rect = 450

    def draw(self):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button_sound = pygame.mixer.Sound('Sounds/button.wav')

        if self.rect < mouse[0] < 350 + self.rect:
            if self.rect < mouse[1] < 140 + self.rect:
                if click[0] == 1:
                    self.settings.current_level = 1
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(200)

        # else:
        #    pygame(screen ,ic,  (self.width, self.height))

    def dl(self):
        self.scrren.blit(self.image, (self.rect, self.rect))
