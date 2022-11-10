from grid import OccupiedPositionException
import pygame
from tetris import Tetris
from tetris import GameRenderer
from tetris import GameState

pygame.init()

WİDTH = 600
HEİGHT = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WİDTH, HEİGHT))
tetris = Tetris()
render = GameRenderer(tetris.grid)

run = True

while run:
    screen.fill(WHITE)

    tetris.play()
    render.start()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            render.playing = False
            tetris.state = GameState.PAUSE
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                tetris.move_left()

            if event.type == pygame.K_RIGHT:
                tetris.move_right()

            if event.type == pygame.K_DOWN:
                tetris.move_down()

            if event.type == pygame.K_SPACE:
                tetris.move_ground()

            if event.type == pygame.K_UP:
                tetris.rotate()

            if event.type == pygame.K_c:
                tetris.hold()

    pygame.display.update()
