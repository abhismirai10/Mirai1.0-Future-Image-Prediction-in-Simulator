import time
import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH = 50
HEIGHT = 50
MIDLINE = HEIGHT // 2

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falling Circle Simulator")

class Circle:
    def __init__(self):
        self.diameter_choice = random.choice([5, 10, 15, 20])
        self.radius = self.diameter_choice // 2
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, MIDLINE - self.radius)
        self.speed = self.diameter_choice * 0.03  # Speed is proportional to diameter
        
    def draw(self):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)
            
    def update(self):
        self.y += self.speed

def main():
    clock = pygame.time.Clock()
    circle = Circle()  # Generating the first circle

    iteration = 800  # To keep track of how many circles have been generated
    frame_count = 0

    running = True
    while running and iteration < 1600:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        circle.update()
        circle.draw()
        pygame.display.flip()

        if frame_count == 0:
            pygame.image.save(screen, f"X{iteration + 1}.png")

        # if frame_count == 3:
        #     pygame.image.save(screen, f"X_2{iteration + 1}.png")

        # if frame_count == 6:
        #     pygame.image.save(screen, f"X_3{iteration + 1}.png")

        frame_count += 1

        if frame_count == 30:
            pygame.image.save(screen, f"Y{iteration + 1}.png")
            iteration += 1
            frame_count = 0
            circle = Circle()  # Generate a new circle

        clock.tick(30)  # 30 FPS
        

    pygame.quit()

if __name__ == "__main__":
    main()
