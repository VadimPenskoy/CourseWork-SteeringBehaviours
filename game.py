
import pygame


class GameTemplate(object):

    def __init__(self):
        pygame.display.init()
        self.surface = pygame.display.set_mode((1366, 768))
        self.clock = pygame.time.Clock()
        self.background = pygame.Surface(self.surface.get_size()).convert()
        self.background.fill((0, 0, 0))
        self.deltatime = 0.0

    def startup(self):
        return True

    def update(self):
        return True

    def draw(self):
        pygame.display.flip()
        self.surface.blit(self.background, (0, 0))
        return True

    def shutdown(self):
        return True
