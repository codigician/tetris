import pygame

pygame.init()

pygame.font.init()

width = 800
height = 700

screen = pygame.display.set_mode((width, height))

while True:
    screen.fill((255, 255, 255))

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse[0])
            if 200 <= mouse[0] <= 600 and 200 <= mouse[1] <= 300:
                print('Naber bebek')

    text = pygame.font.SysFont('arial', 50)

    text_display = text.render('Resume the game', 1, (0, 0, 0))

    screen.blit(text_display, (230, 220))

    pygame.draw.rect(screen, (0, 0, 0), (200, 200, 400, 100), 1)

    pygame.display.flip()
