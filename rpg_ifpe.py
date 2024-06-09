import pygame
#import sys

# Inicializando o Pygame
pygame.init()



# Configurações da tela
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("ELSE")

# Carregar tela inicial
tela_inicial = pygame.image.load("else.jpeg").convert()
tela_inicial_width = tela_inicial.get_width()
tela_inicial_height = tela_inicial.get_height()


# Carregar a imagem de fundo
background = pygame.image.load("cenario_rpg.jpeg").convert()
background_width = background.get_width()
background_height = background.get_height()

# Carregar personagem
ivo = pygame.image.load("mini_ivo.png").convert_alpha()
ivo_width = ivo.get_width()
ivo_height = ivo.get_height()

# Coordenadas iniciais do fundo
bg_x1 = 0
bg_x2 = background_width

# Coordenadas iniciais do personagem
ivo_x = 66 
ivo_y = ivo_height

# Velocidade do movimento do fundo
scroll_speed = 2
ivo_speed = 2

# Função para desvanecer a tela
def desvanecer_tela():
    superficie = pygame.Surface((800, 600))
    superficie.fill((0, 0, 0))

    for alpha in range(0, 300, 10):
        superficie.set_alpha(alpha)
        screen.blit(superficie, (0, 0))
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

    keys = pygame.key.get_pressed()
    if tela == "primeira":
        # Desenhar tela inicial
        screen.blit(tela_inicial, (0, 0))
        font = pygame.font.Font(None, 36)
        pressione_enter = font.render("Press ENTER to start", True, (255, 255, 255))
        screen.blit(pressione_enter, (200, 200))
        if keys[pygame.K_RETURN]:
            desvanecer_tela()
            tela = "segunda"
    if tela == "segunda":

        # Desenhar tela inicial
        screen.blit(tela_inicial, (0, 0))

        #mover personagem
        
        if keys[pygame.K_LEFT] and ivo_x > 0:
            ivo_x -= ivo_speed # Move ivo
            bg_x1 += scroll_speed # Move o cenário na direção contrária
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

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
#sys.exit()
