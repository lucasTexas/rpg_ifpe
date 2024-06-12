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
        self.image = pygame.transform.scale(self.image, (64*1.5, 74*1.5))

        self.rect = self.image.get_rect()
        self.rect_x = 50
        self.rect_y = 200
        self.rect.topleft = self.rect_x, self.rect_y

    def update(self):
        if keys[pygame.K_RIGHT]:
            self.atual += 0.1
            if self.atual >= len(self.sprites_direita):
                self.atual = 0
                self.rect.topleft = self.rect_x, self.rect_y
            config.bg_x1 -= 2
            config.bg_x2 -= 2
            self.image = self.sprites_direita[int(self.atual)]
        elif keys[pygame.K_LEFT]:
            self.atual += 0.1
            if self.atual >= len(self.sprites_direita):
                self.atual = 0
                self.rect.topleft = self.rect_x, self.rect_y
            config.bg_x1 += 2
            config.bg_x2 += 2
            self.image = self.sprites_esquerda[int(self.atual)]


todas_as_sprites = pygame.sprite.Group()
ivo = Ivo()
todas_as_sprites.add(ivo)



# Loop principal
clock = pygame.time.Clock()
running = True
tela = "primeira"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    config.screen.blit(config.background, (config.bg_x1, 0))
    config.screen.blit(config.background, (config.bg_x2, 0))

    if config.bg_x1 <= -config.background_width:
        bg_x1 = config.background_width
    if config.bg_x2 <= -config.background_width:
        bg_x2 = config.background_width
    
    todas_as_sprites.draw(config.screen)
    keys = pygame.key.get_pressed()
    
    todas_as_sprites.update()   






    # Atualizar a tela
    pygame.display.flip()
    clock.tick(60)

# Encerrar o Pygame
pygame.quit()
