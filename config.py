import pygame

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
ivo = pygame.image.load("mini_ivo_parado.png").convert_alpha()
ivo_width = ivo.get_width()
ivo_height = ivo.get_height()

ivo_andando_1 = pygame.image.load("mini_ivo_andando1.png").convert_alpha()
ivo_andando_1_width = ivo.get_width()
ivo_andando_1_height = ivo.get_height()

ivo_andando_2 = pygame.image.load("mini_ivo_andando2.png").convert_alpha()
ivo_andando_2_width = ivo.get_width()
ivo_andando_2_height = ivo.get_height()

ivo_andando_3 = pygame.image.load("mini_ivo_andando3.png").convert_alpha()
ivo_andando_3_width = ivo.get_width()
ivo_andando_3_height = ivo.get_height()

ivo_andando_4 = pygame.image.load("mini_ivo_andando4.png").convert_alpha()
ivo_andando_4_width = ivo.get_width()
ivo_andando_4_height = ivo.get_height()

ivo_andando_5 = pygame.image.load("mini_ivo_andando5.png").convert_alpha()
ivo_andando_5_width = ivo.get_width()
ivo_andando_5_height = ivo.get_height()

ivo_andando_6 = pygame.image.load("mini_ivo_andando6.png").convert_alpha()
ivo_andando_6_width = ivo.get_width()
ivo_andando_6_height = ivo.get_height()

ivo_andando_7 = pygame.image.load("mini_ivo_andando7.png").convert_alpha()
ivo_andando_7_width = ivo.get_width()
ivo_andando_7_height = ivo.get_height()

ivo_andando_8 = pygame.image.load("mini_ivo_andando8.png").convert_alpha()
ivo_andando_8_width = ivo.get_width()
ivo_andando_8_height = ivo.get_height()

# Coordenadas iniciais do fundo
bg_x1 = 0
bg_x2 = background_width

# Coordenadas iniciais do personagem
ivo_x = 2
ivo_y = ivo_height

# Velocidade do movimento do fundo
scroll_speed = 2
ivo_speed = 2
