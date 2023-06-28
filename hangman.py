import pygame
import sys
import random

from settings import Settings
from buttons import Buttons
from man import Man

class Hangman:
    """ Main class that runs the game """
    def __init__(self):
        pygame.init()
        self.tries = 0
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        pygame.display.set_caption("Hangman")
        self.btn = Buttons(self)
        self.man = Man(self)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # Only draw rects and load images after filling the screen or else it won't appear 
        self.btn.draw_buttons()
        self.man.draw_man()
        pygame.display.flip()

    def get_word(self):
        """ From the word list, it fetches a random word """
        collection = self.settings.word_list
        random_number =random.randint(0,len(collection)-1)
        word = collection[random_number]
        return word


if __name__ == '__main__':
    hg = Hangman()
    hg.run_game()