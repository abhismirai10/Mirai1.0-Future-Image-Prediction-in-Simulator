# Modified code to accommodate circles, squares, and triangles:
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
pygame.display.set_caption("Falling Shape Simulator")

class Shape:
    def __init__(self, shape_type="circle"):
        self.shape_type = shape_type
        
        # Define attributes based on shape type
        if self.shape_type == "circle":
            self.radius = 5
            self.x = random.randint(self.radius, WIDTH - self.radius)
            self.y = random.randint(self.radius, MIDLINE - self.radius)
        
        elif self.shape_type == "square":
            self.side = 10
            self.half_side = self.side // 2
            self.x = random.randint(self.half_side, WIDTH - self.half_side)
            self.y = random.randint(self.half_side, MIDLINE - self.half_side)
        
        elif self.shape_type == "triangle":
            self.side = 10
            self.height = int((3**0.5 / 2) * self.side)
            self.half_height = self.height // 2
            self.x = random.randint(self.side // 2, WIDTH - self.side // 2)
            self.y = random.randint(self.half_height, MIDLINE - self.half_height)
        
        self.speed = 0.5
        
    def draw(self):
        if self.shape_type == "circle":
            pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)
        elif self.shape_type == "square":
            pygame.draw.rect(screen, WHITE, (self.x - self.half_side, self.y - self.half_side, self.side, self.side))
        elif self.shape_type == "triangle":
            pygame.draw.polygon(screen, WHITE, [
                (self.x, self.y - self.half_height),
                (self.x - self.side // 2, self.y + self.half_height),
                (self.x + self.side // 2, self.y + self.half_height)
            ])
            
    def update(self):
        self.y += self.speed

def main():
    clock = pygame.time.Clock()
    shape_type = random.choice(["circle", "square", "triangle"])
    shape = Shape(shape_type)  # Generating the first shape

    iteration = 400  # To keep track of how many shapes have been generated
    frame_count = 0

    running = True
    while running and iteration < 801:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        shape.update()
        shape.draw()
        pygame.display.flip()

        if frame_count == 0:
            pygame.image.save(screen, f"X{iteration + 1}.png")
            
        frame_count += 1

        if frame_count == 30:
            pygame.image.save(screen, f"Y{iteration + 1}.png")
            iteration += 1
            frame_count = 0
            shape_type = random.choice(["circle", "square", "triangle"])
            shape = Shape(shape_type)  # Generate a new shape

        clock.tick(30)  # 30 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
