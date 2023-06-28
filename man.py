import pygame

class Man:
    """ Loads different phases of hangman"""
    def __init__(self,hg_game):
        self.screen = hg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = hg_game.settings
        self.tries = hg_game.tries
        path = self.determine_image(self.tries)
        
        self.image = pygame.image.load(path)
        self.image_rect = self.image.get_rect()

        self.image_rect.midright = (self.screen_rect.midright[0]-50,self.screen_rect.midright[1]-30)

    def determine_image(self,tries):
        if tries == 0:
            path = "images/zero.bmp"
        elif tries == 1:
            path = "images/one.bmp"
        elif tries == 2:
            path = "images/two.bmp"
        elif tries == 3:
            path = "images/three.bmp"
        elif tries == 4:
            path = "images/four.bmp"
        elif tries == 5:
            path = "images/five.bmp"
        elif tries == 6:
            path = "images/six.bmp"
        return path

    def draw_man(self):
        self.screen.blit(self.image, self.image_rect)

        

