import pygame

import agent as ag
from steeringbehavioursgame import SteeringGame


def main():

    game = SteeringGame("SteeringGame")
    for _ in range(1):
        game.addtobatch(ag.Agent((pygame.display.get_surface(
        ).get_width(), pygame.display.get_surface().get_height()), 75, 50))
    game.run()


if __name__ == "__main__":
    main()
