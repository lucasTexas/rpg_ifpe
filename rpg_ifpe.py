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

class Cenarios:
    def __init__(self):
        self.ivo = Ivo()
        self.todas_as_sprites = pygame.sprite.Group()
        self.todas_as_sprites.add(self.ivo)
        self.parametro_tela = "inicial"
        self.contador_cenarios = 1
        #self.keys = pygame.key.get_pressed()
    def cenarios(self):
        if self.parametro_tela == "inicial":
            config.screen.blit(config.tela_inicial, (0, 0))
            font = pygame.font.Font(None, 36)
            pressione_enter = font.render("Press ENTER to start", True, (255, 255, 255))
            config.screen.blit(pressione_enter, (200, 200))
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_RETURN]:
                desvanecer_tela()
                self.parametro_tela = "principal"
                pygame.display.flip()
            #return 0

        elif self.parametro_tela == "principal":
            config.alea = pygame.transform.scale(config.alea, (config.alea_width*0.01, config.alea_height*0.01))
            config.screen.blit(config.background, (config.bg_x1, 0))
            config.screen.blit(config.background, (config.bg_x2, 0))
            config.screen.blit(config.background, (config.bg_x3, 0))
            config.screen.blit(config.alea, (config.alea_x, 100))
            
            

            if config.bg_x1 <= -config.background_width:
                config.bg_x1 = config.background_width
            if config.bg_x2 <= -config.background_width:
                config.bg_x2 = config.background_width
            if config.bg_x3 <= -config.background_width:
                config.bg_x3 = config.background_width

            if self.ivo.rect_x == config.background_largura and self.contador_cenarios == 1:
                self.contador_cenarios = 2
            elif self.ivo.rect_x == config.background_largura and self.contador_cenarios == 2:
                self.contador_cenarios = 3

            if self.contador_cenarios == 1:
                if self.ivo.rect_x >= config.alea_x - 50 and self.ivo.rect_x <= config.alea_x + 50:
                    font = pygame.font.Font(None, 36)
                    pressione_up = font.render("Press UP to maker", True, (255, 255, 255))
                    config.screen.blit(pressione_up, (200, 200))
                    self.keys = pygame.key.get_pressed()
                    if self.keys[pygame.K_UP]:
                        desvanecer_tela()
                        self.parametro_tela = "maker"
                        pygame.display.flip()
                self.todas_as_sprites.draw(config.screen)
                self.todas_as_sprites.update() 

            elif self.contador_cenarios == 2:
                if config.background_largura >= 600 and config.bg_x2 <= 700:
                    font = pygame.font.Font(None, 36)
                    pressione_up = font.render("Press UP to Dacal's Room", True, (255, 255, 255))
                    config.screen.blit(pressione_up, (200, 200))
                    self.keys = pygame.key.get_pressed()
                    if self.keys[pygame.K_UP]:
                        desvanecer_tela()
                        self.parametro_tela = "dacal"
                        pygame.display.flip()
                self.todas_as_sprites.draw(config.screen)
                self.todas_as_sprites.update() 

            elif self.contador_cenarios == 3:
                if config.background_largura >= 600 and config.bg_x2 <= 700:
                    font = pygame.font.Font(None, 36)
                    pressione_up = font.render("Press UP to Class Room", True, (255, 255, 255))
                    config.screen.blit(pressione_up, (200, 200))
                    self.keys = pygame.key.get_pressed()
                    if self.keys[pygame.K_UP]:
                        desvanecer_tela()
                        self.parametro_tela = "class"
                        pygame.display.flip()
                self.todas_as_sprites.draw(config.screen)
                self.todas_as_sprites.update() 





        elif self.parametro_tela == "maker":
            config.screen.blit(config.maker, (config.bg_x1, 0))
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_DOWN]:
                desvanecer_tela()
                self.parametro_tela = "principal"

    

            self.todas_as_sprites.draw(config.screen)
            self.todas_as_sprites.update() 

        elif self.parametro_tela == "dacal":
            config.screen.blit(config.dacal, (0, 0))
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_DOWN]:
                desvanecer_tela()
                self.parametro_tela = "principal"

            self.todas_as_sprites.draw(config.screen)
            self.todas_as_sprites.update()

        elif self.parametro_tela == "class":
            config.screen.blit(config.sala, (0, 0))
            self.keys = pygame.key.get_pressed()
            if self.keys[pygame.K_DOWN]:
                desvanecer_tela()
                self.parametro_tela = "principal"

            self.todas_as_sprites.draw(config.screen)
            self.todas_as_sprites.update()
            



class Ivo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_direita = []
        self.sprites_direita.append(pygame.image.load("mini_ivo_andando1.png"))
        self.sprites_direita.append(pygame.image.load("mini_ivo_andando2.png"))
        self.sprites_direita.append(pygame.image.load("mini_ivo_andando3.png"))
        self.sprites_direita.append(pygame.image.load("mini_ivo_andando4.png"))
        self.sprites_direita.append(pygame.image.load("mini_ivo_andando5.png"))
        self.sprites_direita.append(pygame.image.load("mini_ivo_andando6.png"))
        self.sprites_direita.append(pygame.image.load("mini_ivo_andando7.png"))
        self.sprites_direita.append(pygame.image.load("mini_ivo_andando8.png"))

        self.sprites_esquerda = []
        self.sprites_esquerda.append(pygame.image.load("mini_ivo_andando_esquerda8.png"))
        self.sprites_esquerda.append(pygame.image.load("mini_ivo_andando_esquerda7.png"))
        self.sprites_esquerda.append(pygame.image.load("mini_ivo_andando_esquerda6.png"))
        self.sprites_esquerda.append(pygame.image.load("mini_ivo_andando_esquerda5.png"))
        self.sprites_esquerda.append(pygame.image.load("mini_ivo_andando_esquerda4.png"))
        self.sprites_esquerda.append(pygame.image.load("mini_ivo_andando_esquerda3.png"))
        self.sprites_esquerda.append(pygame.image.load("mini_ivo_andando_esquerda2.png"))
        self.sprites_esquerda.append(pygame.image.load("mini_ivo_andando_esquerda1.png"))

        self.atual = 0
        self.image = self.sprites_direita[self.atual]
        #self.image = pygame.transform.scale(self.image, (64*1.5, 74*1.5))

        self.rect = self.image.get_rect()
        self.rect_x = 50
        self.rect_y = 200
        self.rect.topleft = self.rect_x, self.rect_y

    def update(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_RIGHT]:
            self.atual += 0.1
            if self.atual >= len(self.sprites_direita):
                self.atual = 0
                self.rect.topleft = self.rect_x, self.rect_y
            config.bg_x1 -= 2
            config.bg_x2 -= 2
            config.alea_x -= 2
            config.background_largura -= 2
            if config.background_largura <= 0:
                config.background_largura = 700
            self.image = self.sprites_direita[int(self.atual)]
        elif self.keys[pygame.K_LEFT]:
            self.atual += 0.1
            if self.atual >= len(self.sprites_direita):
                self.atual = 0
                self.rect.topleft = self.rect_x, self.rect_y
            config.bg_x1 += 2
            config.bg_x2 += 2
            config.alea_x += 2
            config.background_largura += 2
            if config.background_largura > 700:
                config.background_largura = 0
            self.image = self.sprites_esquerda[int(self.atual)]


cenarios = Cenarios()


# Loop principal
clock = pygame.time.Clock()
running = True
tela = "inicial"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cenarios.cenarios()
    print(config.background_largura)
    print(cenarios.contador_cenarios)
    #print(bg_x1)
    print(config.bg_x2)

    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
