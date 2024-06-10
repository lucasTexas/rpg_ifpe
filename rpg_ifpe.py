import pygame
from config import *
from functions import *
#import sys

# Inicializando o Pygame
pygame.init()

    
# Loop principal
clock = pygame.time.Clock()
running = True
tela = "primeira"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    if tela == "primeira":
        build_tela_inicial()
        tela = "segunda"
            
    if tela == "segunda":
        build_tela_principal()

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
#sys.exit()
