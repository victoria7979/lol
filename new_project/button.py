import pygame
from settings import Settings


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (23, 204, 58)
        self.act_color = (13, 152, 58)

    def draw(self, x, y, message, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        ol_settings = Settings()
        button_sound = pygame.mixer.Sound('Sounds/button.wav')

        if x < mouse[0] < x + self.width:
            if y < mouse[1] < y + self.height:
                pygame.draw.rect(ol_settings, self.inactive_color, (x, y, self.width, self.height))

                if click[0] == 1:
                    pygame.mixer.Sound.play(button_sound)
                    pygame.time.delay(300)
                    if action is not None:
                        action()
            # вписати звук кнопки в сетінг і імпортувати сюда

        else:
            pygame.draw.rect(ol_settings, self.act_color, (x, y, self.width, self.height))

        print_text(message, x + 10, y + 10, )


def print_text(message, x, y, font_color=(0, 0, 0), font_type=(), font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
