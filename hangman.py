import pygame
import sys
import random

from settings import Settings

class Hangman:
    """ Main class that runs the game """
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        pygame.display.set_caption("Hangman")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
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