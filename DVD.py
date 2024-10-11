import pygame
import random
import os

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Bouncing DVD Logo")

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Load image and sound from the script's directory
logo_path = os.path.join(script_dir, 'DVD.png')
logo = pygame.image.load(logo_path)
logo = pygame.transform.scale(logo, (200, 100))  # Scale image to twice its original size
logo_width, logo_height = logo.get_size()

fart_sound_path = os.path.join(script_dir, 'Fart.mp3')
fart_sound = pygame.mixer.Sound(fart_sound_path)

# Initial position and speed
margin = 10
x = random.randint(margin, WIDTH - logo_width - margin)
y = random.randint(margin, HEIGHT - logo_height - margin)
dx = random.choice([-1, 1]) * random.uniform(0.5, 2)
dy = random.choice([-1, 1]) * random.uniform(0.5, 2)

# Initial color
tint_color = [random.randint(0, 255) for _ in range(3)]

# Function to change the color of the image
def tint_image(image, tint_color):
    image = image.copy()
    tint_surf = pygame.Surface(image.get_size())
    tint_surf.fill(tint_color)
    image.blit(tint_surf, (0, 0), special_flags=pygame.BLEND_MULT)
    return image

# Function to change color a bit faster
def change_color_faster(color):
    for i in range(3):
        color[i] += random.choice([-3, -2, -1, 1, 2, 3])
        if color[i] > 255:
            color[i] = 255
        if color[i] < 0:
            color[i] = 0

# Main loop
running = True
fullscreen = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    # Update position
    x += dx
    y += dy

    # Bounce off walls, keeping the logo away from corners
    if x <= margin or x + logo_width >= screen.get_width() - margin:
        dx = -dx
        x += dx
        fart_sound.play()
    if y <= margin or y + logo_height >= screen.get_height() - margin:
        dy = -dy
        y += dy
        fart_sound.play()

    # Change color a bit faster
    change_color_faster(tint_color)
    tinted_logo = tint_image(logo, tint_color)

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(tinted_logo, (x, y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
