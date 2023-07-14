# Example file showing a basic pygame "game loop"
import pygame
import random
from pygame.locals import *
import logging
from log_file import log
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

class Button:
    def __init__(self, color, text, font, text_color, x, y, w, h):
        self.color = color
        self.text = text
        self.font = font
        self.text_color = text_color
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self):
        pygame.draw.rect(window, self.color, self.rect)
        text = self.font.render(self.text, True, self.text_color)
        text_rect = text.get_rect(center=self.rect.center)
        window.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)
    
def reset_true(*options):
    for value in options:
        value = True

def reset_false(*options):
    for value in options:
        value = False

def main():
    # pygame setup
    pygame.init()
    window_width = 1200
    window_height = 600
    global window
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("AimLab")
    clock = pygame.time.Clock()
    score = 0

    # option
    running = True
    game_running = False
    end_score = True
    home = True
    timer = True
    display_score = True
    start_countdown = True

    # Set up the font
    font = pygame.font.SysFont(None, 48)
    font_score = pygame.font.SysFont(None,30)
    font_color = (182, 192, 207)

    # timer setup
    # duration = 11 * 1000
    duration = 4 * 1000 # testing purpose
    countdown_duration = 4 * 1000

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

    # button setup
    button_width = 200
    button_height = 40

    # button click
    mouse_x, mouse_y = (window_width // 2, window_height // 2) # to initialize a value

    # create object
    circle = Circle( circle_color)
    button_restart = Button(
        color=(57, 59, 64), 
        text="Restart", 
        font=font, 
        text_color=(182, 192, 207), 
        x=window_width/4, 
        y=window_height - window_height/6, 
        w=button_width, 
        h=button_height)
    
    button_home = Button(
        color=(57, 59, 64), 
        text="Home", 
        font=font, 
        text_color=(182, 192, 207), 
        x=(window_width - window_width/2) + button_width - 100, 
        y=window_height - window_height/6, 
        w=button_width, 
        h=button_height)
    
    # Logging report
    log("\n-----------SESSION STARTING--------------")

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
        if home:
            # current_time = pygame.time.get_ticks()
            display_text(font, font_color, window_width/2, window_height/6, window, text="Click on ball to start game!")
            cointaner_x_start = window_width/2
            cointaner_y_start = window_height/2
            circle.draw(cointaner_x_start, cointaner_y_start, container_width, container_height)
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x >= (cointaner_x_start) and mouse_x <=  (cointaner_x_start + container_width):
                    if mouse_y >= (cointaner_y_start) and mouse_y <= (cointaner_y_start + container_height):
                        if not game_running:
                            # Start the game here
                            # print("Game started!")
                            log("Game started!")
                            game_running = True
                            home = False
            window.fill((36, 38, 41))


        if game_running:
            # countdown before start game
            if start_countdown:
                countdown = True
                countdown_current_time = pygame.time.get_ticks()
                start_countdown = False
                start = False
            if countdown:
                countdown_start_time = pygame.time.get_ticks() - countdown_current_time
                countdown_time = max(0, (countdown_duration - countdown_start_time)) // 1000
                display_text(font, font_color, window_width/2, window_height/2, window, text=f'Game starting in {countdown_time}')
                if countdown_time == 0:
                    start = True
                    current_time = pygame.time.get_ticks()
                    countdown = False
            if start:
                # if remaining_time != 0:
                if timer == True:
                    countdown = False
                    start_time = pygame.time.get_ticks() - current_time 
                    remaining_time = max(0, (duration - start_time)) // 1000
                    # Render the game timer
                    display_text(font, font_color, window_width/2, window_height/6, window, text=str(remaining_time))
                    circle.draw(cointaner_x, cointaner_y, container_width, container_height)
                    if display_score:
                        display_text(font_score, font_color, window_width/4, window_height/4, window, text=f'Score : {score}')
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
                            # print("Ball Hit! +1 Point ")
                            log("Ball Hit! +1 Point ")
                            score += 1
                    if remaining_time == 0:
                        timer = False
                # elif remaining_time == 0:
                elif timer == False:
                    display_score = False
                    display_text(font, font_color, window_width/2, window_height/5, window, text="Times Up!")
                    display_text(font, font_color, window_width/2, window_height/2, window, text=f'Your Score : {str(score)}')
                    button_restart.draw()
                    button_home.draw()
                    if end_score:
                        print("Your Score : ", score)
                        log(f"Your Score : {score}")
                        end_score = False
                    mouse_pos_button = (window_width/2, window_height/2)
                    if event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:  # Left mouse button
                            # Get the mouse coordinates
                            if event.button == 1:
                                mouse_pos_button = pygame.mouse.get_pos()
                    # if restart:
                    if button_restart.is_clicked(mouse_pos_button):
                        timer = True
                        display_score = True
                        start_countdown = True
                        score = 0
                        print("Game Restart. Try Your Best!")
                    elif button_home.is_clicked(mouse_pos_button):
                        timer = True
                        display_score = True
                        home = True
                        game_running = False
                        start_countdown = True
                        score = 0
                        print("Go Home")

                        
                        
                
                
        
                
                #TODO 4.0 log report output
                #TODO 6.0 add sound if ball hit and ball appear
                #TODO 7.0 change mouse cursor
                #TODO 8.0 allow player to pick time [10,30,60] seconds

        # flip() the display to put your work on window
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60



    pygame.quit()
    log("\n-----------SESSION ENDED--------------\n\n")


if __name__ == '__main__':
    main()


