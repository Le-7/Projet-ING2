import pygame
from computer import Computer
from server import Server
from connection import Connection
from scheduling import *
import threading

# Initialisation de Pygame
pygame.init()

# Taille de l'écran
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0,0,0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (192, 192, 192)


def display_hovered_computer_info(screen, hovered_computer):
    # Créez une surface de texte pour afficher les informations de l'ordinateur
        font = pygame.font.Font(None, 24)  # Choisissez une police et une taille de texte

    # Affichage des coordonnées de l'ordinateur
        position_text_surface = font.render(f"Position: ({hovered_computer.x}, {hovered_computer.y})", True, WHITE, BLACK)
        position_text_rect = position_text_surface.get_rect()
        position_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)  # Positionnez le texte en bas de l'écran
        screen.blit(position_text_surface, position_text_rect)

    # Affichage du niveau de batterie
        battery_text_surface = font.render(f"Battery Level: {hovered_computer.battery_level:.2f}", True, WHITE, BLACK)
        battery_text_rect = battery_text_surface.get_rect()
        battery_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)  # Positionnez le texte au-dessus du précédent
        screen.blit(battery_text_surface, battery_text_rect)

    # Affichage de la température
        temperature_text_surface = font.render(f"Temperature: {hovered_computer.temperature:.2f}", True, WHITE, BLACK)
        temperature_text_rect = temperature_text_surface.get_rect()
        temperature_text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 90)  # Positionnez le texte au-dessus du précédent
        screen.blit(temperature_text_surface, temperature_text_rect)

# Fonction principale pour simuler le réseau
def main():
    # Création de la fenêtre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Simulation de réseau")

    # Création du serveur
    server = Server(SCREEN_WIDTH // 2, 50)

    # Création des ordinateurs pour les sous-réseaux
    connections = []
    main_computers = []
    subnet_computers = []
    num_subnet_computers = [5, 4, 3]  # Nombre d'ordinateurs dans chaque sous-réseau
    subnet_positions = [(200, 200), (400, 400), (600, 200)]  # Positions des ordinateurs principaux de chaque sous-réseau
    for i in range(3):  # Boucle pour créer les ordinateurs principaux de chaque sous-réseau
        main_computer = Computer(subnet_positions[i][0], subnet_positions[i][1])
        main_computers.append(main_computer)

        # Création des ordinateurs du sous-réseau
        spacing = 70  # Espacement entre les ordinateurs du sous-réseau
        for j in range(num_subnet_computers[i]):
            x = subnet_positions[i][0] + (j - (num_subnet_computers[i] - 1) / 2) * spacing
            y = subnet_positions[i][1] + 100
            computer = Computer(x, y)
            subnet_computers.append(computer)
            connections.append(Connection(main_computer, computer))

    # Création des connexions entre le serveur et les ordinateurs principaux de chaque sous-réseau
    for computer in main_computers:
        connections.append(Connection(server, computer))

    # Choix de la stratégie d'ordonnancement
    scheduling_strategy =  select_scheduling_strategy()
    Task= 0    #100% de la tache initialement
    running = True
    choice = True

    while running:
        
        if Task > 0 :
            Task = scheduling_strategy.schedule(subnet_computers,Task)
        mouse_pos = pygame.mouse.get_pos()
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Dessin sur l'écran
        screen.fill(GREY)
        server.draw(screen)
        hovered_computer = None
        for computer in subnet_computers:
            computer.draw(screen)
            if computer.is_hovered(mouse_pos):
                hovered_computer = computer  # Stocke l'ordinateur survolé

        # Affichage des informations de l'ordinateur survolé
        if hovered_computer:
            display_hovered_computer_info(screen, hovered_computer)

        for connection in connections:
            connection.draw(screen)
        pygame.display.flip()

        # Limiter le nombre d'images par seconde
        pygame.time.Clock().tick(60)

        if choice :
            Task= float(input("Niveau de puissance du calcul en pourcentage : "))
            choice = False


    # Quitter Pygame
    pygame.quit()

if __name__ == "__main__":
    main()

def select_scheduling_strategy():
    print("Choose a scheduling strategy:")
    print("1. Random Scheduling")
    print("2. Round Robin Scheduling")
    print("3. Priority Scheduling")
    print("4. Lowest Battery Scheduling")
    print("5. Temperature Control Scheduling")
    print("6. Strength Based Scheduling")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        return RandomScheduling()
    elif choice == '2':
        return RoundRobinScheduling()
    elif choice == '3':
        return PriorityScheduling()
    elif choice == '4':
        return LowestBatteryScheduling()
    elif choice == '5':
        return TemperatureControlScheduling()
    elif choice == '6':
        return StrengthBasedScheduling()
    else:
        print("Invalid choice. Using default Random Scheduling.")
        return RandomScheduling()