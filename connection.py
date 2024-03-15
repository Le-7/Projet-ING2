import pygame

class Connection:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), (self.start.x, self.start.y), (self.end.x, self.end.y), 2)
