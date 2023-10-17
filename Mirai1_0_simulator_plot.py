import pygame
import random
import matplotlib.pyplot as plt
import imageio

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

class Shape:
    def __init__(self):
        self.side = 10  # Side length of the square
        self.half_side = self.side // 2
        self.x = random.randint(self.half_side, WIDTH - self.half_side)  # Center x-coordinate
        self.y = random.randint(self.half_side, MIDLINE - self.half_side)  # Center y-coordinate
        self.speed = 0.5  # 5 pixels per second
        
    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x - self.half_side, self.y - self.half_side, self.side, self.side))
            
    def update(self):
        self.y += self.speed

def visualize_frames():
    # Read all the saved images into a list
    frames = [imageio.imread(f'Frame{i+1}.png') for i in range(30)]

    # Create a figure with a specific size
    fig = plt.figure(figsize=(12, 10))  # Adjusted for a 5x6 grid

    # Plot each image in a 5x6 grid
    for idx, frame in enumerate(frames, 1):
        ax = fig.add_subplot(5, 6, idx)
        ax.imshow(frame)
        ax.axis('off')  # Hide axis
        ax.set_title(f'Frame {idx}', fontsize=8)  # Display the frame number as title

    plt.tight_layout()
    plt.suptitle('Simulation Frames from 1 to 30', fontsize=16, y=1.05)  # Adjusted y-position for the title

    # Save the figure in high resolution
    plt.savefig("frames_presentation_grid.png", dpi=300, bbox_inches='tight')

    plt.show()

def main():
    clock = pygame.time.Clock()
    shape = Shape()

    frame_count = 0

    running = True
    while running and frame_count < 30:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        shape.update()
        shape.draw()
        pygame.display.flip()

        pygame.image.save(screen, f"Frame{frame_count + 1}.png")
            
        frame_count += 1

        clock.tick(30)  # 30 FPS

    pygame.quit()

    # Visualize the saved frames after the simulation ends
    visualize_frames()

if __name__ == "__main__":
    main()
