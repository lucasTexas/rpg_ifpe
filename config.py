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
background_largura = background.get_width()
background_height = background.get_height()

maker = pygame.image.load("maker.jpeg").convert()
maker_width = maker.get_width()
maker_height = maker.get_height()

dacal = pygame.image.load("sala_de_dacal.jpeg").convert()
dacal_width = maker.get_width()
dacal_height = maker.get_height()

sala = pygame.image.load("sala_de_aula.jpeg").convert()
sala_width = sala.get_width()
sala_height = sala.get_height()

marlon = pygame.image.load("marlon_parado.png").convert()
marlon_width = marlon.get_width()
marlon_height = marlon.get_height()





# Coordenadas iniciais do fundo
bg_x1 = 0
bg_x2 = background_width
bg_x3 = bg_x2 + background_width


# Velocidade do movimento do fundo
scroll_speed = 2
ivo_speed = 2

#if tela == "primeira":
 #   # Desenhar tela inicial
  #  config.screen.blit(config.tela_inicial, (0, 0))
   # font = pygame.font.Font(None, 36)
    #pressione_enter = font.render("Press ENTER to start", True, (255, 255, 255))
    #config.screen.blit(pressione_enter, (200, 200))
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_RETURN]:
#        desvanecer_tela()
 #       tela = "segunda"
  #          
#if tela == "segunda":
#	todas_as_sprites.draw(config.screen)
 #   todas_as_sprites.update()
#
#    # Reposicionando o fundo
#    if config.bg_x1 <= -config.background_width:
#        bg_x1 = config.background_width
 #   if config.bg_x2 <= -config.background_width:
  #      bg_x2 = config.background_width
#
 #   # Desenhar o fundo
  #  config.screen.blit(config.background, (config.bg_x1, 0))
   # config.screen.blit(config.background, (config.bg_x2, 0))
  #  # Desenhar o personagem
   # config.screen.blit(config.ivo, (200, 200))

 #   keys = pygame.key.get_pressed()
