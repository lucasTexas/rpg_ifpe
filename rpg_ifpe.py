import pygame
import config

# Inicializando o Pygame
pygame.init()

def desvanecer_tela():
    superficie = pygame.Surface((800, 600))
    superficie.fill((0, 0, 0))

    for alpha in range(0, 300, 10):
        superficie.set_alpha(alpha)
        config.screen.blit(superficie, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)


# Loop principal
clock = pygame.time.Clock()
running = True
tela = "primeira"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if tela == "primeira":
        # Desenhar tela inicial
        config.screen.blit(config.tela_inicial, (0, 0))
        font = pygame.font.Font(None, 36)
        pressione_enter = font.render("Press ENTER to start", True, (255, 255, 255))
        config.screen.blit(pressione_enter, (200, 200))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            desvanecer_tela()
            tela = "segunda"
            
    if tela == "segunda":
        cont = 1

        # Reposicionando o fundo
        if config.bg_x1 <= -config.background_width:
            bg_x1 = config.background_width
        if config.bg_x2 <= -config.background_width:
            bg_x2 = config.background_width

        # Desenhar o fundo
        config.screen.blit(config.background, (config.bg_x1, 0))
        config.screen.blit(config.background, (config.bg_x2, 0))
        # Desenhar o personagem
        config.screen.blit(config.ivo, (200, 200))

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

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
#sys.exit()
