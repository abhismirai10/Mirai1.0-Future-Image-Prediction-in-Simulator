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
pygame.display.set_caption("Falling Circle Simulator")

# class Shape:
#     def __init__(self):
#         self.radius = 5
#         self.x = random.randint(self.radius, WIDTH - self.radius)
#         self.y = random.randint(self.radius, MIDLINE - self.radius)
#         self.speed = 0.5  # 5 pixels per second
        
#     def draw(self):
#         pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)
            
#     def update(self):
#         self.y += self.speed

class Shape:
    def __init__(self):
        self.side = 10  # Side length of the square
        self.half_side = self.side // 2
        self.x = random.randint(self.half_side, WIDTH - self.half_side)  # Center x-coordinate
        self.y = random.randint(self.half_side, MIDLINE - self.half_side)  # Center y-coordinate
        self.speed = 0.5  # 5 pixels per second
        
    def draw(self):
        # Draw a square; (self.x - self.half_side, self.y - self.half_side) is the top-left corner of the square
        pygame.draw.rect(screen, WHITE, (self.x - self.half_side, self.y - self.half_side, self.side, self.side))
            
    def update(self):
        self.y += self.speed

def main():
    clock = pygame.time.Clock()
    shape = Shape()  # Generating the first circle

    iteration = 0  # To keep track of how many circles have been generated
    frame_count = 0

    running = True
    while running and iteration < 9:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        shape.update()
        shape.draw()
        #pygame.draw.line(screen, WHITE, (0, MIDLINE), (WIDTH, MIDLINE))
        pygame.display.flip()

        if frame_count == 0:
            pygame.image.save(screen, f"X{iteration + 1}.png")
            
        frame_count += 1

        # 1 seconds (30 frames at 30 FPS) after initial state, save the frame as label and reset for the next circle
        if frame_count == 30:
            pygame.image.save(screen, f"Y{iteration + 1}.png")
            iteration += 1
            frame_count = 0
            shape = Shape()  # Generate a new circle
            
            #time.sleep(1)  # Wait for 1 second before the new circle starts falling

        clock.tick(30)  # 30 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
