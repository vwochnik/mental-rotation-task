import pygame, time
from drawer import Drawer
from logic import Logic

"""Event ID for spawning graphic"""
SPAWN = pygame.USEREVENT + 1

class Main:
    def __init__(self, width, height, caption):
        self.width = width
        self.height = height
        self.caption = caption
        self.drawer = Drawer(self)
        self.logic = Logic()

    def init(self):
        pygame.init()
        pygame.display.set_caption(self.caption)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.drawer.init()

        # start game with clear surface
        self.drawer.clear()
        self.draw_info()
        pygame.display.flip()

        # spwn number in one second after game start
        pygame.time.set_timer(SPAWN, 1000)

    def quit(self):
        pygame.quit()

    def loop(self):
        running = True
        while running:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == SPAWN:
                self.spawn()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    self.submit(event.key)

    def spawn(self):
        pygame.time.set_timer(SPAWN, 0)
        self.logic.start_test()

        transform = self.logic.current_transform
        self.drawer.draw(transform)
        self.draw_info()
        pygame.display.flip()

    def submit(self, key):
        if key in (pygame.K_SPACE, pygame.K_r, pygame.K_f):
            # neither rotated nor flipped
            if key == pygame.K_SPACE:
                self.logic.submit_result(False, False)
            elif key == pygame.K_r:
                self.logic.submit_result(True, False)
            else: # key == pygame.K_f
                self.logic.submit_result(False, True)

            # make number disappear
            self.drawer.clear()
            self.draw_info()
            pygame.display.flip()

            # spawn another test in one second
            pygame.time.set_timer(SPAWN, 1000)

    def draw_info(self):
        text = "Tests Completed: %d\nTests Failed: %d\nAverage Time: %f sec" % (self.logic.tests_completed, self.logic.tests_failed, (float(self.logic.average_time)/1000.0))
        self.drawer.render_text(text, False)
        self.drawer.render_text("Press R if rotated\nPress F if flipped\nPress SPACE if neither apply", True)
