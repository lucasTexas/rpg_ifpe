import pygame
import config

cont = 1

while cont > 0 and cont <= 8:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if cont == 1:
            ivo_andando1_x = config.ivo_x
            ivo_andando1_x -= config.ivo_speed
            config.bg_x1 += config.scroll_speed
            config.bg_x2 += config.scroll_speed
            cont = 2
        elif cont == 2:
            ivo_andando2_x = config.ivo_x
            ivo_andando2_x -= config.ivo_speed
            config.bg_x1 += config.scroll_speed
            config.bg_x2 += config.scroll_speed
            cont = 3
        elif cont == 3:
            ivo_andando3_x = config.ivo_x
            ivo_andando3_x -= config.ivo_speed
            config.bg_x1 += config.scroll_speed
            config.bg_x2 += config.scroll_speed
            cont = 4
        elif cont == 4:
            ivo_andando4_x = config.ivo_x
            ivo_andando4_x -= config.ivo_speed
            config.bg_x1 += config.scroll_speed
            config.bg_x2 += config.scroll_speed
            cont = 5
        elif cont == 5:
            ivo_andando5_x = config.ivo_x
            ivo_andando5_x -= config.ivo_speed
            config.bg_x1 += config.scroll_speed
            config.bg_x2 += config.scroll_speed
            cont = 6
        elif cont == 6:
            ivo_andando6_x = config.ivo_x
            ivo_andando6_x -= config.ivo_speed
            config.bg_x1 += config.scroll_speed
            config.bg_x2 += config.scroll_speed
            cont = 7
        elif cont == 7:
            ivo_andando7_x = config.ivo_x
            ivo_andando7_x -= config.ivo_speed
            config.bg_x1 += config.scroll_speed
            config.bg_x2 += config.scroll_speed
            cont = 8
        elif cont == 8:
            ivo_andando8_x = config.ivo_x
            ivo_andando8_x -= config.ivo_speed
            config.bg_x1 += config.scroll_speed
            config.bg_x2 += config.scroll_speed
            cont = 9
    if keys[pygame.K_RIGHT]:
        if cont == 1:
            ivo_andando1_x = config.ivo_x
            ivo_andando1_x += config.ivo_speed
            config.bg_x1 -= config.scroll_speed
            config.bg_x2 -= config.scroll_speed
            cont = 2
        elif cont == 2:
            ivo_andando2_x = config.ivo_x
            ivo_andando2_x += config.ivo_speed
            config.bg_x1 -= config.scroll_speed
            config.bg_x2 -= config.scroll_speed
            cont = 3
        elif cont == 3:
            ivo_andando3_x = config.ivo_x
            ivo_andando3_x += config.ivo_speed
            config.bg_x1 -= config.scroll_speed
            config.bg_x2 -= config.scroll_speed
            cont = 4
        elif cont == 4:
            ivo_andando4_x = config.ivo_x
            ivo_andando4_x += config.ivo_speed
            config.bg_x1 -= config.scroll_speed
            config.bg_x2 -= config.scroll_speed
            cont = 5
        elif cont == 5:
            ivo_andando5_x = config.ivo_x
            ivo_andando5_x += config.ivo_speed
            config.bg_x1 -= config.scroll_speed
            config.bg_x2 -= config.scroll_speed
            cont = 6
        elif cont == 6:
            ivo_andando6_x = config.ivo_x
            ivo_andando6_x += config.ivo_speed
            config.bg_x1 -= config.scroll_speed
            config.bg_x2 -= config.scroll_speed
            cont = 7
        elif cont == 7:
            ivo_andando7_x = config.ivo_x
            ivo_andando7_x += config.ivo_speed
            config.bg_x1 -= config.scroll_speed
            config.bg_x2 -= config.scroll_speed
            cont = 8
        elif cont == 8:
            ivo_andando8_x = config.ivo_x
            ivo_andando8_x += config.ivo_speed
            config.bg_x1 -= config.scroll_speed
            config.bg_x2 -= config.scroll_speed
            cont = 9


keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and config.ivo_x > 0:
            config.ivo_x -= config.ivo_speed
            config.bg_x1 += config.scroll_speed
            config.bg_x2 += config.scroll_speed

        if keys[pygame.K_RIGHT] and config.ivo_x < config.screen_width - config.ivo_width:
            config.ivo_x += config.ivo_speed
            config.bg_x1 -= config.scroll_speed
            config.bg_x2 -= config.scroll_speed
        if keys[pygame.K_UP] and config.ivo_y > 0:
            desvanecer_tela()