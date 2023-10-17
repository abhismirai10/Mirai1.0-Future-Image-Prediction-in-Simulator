import pygame
import random
import time

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
pygame.display.set_caption("Falling Star Simulator")

class Shape:
    def __init__(self):
        self.size = 10  # Size of the star (from center to an outer point)
        self.x = random.randint(self.size, WIDTH - self.size)
        self.y = random.randint(self.size, MIDLINE - self.size)
        self.speed = 0.5  # 5 pixels per second
        
    def draw_star(self, x, y, size):
        # Create the points for the star
        points = [
            (x, y - size),
            (x + size * 0.24, y - size * 0.38),
            (x + size, y),
            (x + size * 0.61, y + size * 0.36),
            (x + size * 0.71, y + size),
            (x, y + size * 0.6),
            (x - size * 0.71, y + size),
            (x - size * 0.61, y + size * 0.36),
            (x - size, y),
            (x - size * 0.24, y - size * 0.38)
        ]
        pygame.draw.polygon(screen, WHITE, points)
        
    def draw(self):
        self.draw_star(self.x, self.y, self.size)
            
    def update(self):
        self.y += self.speed

def main():
    clock = pygame.time.Clock()
    shape = Shape()  # Generating the first star

    iteration = 0  # To keep track of how many stars have been generated
    frame_count = 0

    running = True
    while running and iteration < 9:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        shape.update()
        shape.draw()
        pygame.display.flip()

        if frame_count == 0:
            pygame.image.save(screen, f"X{iteration + 1}.png")

        # if frame_count == 3:
        #     pygame.image.save(screen, f"X_2{iteration + 1}.png")

        # if frame_count == 6:
        #     pygame.image.save(screen, f"X_3{iteration + 1}.png")

        frame_count += 1

        # 1 seconds (30 frames at 30 FPS) after initial state, save the frame as label and reset for the next star
        if frame_count == 30:
            pygame.image.save(screen, f"Y{iteration + 1}.png")
            iteration += 1
            frame_count = 0
            shape = Shape()  # Generate a new star
            
        clock.tick(30)  # 30 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
