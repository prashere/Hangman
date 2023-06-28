import pygame

class Man:
    """ Loads different phases of hangman"""
    def __init__(self,hg_game):
        self.screen = hg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = hg_game.settings
        self.path = self.determine_image(0)
        self.image = pygame.image.load(self.path)
        self.image_rect = self.image.get_rect()
        self.image_rect.midright = (self.screen_rect.midright[0]-50,self.screen_rect.midright[1]-30)
        

    def create_man(self,tries):
        self.path = self.determine_image(tries)
        
        self.image = pygame.image.load(self.path)
        self.image_rect = self.image.get_rect()

        self.image_rect.midright = (self.screen_rect.midright[0]-50,self.screen_rect.midright[1]-30)
        

    def determine_image(self,tries):
        if tries == 0:
            self.path = "images/zero.bmp"
        elif tries == 1:
            self.path = "images/one.bmp"
        elif tries == 2:
            self.path = "images/two.bmp"
        elif tries == 3:
            self.path = "images/three.bmp"
        elif tries == 4:
            self.path = "images/four.bmp"
        elif tries == 5:
           self. path = "images/five.bmp"
        elif tries == 6:
           self. path = "images/six.bmp"
        return self.path

    def draw_man(self):
        self.screen.blit(self.image, self.image_rect)

        

