import pygame.font

class Settings:
    """ COntains all the settings of the game"""
    def __init__(self):
        # Screen settings
        self.height = 700
        self.width = 1200
        self.bg_color = (177,79,179)

        # words to be used for the game
        self.word_list = ['apple', 'banana', 'orange', 'grape', 'watermelon', 'strawberry', 'pineapple', 'mango', 'kiwi', 'papaya',
    'pear', 'cherry', 'plum', 'peach', 'apricot', 'blueberry', 'raspberry', 'blackberry', 'cranberry', 'lemon',
    'lime', 'coconut', 'avocado', 'fig', 'passion fruit', 'guava', 'pomegranate', 'dragon fruit', 'melon', 'kiwifruit',
    'starfruit', 'lychee', 'tangerine', 'grapefruit', 'persimmon', 'jackfruit', 'date', 'nectarine', 'apricot', 'quince',
    'blackcurrant', 'boysenberry', 'gooseberry', 'kiwano', 'mangosteen', 'mulberry', 'olive', 'pawpaw', 'prickly pear',
    'rhubarb', 'carrot', 'potato', 'tomato', 'broccoli', 'cabbage', 'cauliflower', 'spinach', 'onion', 'garlic', 'pepper',
    'lettuce', 'cucumber', 'zucchini', 'eggplant', 'green bean', 'pea', 'corn', 'radish', 'beetroot', 'asparagus',
    'celery', 'leek', 'sweet potato', 'pumpkin', 'squash', 'artichoke', 'brussels sprout', 'kale', 'okra', 'mushroom',
    'turnip', 'yam', 'cassava', 'fennel', 'bamboo shoot', 'rhubarb', 'endive', 'bok choy', 'parsnip', 'ginger', 'horseradish',
    'parsley', 'shallot', 'watercress', 'radicchio', 'arugula', 'chard', 'broccolini', 'cactus', 'chicory', 'daikon' 'dog', 'cat', 'lion', 'tiger', 'elephant', 'giraffe', 'monkey', 'kangaroo', 'zebra', 'hippopotamus',
    'rhinoceros', 'crocodile', 'alligator', 'penguin', 'koala', 'panda', 'bear', 'wolf', 'fox', 'hyena',
    'jaguar', 'leopard', 'cheetah', 'deer', 'moose', 'gazelle', 'antelope', 'camel', 'buffalo', 'cow',
    'horse', 'sheep', 'goat', 'pig', 'rabbit', 'squirrel', 'hamster', 'mouse', 'rat', 'guinea pig',
    'chimpanzee', 'orangutan', 'gorilla', 'seal', 'dolphin', 'whale', 'turtle', 'cobra', 'eagle', 'hawk''sparrow', 'parrot', 'pigeon', 'ostrich', 'peacock', 'flamingo', 'hummingbird', 'owl', 'swan', 'duck',
    'goose', 'eagle', 'hawk', 'vulture', 'woodpecker', 'robin', 'crow', 'seagull', 'pelican', 'canary',
    'blue jay', 'magpie', 'kingfisher', 'finch', 'toucan', 'dove', 'swallow', 'penguin', 'kiwi', 'raven',
    'starling', 'stork', 'sparrowhawk', 'heron', 'blackbird', 'nightingale', 'crane', 'rooster', 'turkey',
    'macaw', 'cockatoo', 'gull', 'osprey', 'cormorant', 'puffin', 'warbler', 'ibis', 'oriole', 'kookaburra',
    'quail', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'black', 'white',
    'gray', 'beige', 'turquoise', 'gold', 'silver', 'maroon', 'indigo', 'olive', 'teal', 'navy',
    'magenta', 'violet', 'cyan', 'lime', 'coral', 'peach', 'salmon', 'lavender', 'plum', 'khaki',
    'ivory', 'azure', 'chartreuse', 'periwinkle', 'sienna', 'crimson', 'fuchsia', 'rose', 'mint',
    'ruby', 'emerald', 'amber', 'jade', 'sapphire', 'topaz', 'bronze', 'copper', 'mauve', 'scarlet',
    'mustard']
    
        # button settings
        self.button_width = 50
        self.button_height = 50
        self.button_margin = 10
        self.text_color = (0,0,0)
        self.button_color = (255,255,255)
        self.hover_color = (220,220,220)
        self.font = pygame.font.SysFont(None, 35)

        # word settings
        self.word_width = 800
        self.word_height = 400
        self.word_font = pygame.font.SysFont(None, 50)
        