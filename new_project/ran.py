import pygame
import sys
from settings import Settings
from st_menu import Menu
from button0 import Button
from level_one import Level1
from level_two import Level2
from level_three import Level3
from level_four import Level4
from level_five import Level5
from level_six import Level6
from level_seven import Level7
from level_eight import Level8
from level_nine import Level9
from level_ten import Level10


def terminate():
    # pygame.QUIT()
    sys.exit()


def run_game():
    pygame.init()
    ol_settings = Settings()
    screen = pygame.display.set_mode((ol_settings.screen_width, ol_settings.screen_height))
    pygame.display.set_caption('Identiphishing')
    menu = Menu(screen)
    button0 = Button(screen, ol_settings)
    pygame.mixer.music.load('Sounds/back.mp3')
    pygame.mixer.music.play()
    level1 = Level1(screen, ol_settings)
    level2 = Level2(screen, ol_settings)
    level3 = Level3(screen, ol_settings)
    level4 = Level4(screen, ol_settings)
    level5 = Level5(screen, ol_settings)
    level6 = Level6(screen, ol_settings)
    level7 = Level7(screen, ol_settings)
    level8 = Level8(screen, ol_settings)
    level9 = Level9(screen, ol_settings)
    level10 = Level10(screen, ol_settings)

    # button = Button(100, 100)

    while True:

        if ol_settings.current_level == 0:
            print('00000P')
            menu.blitme()
            button0.dl()
            button0.draw()
        elif ol_settings.current_level == 1:
            level1.show()
            level1.pr_next()
        elif ol_settings.current_level == 2:
            level2.show()
            level2.pr_next()
        elif ol_settings.current_level == 3:
            level3.show()
            level3.pr_next()
        elif ol_settings.current_level == 4:
            level4.show()
            level4.pr_next()
        elif ol_settings.current_level == 5:
            level5.show()
            level5.pr_next()
        elif ol_settings.current_level == 6:
            level6.show()
            level6.pr_next()
        elif ol_settings.current_level == 7:
            level7.show()
            level7.pr_next()
        elif ol_settings.current_level == 8:
            level8.show()
            level8.pr_next()
        elif ol_settings.current_level == 9:
            level9.show()
            level9.pr_next()
        elif ol_settings.current_level == 10:
            level10.show()
            level10.pr_next()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()


            # if event.type == pygame.KEYDOWN:
            #     ol_settings.current_level += 1

        pygame.display.flip()
        # print(pygame.mouse.get_pos())


run_game()
