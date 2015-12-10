import os, pygame

class Drawer:
    def __init__(self, main):
        self.main = main

    def init(self):
        self.center = (int(round(self.main.width/2.0)), int(round(self.main.height/2.0)))
        self.radius = int(round(min(self.main.width, self.main.height)/2.0)*0.8)
        self.rect = (self.center[0]-self.radius, self.center[1]-self.radius, 2*self.radius, 2*self.radius)
        self.graphic = self.load_image("graphic.png")
        self.font = pygame.font.Font(None, 12)

    def draw(self, transform):
        self.clear()

        # scale graphic to circle size
        graphic = pygame.transform.smoothscale(self.graphic, (2*self.radius, 2*self.radius))

        if transform['flip_horizontally'] or transform['flip_vertically']:
            graphic = pygame.transform.flip(graphic, transform['flip_horizontally'], transform['flip_vertically'])

        if transform['rotate']:
            graphic = pygame.transform.rotate(graphic, transform['rotate'])

        self.main.screen.blit(graphic, self.rect)

    def clear(self):
        self.main.screen.fill((48, 48, 64))
        pygame.draw.circle(self.main.screen, (128, 128, 152), self.center, self.radius, 0)

    def render_text(self, text, bottom):
        text = self.font.render(text, True, (255, 255, 255))

        if bottom:
            self.main.screen.blit(text, (10, self.main.height-10-text.get_height()))
        else:
            self.main.screen.blit(text, (10, 10))

    def load_image(self, filename):
        image_path = os.path.join(os.path.dirname(__file__), 'images')
        path = os.path.join(image_path, filename)
        return pygame.image.load(path)
