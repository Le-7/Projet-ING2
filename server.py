import pygame

class Server:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("logo-serveur.png")
        self.image = pygame.transform.scale(self.image, (80, 90))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
