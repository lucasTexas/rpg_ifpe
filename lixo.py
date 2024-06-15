if tela == "primeira":
    
        # Desenhar tela inicial
        config.screen.blit(config.tela_inicial, (0, 0))
        font = pygame.font.Font(None, 36)
        pressione_enter = font.render("Press ENTER to start", True, (255, 255, 255))
        config.screen.blit(pressione_enter, (200, 200))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            desvanecer_tela()
            tela == "segunda"
            