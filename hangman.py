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
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Hangman")
        self.btn = Buttons(self)
        self.man = Man(self)

    def run_game(self):
        word = self.get_word()
        self.activate_word(word)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # That number 1 represents the clicking of the left mouse button
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                    self.check_mouse_position(pygame.mouse.get_pos())
            self.update_screen()

    def check_mouse_position(self,mouse_pos):
         temp = 0
         buttons=self.btn.generate_button_details()
         for button in buttons:
                if button['rect'].collidepoint(mouse_pos):
                    letter = button['letter']
         for i in range(len(self.permanent_list)):
             if (self.permanent_list[i]).upper()==letter.upper():
                 self.dynamic_list[i] = letter
                 self.list_str_converter(self.dynamic_list)
             else:
                 temp +=1
         if temp == len(self.permanent_list):
             self.tries +=1
             self.man.create_man(self.tries)
                


    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # Only draw rects and load images after filling the screen or else it won't appear 
        self.btn.draw_buttons()
        self.man.draw_man()
        self.draw_word()
        pygame.display.flip()

    def get_word(self):
        """ From the word list, it fetches a random word """
        collection = self.settings.word_list
        random_number =random.randint(0,len(collection)-1)
        print(random_number)
        word = collection[random_number]
        print(word)
        return word
    
    def activate_word(self,word):
        self.dynamic_list = []
        self.permanent_list = list(word)
        len_word = len(word)
        for i  in range(len_word):
            self.dynamic_list.append("_")
        self.list_str_converter(self.dynamic_list)
    
    def list_str_converter(self,list):
        display_string = ' '.join(str(element) for element in list)
        self.rendered_image(display_string)
    
    def rendered_image(self,string):
        self.image = self.settings.word_font.render(string,True,(0,0,0))
        self.image_rect = self.image.get_rect()

        self.image_rect.midleft = (self.screen_rect.midleft[0]+200,self.screen_rect.midleft[1])

    def draw_word(self):
        self.screen.blit(self.image,self.image_rect)

    


if __name__ == '__main__':
    hg = Hangman()
    hg.run_game()