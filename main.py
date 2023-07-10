# Example file showing a basic pygame "game loop"
import pygame
import random
from pygame.locals import *
import sys

class Circle:
    def __init__(self, color):
        self.color = color

    def draw(self, x, y, w, h):
        pygame.draw.ellipse(window, self.color, (x, y, w, h))

def display_text(font, w, h, window, text ):
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(w,h))
    window.blit(text_surface, text_rect)

# pygame setup
pygame.init()
window_width = 1200
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
running = True
game_running = False
start = True

# timer setup
duration = 11 * 1000

# circle setup
constraint_x_left = ((window_width/2)/2)
constraint_x_right = window_width - constraint_x_left
constraint_y_top = ((window_height/2)/2)
constraint_y_bottom = window_height - constraint_y_top
circle_color = (173,216,230)
container_width = 40
container_height = 40
cointaner_x = random.randint(constraint_x_left + container_width, constraint_x_right - container_width)
cointaner_y = random.randint(constraint_y_top + container_height, constraint_y_bottom - container_height)


# button click
mouse_x, mouse_y = (window_width // 2, window_height // 2)

# Set up the font
font = pygame.font.SysFont(None, 48)

circle = Circle( circle_color)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the window with a color to wipe away anything from last frame
    window.fill("purple")

    # RENDER YOUR GAME HERE
    # start game
    if start:
        current_time = pygame.time.get_ticks()
        display_text(font, window_width/2, window_height/6, window, text="Click on ball to start game!")
        cointaner_x_start = window_width/2
        cointaner_y_start = window_height/2
        circle.draw(cointaner_x_start, cointaner_y_start, container_width, container_height)
    if event.type == MOUSEBUTTONDOWN:
        # print("DRAWED")
        if event.button == 1:  # Left mouse button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x >= (cointaner_x_start) and mouse_x <=  (cointaner_x_start + container_width):
                if mouse_y >= (cointaner_y_start) and mouse_y <= (cointaner_y_start + container_height):
                    if not game_running:
                        # Start the game here
                        print("Game started!")
                        game_running = True
                        start = False
        window.fill('purple')


    if game_running:
        # timer clock
        start_time = pygame.time.get_ticks() - current_time
        print(start_time)
        # remaining_time = max(0, (duration - pygame.time.get_ticks())) // 1000
        remaining_time = max(0, (duration - start_time)) // 1000
        # Render the countdown timer
        if remaining_time != 0:
            display_text(font, window_width/2, window_height/6, window, text=str(remaining_time))
            circle.draw(cointaner_x, cointaner_y, container_width, container_height)
            # Event of click on circle
            if event.type == MOUSEBUTTONDOWN:
                # print("DRAWED")
                if event.button == 1:  # Left mouse button
                    # Get the mouse coordinates
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # print("POS ",mouse_x," ",mouse_y)
                    # print("circle ", cointaner_x, cointaner_y)
            # check if point inside circle
            if mouse_x >= (cointaner_x) and mouse_x <=  (cointaner_x + container_width):
                if mouse_y >= (cointaner_y) and mouse_y <= (cointaner_y + container_height):
                    cointaner_x = random.randint(constraint_x_left + container_width, constraint_x_right - container_width)
                    cointaner_y = random.randint(constraint_y_top + container_height, constraint_y_bottom - container_height)
                    circle.draw(cointaner_x, cointaner_y, container_width, container_height)
                    print("INSIDE ")
        elif remaining_time <= 0:
            display_text(font, window_width/2, window_height/5, window, text="Time Reached!")
    
    # circle.draw(cointaner_x, cointaner_y, container_width, container_height)
    # if event.type == MOUSEBUTTONDOWN:
    #     print("DRAWED")
    #     if event.button == 1:  # Left mouse button
    #         # Get the mouse coordinates
    #         mouse_x, mouse_y = pygame.mouse.get_pos()
    #         # print("POS ",mouse_x," ",mouse_y)
    #         # print("circle ", cointaner_x, cointaner_y)
    # # check if point inside circle
    # if mouse_x >= (cointaner_x) and mouse_x <=  (cointaner_x + container_width):
    #     if mouse_y >= (cointaner_y) and mouse_y <= (cointaner_y + container_height):
    #         cointaner_x = random.randint(constraint_x_left + container_width, constraint_x_right - container_width)
    #         cointaner_y = random.randint(constraint_y_top + container_height, constraint_y_bottom - container_height)
    #         circle.draw(cointaner_x, cointaner_y, container_width, container_height)
    #         # print("INSIDE ")

    # flip() the display to put your work on window
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    

pygame.quit()


