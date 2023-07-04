import pygame
from pygame.locals import *
import sys
import random
from time import sleep

from settings import Settings
from buttons import Buttons
from man import Man

class Hangman:
    """ Main class that runs the game """
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        # Initialize sounds
        self.win_sound = pygame.mixer.Sound("sounds/win.wav")
        self.lose_sound =  pygame.mixer.Sound("sounds/lose.wav")

        # Initializing variables
        self.tries = 0
        self.letter = None

        # Setting class's object
        self.settings = Settings()

        # Creating a screen, setting it s caption amd calculating its rect
        self.screen = pygame.display.set_mode((self.settings.width,self.settings.height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Hangman")

        # Button and Man classes's objects
        self.btn = Buttons(self)
        self.man = Man(self)
       

    def run_game(self):
        """ The method that is called to run the game """
        self.flag_correct = False
        self.word = self.get_word()
        self.activate_word(self.word)

        # Initializing flag
        self.game_active = True

        while self.game_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # That number 1 represents the clicking of the left mouse button
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button ==1:
                    self.check_mouse_position(pygame.mouse.get_pos())
            if self.tries < 6:
                self.update_screen()
                # Checks if the user got the word correct
                check_list = list((element.upper() for element in self.permanent_list))
                if self.dynamic_list == check_list:
                    self.flag_correct = True
                    self.win_sound.play()
                    self.update_screen()
                    sleep(1)
                    self.reset_game()
            elif self.tries == 6:
                self.game_active = False
                self.lose_sound.play()
                self.update_screen()
                sleep(1)
                self.reset_game()

    def reset_game(self):
        """ Resets the entire game"""
        self.tries = 0 
        self.man.create_man(self.tries)
        self.run_game()

    def draw_correct_answer(self,msg):
        self.word_image = self.settings.word_font.render(msg,True,(0,0,0))
        self.word_image_rect = self.word_image.get_rect()
        self.word_image_rect = pygame.Rect(self.screen_rect.midtop[0]-150, self.screen_rect.midtop[1]+30,400,200)

        self.clear_rect()
        self.screen.blit(self.word_image,self.word_image_rect)
       
    def clear_rect(self):
        clear_rect = pygame.Rect(
        self.word_image_rect.left,
        self.word_image_rect.top,
        self.word_image_rect.width,
        self.word_image_rect.height)
        self.screen.fill(self.settings.bg_color,clear_rect)


    def check_mouse_position(self,mouse_pos):
         temp =0
         buttons=self.btn.generate_button_details()
         for button in buttons:
                if button['rect'].collidepoint(mouse_pos):
                    self.letter = button['letter']
         for i in range(len(self.permanent_list)):
             if self.letter is not None:
                if (self.permanent_list[i]).upper()==self.letter.upper():
                    self.dynamic_list[i] = self.letter
                    self.list_str_converter(self.dynamic_list)
                else:
                    temp +=1
         if temp == len(self.permanent_list):
             self.tries +=1
             self.man.create_man(self.tries)
        

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.draw_correct_answer(self.hint)
        # Only draw rects and load images after filling the screen or else it won't appear 
        if not self.game_active:
            self.draw_correct_answer("Correct word is "+self.word)
        elif self.flag_correct:
            self.draw_correct_answer("GOOD JOB !")
        
        self.btn.draw_buttons()
        self.man.draw_man()
        self.draw_word()
        pygame.display.flip()

    def get_word(self):
        """ From the word list, it fetches a random word """
        collection = self.settings.word_list
        random_number =random.randint(0,len(collection)-1)
        self.hint = self.show_hint(random_number)
        print(random_number)
        word = collection[random_number]
        print(word)
        return word
    
    def show_hint(self,number):
        if number >=0 and number<=49:
            self.hint = "It's a fruit !"
        elif number >=50 and number <=100:
            self.hint= "It's a vegetable !"
        elif number >=101 and number <= 149:
            self.hint = "It's an animal !"
        elif number>=150 and number<=198:
            self.hint = "It's a bird !"
        else:
            self.hint = "It's a color !"
        return self.hint
    
    
    def activate_word(self,word):
        """  Displays underscores for each letter of the word"""
        self.dynamic_list = []
        self.permanent_list = list(word)
        len_word = len(word)
        for i  in range(len_word):
            self.dynamic_list.append("_")
        self.list_str_converter(self.dynamic_list)
    
    def list_str_converter(self,list):
        """ Converts the list to a string """
        display_string = ' '.join(str(element) for element in list)
        self.rendered_image(display_string)
    
    def rendered_image(self,string):
        self.image = self.settings.word_font.render(string,True,(0,0,0))
        self.image_rect = self.image.get_rect()

        self.image_rect.midleft = (self.screen_rect.midleft[0]+200,self.screen_rect.midleft[1])

    def draw_word(self):
        self.screen.blit(self.image,self.image_rect)

 # If this is the main module being executed, creates an aboject of Hangman class
 # Then it runs the run_game() method to start the game   
if __name__ == '__main__':
    hg = Hangman()
    hg.run_game()