import pygame

from tetris import Tetris
from tetris import GameState
from grid import TetrisVirtualGrid
from grid import TetrisGrid
from tetris import RandomShapeGenerator
from tetris import Gravity


black = (0, 0, 0)
red = (255, 0, 0)
grey = (128, 128, 128)
white = (255, 255, 255)
blue = (0, 0, 255)
green = (0, 100, 0)

colors = (red, blue, black, green)

screen_width = 800
screen_height = 700

unit_size = 30
grid_width = 300
grid_height = 600

start_x = (screen_width - grid_width) / 2
start_y = (screen_height - grid_height) / 2


class Game:
    def __init__(self, screen, tetris):
        self.screen = screen
        self.tetris = tetris

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
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
        pygame.font.init()

        self.tetris.play()

        while self.tetris.state != GameState.GAMEOVER:
            pygame.time.delay(2)

            self.update()
            self.render()

    def render(self):
        screen.fill(white)

        score_text = pygame.font.SysFont('arial', 18)

        score_text_display = score_text.render(
            'Score: {0}'.format(tetris.score), 1, blue)

        level_text_display = score_text.render(
            'Level : {0}'.format(tetris.level), 1, blue)

        screen.blit(score_text_display, (100, 100))
        screen.blit(level_text_display, (100, 140))
        grid = self.tetris.grid.get_map()

        for row in range(len(grid)):
            pygame.draw.line(screen, grey, (start_x, start_y + row * unit_size),
                             (start_x + grid_width, start_y + row * unit_size))

            for col in range(len(grid[row])):
                pygame.draw.line(screen, grey, (start_x + col * unit_size, start_y),
                                 (start_x + col * unit_size, start_y + grid_height))

                if grid[row][col] != None:
                    pygame.draw.rect(
                        screen, grid[row][col].color, (start_x + col * unit_size, start_y + row * unit_size, unit_size, unit_size))

        pygame.draw.line(screen, grey, (start_x + grid_width, start_y),
                         (start_x + grid_width, start_y + grid_height))
        pygame.draw.line(screen, grey, (start_x, start_y + grid_height),
                         (start_x + grid_width, start_y + grid_height))

        pygame.display.update()


if __name__ == "__main__":
    screen = pygame.display.set_mode((screen_width, screen_height))

    grid = TetrisGrid(20, 10)
    virtual_grid = TetrisVirtualGrid(20, 10, grid.sync)
    shape_generator = RandomShapeGenerator(0, 4, colors)
    gravity = Gravity()

    tetris = Tetris(grid, virtual_grid, shape_generator, gravity)

    game = Game(screen, tetris)
    game.start()
