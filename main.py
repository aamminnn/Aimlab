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

def display_text(font, font_color, w, h, window, text ):
    text_surface = font.render(text, True, font_color)
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
end_score = True
start = True
score = 0

# timer setup
duration = 11 * 1000

# constraint area setup #NOTE to limit area of ball appears
constraint_x_left = ((window_width/2)/2)
constraint_x_right = window_width - constraint_x_left
constraint_y_top = ((window_height/2)/2)
constraint_y_bottom = window_height - constraint_y_top

# circle setup
circle_color = (173,216,230)
container_width = 40 # circle's boundaries
container_height = 40 # circle's boundaries
cointaner_x = random.randint(constraint_x_left + container_width, constraint_x_right - container_width) # point for circle at x
cointaner_y = random.randint(constraint_y_top + container_height, constraint_y_bottom - container_height) # point for circle at y

# button click
mouse_x, mouse_y = (window_width // 2, window_height // 2)

# Set up the font
font = pygame.font.SysFont(None, 48)
font_color = (182, 192, 207)

circle = Circle( circle_color)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the window with a color to wipe away anything from last frame
    window.fill((36, 38, 41))

    # RENDER YOUR GAME HERE
    # start game
    if start:
        current_time = pygame.time.get_ticks()
        display_text(font, font_color, window_width/2, window_height/6, window, text="Click on ball to start game!")
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
        window.fill((36, 38, 41))


    if game_running:
        # timer clock
        start_time = pygame.time.get_ticks() - current_time
        remaining_time = max(0, (duration - start_time)) // 1000
        # Render the countdown timer
        if remaining_time != 0:
            display_text(font, font_color, window_width/2, window_height/6, window, text=str(remaining_time))
            circle.draw(cointaner_x, cointaner_y, container_width, container_height)
            # Event of click on circle
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Get the mouse coordinates
                    mouse_x, mouse_y = pygame.mouse.get_pos()
            # check if point inside circle
            if mouse_x >= (cointaner_x) and mouse_x <=  (cointaner_x + container_width):
                if mouse_y >= (cointaner_y) and mouse_y <= (cointaner_y + container_height):
                    cointaner_x = random.randint(constraint_x_left + container_width, constraint_x_right - container_width)
                    cointaner_y = random.randint(constraint_y_top + container_height, constraint_y_bottom - container_height)
                    circle.draw(cointaner_x, cointaner_y, container_width, container_height)
                    print("Ball Hit! +1 Point ")
                    score += 1
        elif remaining_time <= 0:
            display_text(font, font_color, window_width/2, window_height/5, window, text="Times Up!")
            display_text(font, font_color, window_width/2, window_height/2, window, text=f'Your Score : {str(score)}')
            if end_score:
                print("Your Score : ", score)
                end_score = False
    
            #TODO 1.0 print score after game finish only once
            #TODO 2.0 restart game / home option
            #TODO 3.0 display real time score
            #TODO 4.0 adjust constraint area for ball to appear
            #TODO 5.0 add countdown before start game
            #TODO 6.0 add sound if ball hit and ball appear
            #TODO 7.0 change mouse cursor
            #TODO 8.0 allow player to pick time [10,30,60] seconds

    # flip() the display to put your work on window
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60



pygame.quit()


