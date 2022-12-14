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
blue = (173, 216, 230)
green = (0, 100, 0)

colors = (
    (255, 0, 0),
    (0, 255, 0),
    (173, 216, 230),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
)

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
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

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
                    tetris.state = GameState.PAUSE

                if event.key == pygame.K_r:
                    tetris.state = GameState.PLAYING

    def start(self):
        pygame.init()
        pygame.font.init()

        self.tetris.play()

        while True:
            pygame.time.delay(2)

            self.update()
            self.render()

    def render_held_shape_grid(self):
        sx, sy, w = 750, 250, 120

        pygame.draw.line(self.screen, black, (sx, sy), (sx, sy-w))
        pygame.draw.line(self.screen, black, (sx, sy), (sx-w, sy))
        pygame.draw.line(self.screen, black, (sx-w, sy-w), (sx-w, sy))
        pygame.draw.line(self.screen, black, (sx-w, sy-w), (sx, sy-w))

        if self.tetris.held_shape is not None:
            held_shape_grid = self.tetris.held_shape.grid

            for row in range(len(held_shape_grid)):
                for col in range(len(held_shape_grid[row])):
                    if held_shape_grid[row][col] != None:
                        pygame.draw.rect(self.screen, held_shape_grid[row][col].color, (
                            sx - (col+1) * unit_size, sy - (row+1) * unit_size, unit_size, unit_size))

                        # draw borders around the shape
                        pygame.draw.rect(self.screen, black, (
                            sx - (col+1) * unit_size, sy - (row+1) * unit_size, unit_size, unit_size), 2)

    def render(self):
        screen.fill(black)

        if tetris.state == GameState.PLAYING:

            score_text = pygame.font.SysFont('arial', 18)

            score_text_display = score_text.render(
                'Score: {0}'.format(tetris.score), 1, blue)

            level_text_display = score_text.render(
                'Level : {0}'.format(tetris.level), 1, blue)

            pause_game_display = score_text.render(
                "Press the 'P' to Pause ", 1, blue)

            screen.blit(pause_game_display, (600, 100))
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

                        # draw borders around the shape
                        pygame.draw.rect(
                            screen, black, (start_x + col * unit_size, start_y + row * unit_size, unit_size, unit_size), 2)

            pygame.draw.line(screen, grey, (start_x + grid_width, start_y),
                             (start_x + grid_width, start_y + grid_height))
            pygame.draw.line(screen, grey, (start_x, start_y + grid_height),
                             (start_x + grid_width, start_y + grid_height))

            self.render_held_shape_grid()

        elif tetris.state == GameState.PAUSE:

            text = pygame.font.SysFont('arial', 50)

            resume_display = text.render(
                "Press 'R' to resume the game", 1, (white))
            quit_display = text.render("Press the 'Escape' to Quit", 1, white)

            screen.blit(resume_display, (130, 220))
            screen.blit(quit_display, (150, 420))

        elif tetris.state == GameState.GAMEOVER:
            text = pygame.font.SysFont('arial', 50)

            score_text = pygame.font.SysFont('arial', 30)

            score_text_display = score_text.render(
                'Score: {0}'.format(tetris.score), 1, (white))

            gameover_display = text.render(
                "Game Over", 1, (white))
                
            screen.blit(gameover_display, (330, 220))
            screen.blit(score_text_display, (330, 3000))

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
