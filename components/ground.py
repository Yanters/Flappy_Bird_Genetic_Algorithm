import pygame

class Ground:
    ground_img = pygame.image.load("images/ground.png").convert_alpha()

    def __init__(self, ground_speed):
        self.ground_speed = ground_speed
        self.ground_scroll = 0

    def draw(self, window, win_height, win_width):
        window.blit(self.ground_img, (self.ground_scroll,
                                      win_height - self.ground_img.get_height()))
        self.ground_scroll -= self.ground_speed
        if abs(self.ground_scroll) > self.ground_img.get_width() - win_width:
            self.ground_scroll = 0