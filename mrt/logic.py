import pygame
from random import randint, getrandbits

class Logic:
    def __init__(self):
        self.average_time = 0
        self.tests_completed = 0
        self.tests_failed = 0
        self.current_time = 0
        self.current_tramsform = 0

    def start_test(self):
        self.current_time = pygame.time.get_ticks()

        # either rotation or transformation test
        if bool(getrandbits(1)):
            self.current_transform = {
                "rotate":            0,
                "flip_horizontally": bool(getrandbits(1)),
                "flip_vertically":   bool(getrandbits(1))
            }
        else:
            self.current_transform = {
                "rotate":            90*randint(0, 3),
                "flip_horizontally": False,
                "flip_vertically":   False
            }

    def submit_result(self, rotated, flipped):
        end_time = pygame.time.get_ticks()

        # determine success
        flip_success = (flipped == (self.current_transform['flip_horizontally'] or self.current_transform['flip_vertically']))
        rotate_success = (rotated == (self.current_transform['rotate'] != 0))
        test_successful = (flip_success and rotate_success)

        # calculate duration and reset time
        duration = end_time - self.current_time
        self.current_time = 0

        # add to test counter
        if test_successful:
            self.tests_completed += 1
        else:
            self.tests_failed += 1

        # compute average time
        count = self.tests_completed + self.tests_failed
        self.average_time = int(round(float((count-1) * self.average_time + duration) / float(count)))
