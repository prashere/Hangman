import pygame.font

class Settings:
    """ COntains all the settings of the game"""
    def __init__(self):
        # Screen settings
        self.height = 700
        self.width = 1200
        self.bg_color = (177,79,179)

        # words to be used for the game
        self.word_list = [
        "abruptly", "absurd", "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure",
        "bagpipes", "bandwagon", "banjo", "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm",
        "boxcar", "boxful", "buckaroo", "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords",
        "cobweb", "cockiness", "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying",
        "duplex", "dwarves", "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable",
        "flapjack", "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby",
        "galaxy", "galvanize", "gazebo", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip", "grogginess",
        "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot", "jaundice",
        "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey", "jogging",
        "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki",
        "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury",
        "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub", "nowadays",
        "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm", "pixel",
        "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue", "quips",
        "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw", "schnapps", "scratch", "shiv",
        "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths", "subway", "swivel", "syndrome",
        "thriftless", "thumbscrew", "topaz", "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown"]
    
        # button settings
        self.button_width = 50
        self.button_height = 50
        self.text_color = (0,0,0)
        self.button_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 35)