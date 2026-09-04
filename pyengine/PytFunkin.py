import pygame
import sys
import os

pygame.init()


script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "pyt.png")

if not os.path.exists(icon_path):
    print(f"Error: '{icon_path}' not found.")
    pygame.quit()
    sys.exit()

try:
    icon_surface = pygame.image.load(icon_path)  
except pygame.error as e:
    print(f"Failed to load icon: {e}")
    pygame.quit()
    sys.exit()


screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("MIT Pyt Funkin'")
pygame.display.set_icon(icon_surface.convert_alpha())  


fullscreen = False
bg_color = (30, 30, 30)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                # Toggle fullscreen
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

        elif event.type == pygame.VIDEORESIZE and not fullscreen:
         
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    screen.fill(bg_color)
    pygame.display.flip()

pygame.quit()
