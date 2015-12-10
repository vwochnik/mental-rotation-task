import pygame, time
#from VideoCapture import Device

class Main:
    def __init__(self, width, height, caption):
        self.width = width
        self.height = height
        self.caption = caption

    def init(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        self.screen = pygame.display.set_mode((self.width, self.height))

    def quit(self):
        pygame.quit()

    def loop(self):
        running = True
        while running:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False
