import pygame
from config import *
pygame.init()

# Função para desvanecer a tela
def desvanecer_tela():
    superficie = pygame.Surface((800, 600))
    superficie.fill((0, 0, 0))

    for alpha in range(0, 300, 10):
        superficie.set_alpha(alpha)
        screen.blit(superficie, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)


def build_tela_inicial():
	# Desenhar tela inicial
    screen.blit(tela_inicial, (0, 0))
    font = pygame.font.Font(None, 36)
    pressione_enter = font.render("Press ENTER to start", True, (255, 255, 255))
    screen.blit(pressione_enter, (200, 200))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        desvanecer_tela()
        

def build_tela_principal():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ivo_x > 0:
        ivo_x -= ivo_speed
        bg_x1 += scroll_speed
        bg_x2 += scroll_speed
    if keys[pygame.K_RIGHT] and ivo_x < screen_width - ivo_width:
        ivo_x += ivo_speed
        bg_x1 -= scroll_speed
        bg_x2 -= scroll_speed
    if keys[pygame.K_UP] and ivo_y > 0:
        desvanecer_tela()
        
    # Reposicionando o fundo
    if bg_x1 <= -background_width:
        bg_x1 = background_width
    if bg_x2 <= -background_width:
        bg_x2 = background_width    

    # Desenhar o fundo
    screen.blit(background, (bg_x1, 0))
    screen.blit(background, (bg_x2, 0))
    # Desenhar o personagem
    screen.blit(ivo, (200, 200))

