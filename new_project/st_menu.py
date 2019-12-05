import pygame


#trans = pygame.transform.scale('play_.jpg', (1200, 800))


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('menu_new.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1200, 800))
        self.rect = (0, 0)
        self.screens = screen
        #self.image2 = pygame.image.load('1.jpg').convert_alpha()
        #self.rect2 = (280, 40)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        #self.screens.blit(self.image2, self.rect2)
