import string
import pygame.font 
import pygame

pygame.init()
from settings import Settings
buttons = []
settings = Settings()
for i,letter in enumerate(string.ascii_uppercase):
            # Calculating the x and y positions
            x = (settings.button_width + 2*settings.button_margin)*(i%13)
            y = (settings.button_height + 2*settings.button_margin)*(i//13) 

            rect = pygame.Rect(x,y,settings.button_width,settings.button_height)
            fonta = pygame.font.SysFont(None, 35)
            text = fonta.render(letter,True,settings.text_color,settings.button_color)
            
            # adding dictionary containing button details inside the list
            buttons.append({'rect':rect,
                            'text':text,
                            'letter':letter})
print (buttons)