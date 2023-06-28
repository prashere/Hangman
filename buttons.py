import pygame.font
import string

class Buttons:
    def __init__(self,hg_game):
        self.screen = hg_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = hg_game.settings
        self.buttons = self.generate_button_details()
        
    def generate_button_details(self):
        # initializing an empty list
        buttons = []
        for i,letter in enumerate(string.ascii_uppercase):
            # Calculating the x and y positions
            x =150+ self.settings.button_margin + (self.settings.button_width + 2*self.settings.button_margin)*(i%13)
            y =550+ self.settings.button_margin + (self.settings.button_height + 2*self.settings.button_margin)*(i//13) 

            self.rect = pygame.Rect(x,y,self.settings.button_width,self.settings.button_height)
            self.text = self.settings.font.render(letter,True,self.settings.text_color)
            
            # adding dictionary containing button details inside the list
            buttons.append({'rect':self.rect,
                            'text':self.text,
                            'letter':letter,
                            'background_color':self.settings.button_color,
                            'foreground_color':self.settings.text_color})
        return buttons
    
    def draw_buttons(self):
        for button in self.buttons:
            if button['rect'].collidepoint(pygame.mouse.get_pos()):
                button['background_color']=self.settings.hover_color
               
            else:
                button['background_color']=self.settings.button_color
               

            pygame.draw.rect(self.screen,button['background_color'],button['rect'])
            text_rect = button['text'].get_rect(center=button['rect'].center)
            self.screen.blit(button['text'], text_rect)
            #self.screen.blit(button['text'], button['rect'])

    

