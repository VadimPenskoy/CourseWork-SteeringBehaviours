
import math

import pygame
import random
import agent as boids
from game import GameTemplate


class SteeringGame(GameTemplate):
    def __init__(self, name):
        super(SteeringGame, self).__init__()
        self._name = name
        self.flee = False
        self.wander = True
        pygame.font.init()
        self.font = pygame.font.SysFont('mono', 20)
        self._gameobjects = []
        self.singlebehaviors = False
        self.targetagent = boids.Agent((pygame.display.get_surface(
        ).get_width(), pygame.display.get_surface().get_height()), 75, 50)

    def addtobatch(self, gameobject):
        self._gameobjects.append(gameobject)
        if type(gameobject) == boids.Agent:
            gameobject.settarget(self.targetagent)

    def update(self):

        self.clock.tick(60)
        self.deltatime = float(self.clock.get_time()) / float(1000)
        if not super(SteeringGame, self).update():
            return False
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_F10:
                    self.singlebehaviors = True if not self.singlebehaviors else False
                if event.key == pygame.K_f:
                    self.flee = True
                    self.wander = False
                if event.key == pygame.K_s:
                    self.flee = False
                    self.wander = False
                if event.key == pygame.K_w:
                    self.wander = True
                    self.flee = False
                if event.key == pygame.K_a:
                    self.flee = False
                    self.wander = False
                if event.key == pygame.K_SPACE:
                    self.addtobatch(boids.Agent((pygame.display.get_surface(
                    ).get_width(),
                        pygame.display.get_surface().get_height()), 75, 50))
                if event.key == pygame.K_F1:
                    self.addtobatch(boids.Agent((pygame.display.get_surface(
                    ).get_width(),
                        pygame.display.get_surface().get_height()), 150, 250))
                if event.key == pygame.K_F2:
                    self.addtobatch(boids.Agent((pygame.display.get_surface(
                    ).get_width(),
                        pygame.display.get_surface().get_height()), 100, 10))
                if event.key == pygame.K_DELETE:
                    if len(self._gameobjects) > 0:
                        self._gameobjects.remove(
                            self._gameobjects[
                                random.randrange(0, len(self._gameobjects))])
            if event.type == pygame.QUIT:
                return False
        self.targetagent.position = pygame.mouse.get_pos()
        for gameobjs in self._gameobjects:
            if type(gameobjs) == boids.Agent:
                if self.flee:
                    gameobjs.scared = True
                else:
                    gameobjs.scared = False
                if self.wander:
                    gameobjs.bored = True
                else:
                    gameobjs.bored = False
                if not self.wander:
                    gameobjs.target = self.targetagent
            if self.singlebehaviors:
                gameobjs.update(self.deltatime)
            else:
                gameobjs.updatealone(self.deltatime)
        return True

    def draw(self):
        for gameobj in self._gameobjects:
            gameobj.draw(self.surface)
            pygame.draw.line(self.surface, (255, 255, 255), gameobj.position, (gameobj.position[0] + gameobj.velocity[0], gameobj.position[1] + gameobj.velocity[1]), 2)
            pygame.draw.line(self.surface, (255, 0, 0), gameobj.position, (gameobj.position[0] + gameobj.acceleration[0], gameobj.position[1] + gameobj.acceleration[1]), 2)
        test = "\'spacebar to spawn an agent\'    \'s to Seek\'"
        test = test + "     \'w to Wander\'    \'f to Flee\' \'a to Arrive\'"
        text = "objects in game: {}".format(len(self._gameobjects))
        fpstext = self.font.render(text, True, (255, 255, 255))
        testthing = self.font.render(test, True, (255, 255, 255))
        self.surface.blit(testthing, (0, 0))
        self.surface.blit(fpstext, (0, 20))

        super(SteeringGame, self).draw()

    def run(self):
        if super(SteeringGame, self).startup():
            while self.update():
                self.draw()
        super(SteeringGame, self).shutdown()
