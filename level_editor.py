class LevelEditor:

    def __init__(self, file=None):
        self.is_active = False
        

    def activate(self): 
        self.is_active = True
        while self.is_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    pass

class Level:

    def __init__(self, file):
        pass

