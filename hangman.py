import pygame
import sys

class Hangman:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,700))
        pygame.display.set_caption("Hangman")
        self.bg_color = (177,79,179)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    hg = Hangman()
    hg.run_game()