import pygame

from tetris import Tetris
from shape import create_shape
from shape import Unit
from grid import TetrisVirtualGrid
from grid import TetrisGrid
from tetris import RandomShapeGenerator
from tetris import Gravity

class Game:
    def __init__(self, screen, tetris):
        self.screen = screen
        self.tetris = tetris
        self.grid = tetris.grid

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tetris.move_left()

            if event.key == pygame.K_RIGHT:
                tetris.move_right()

            if event.key == pygame.K_UP:
                tetris.rotate()

            if event.key == pygame.K_DOWN:
                tetris.move_down()

            if event.key == pygame.K_SPACE:
                tetris.move_ground()

            if event.key == pygame.K_c:
                tetris.hold()

    def start(self):
        pygame.init()
        self.tetris.play()

        while self.tetris.state != GameState.GAME_OVER:
            pygame.time.delay(50)

            self.update()
            self.render()

    def render(self):
        screen.fill(WHITE)

        for row in range(len(self.grid)):
            pygame.draw.line(screen, GREY, (START_X, START_Y + row * UNIT_SIZE),
                             (START_X + PLAY_WIDTH, START_Y + row * UNIT_SIZE))

            for col in range(len(self.grid[row])):

                pygame.draw.line(screen, GREY, (START_X + col * UNIT_SIZE, START_Y),
                                 (START_X + col * UNIT_SIZE, START_Y + PLAY_HEIGHT))

                if self.grid[row][col] != None:

                    pygame.draw.rect(
                        screen, self.grid[row][col].color, (START_X + col * UNIT_SIZE, START_Y + row * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE))

        pygame.draw.line(screen, GREY, (START_X + PLAY_WIDTH, START_Y),
                         (START_X + PLAY_WIDTH, START_Y + PLAY_HEIGHT))
        pygame.draw.line(screen, GREY, (START_X, START_Y + PLAY_HEIGHT),
                         (START_X + PLAY_WIDTH, START_Y + PLAY_HEIGHT))

        pygame.display.update()


BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

UNIT_SIZE = 30
PLAY_WIDTH = 300
PLAY_HEIGHT = 600

START_X = (SCREEN_WIDTH - PLAY_WIDTH) / 2
START_Y = (SCREEN_HEIGHT - PLAY_HEIGHT) / 2



if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    grid = TetrisGrid(20, 10)
    virtual_grid = TetrisVirtualGrid(20, 10, grid.sync)
    shape_generator = RandomShapeGenerator(0, 4)

    tetris = Tetris(grid, virtual_grid, shape_generator)

    game = Game(screen, tetris)
    game.start()
