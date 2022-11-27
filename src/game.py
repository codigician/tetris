import pygame

from tetris import Tetris
from tetris import GameState
from grid import HeldGrid
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
        mouse = pygame.mouse.get_pos()

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

                if event.key == pygame.K_p:
                    tetris.pause()

                if event.key == pygame.K_r:
                    tetris.resume()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 200 <= mouse[0] <= 600 and 200 <= mouse[1] <= 300:
                    tetris.state = GameState.PLAYING

    def start(self):
        pygame.init()
        pygame.font.init()

        self.tetris.play()

        while self.tetris.state != GameState.GAMEOVER:
            pygame.time.delay(2)

            if tetris.state == GameState.PLAYING:
                self.update()
                self.render()

            if tetris.state == GameState.PAUSE:
                self.update()
                self.render()

    def render(self):
        screen.fill(white)

        if tetris.state == GameState.PLAYING:

            score_text = pygame.font.SysFont('arial', 18)

            score_text_display = score_text.render(
                'Score: {0}'.format(tetris.score), 1, blue)

            level_text_display = score_text.render(
                'Level : {0}'.format(tetris.level), 1, blue)

            screen.blit(score_text_display, (100, 100))
            screen.blit(level_text_display, (100, 140))
            grid = self.tetris.grid.get_map()
            held_grid = self.tetris.held_grid.get_held_map()

            # Draw held grid

            for row in range(len(held_grid)):
                pygame.draw.line(screen, grey, (50, 200 + row *
                                                unit_size), (230, 200 + row * unit_size))
                for col in range(len(held_grid[row])):
                    pygame.draw.line(
                        screen, grey, (50 + col * unit_size, 200), (50 + col * unit_size, 380))

                    if held_grid[row][col] != None:
                        pygame.draw.rect(screen, held_grid[row][col].color, (
                            50 + col * unit_size, 200 + row * unit_size, unit_size, unit_size))

            pygame.draw.line(screen, grey, (230, 200), (230, 380))
            pygame.draw.line(screen, grey, (50, 380), (230, 380))
            #  Draw tetris grid

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

        elif tetris.state == GameState.PAUSE:

            text = pygame.font.SysFont('arial', 50)

            resume_display = text.render('Resume the game', 1, (0, 0, 0))
            quit_display = text.render('Quit', 1, (0, 0, 0))

            screen.blit(resume_display, (230, 220))
            screen.blit(quit_display, (350, 420))

            pygame.draw.rect(screen, (0, 0, 0), (200, 400, 400, 100), 1)
            pygame.draw.rect(screen, (0, 0, 0), (200, 200, 400, 100), 1)

        pygame.display.update()


if __name__ == "__main__":
    screen = pygame.display.set_mode((screen_width, screen_height))

    grid = TetrisGrid(20, 10)
    held_grid = HeldGrid()
    virtual_grid = TetrisVirtualGrid(20, 10, grid.sync)
    shape_generator = RandomShapeGenerator(0, 4, colors)
    gravity = Gravity()

    tetris = Tetris(grid, virtual_grid, shape_generator, gravity, held_grid)

    game = Game(screen, tetris)
    game.start()
