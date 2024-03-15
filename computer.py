import pygame
import time

class Computer:
    def __init__(self, x, y, battery_capacity=100, temperature=25, strength =1):
        self.x = x
        self.y = y
        self.image = pygame.image.load("logo-ordinateur.png")
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.powered_on = False
        self.battery_capacity = battery_capacity
        self.battery_level = self.battery_capacity
        self.temperature = temperature
        self.strength = strength
        self.thread = None  # Ajoute un attribut pour stocker le thread de calcul

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if self.powered_on:
            pygame.draw.circle(screen, (0, 255, 0), (self.x + 35, self.y + 10), 5)
        else:
            pygame.draw.circle(screen, (255, 0, 0), (self.x + 35, self.y + 10), 5)

    def calculate(self, percentage):
        print("Je fais ce pourcentage de calcul : "+str(percentage))
        self.powered_on = True
        self.battery_level -= percentage/10
        self.temperature += percentage/10
        time.sleep(percentage/self.strength)
        self.powered_on = False

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
