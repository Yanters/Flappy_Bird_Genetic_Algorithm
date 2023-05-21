import pygame

class BackGround:
    bg_img = pygame.image.load("images/bg.png").convert_alpha()

    # empty constructor
    def __init__(self):
        pass

    def draw(self, window):
        window.blit(self.bg_img, (0, 0))