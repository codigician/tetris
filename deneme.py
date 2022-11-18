import pygame

pygame.init()
window = pygame.display.set_mode((200, 200))
clock = pygame.time.Clock()

POLYGONS = [
    ((255, 0, 0), [(100, 50), (50, 150), [150, 150]], True),
    ((0, 0, 255), [(100, 150), (50, 50), [150, 50]], True)
]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window_center = window.get_rect().center

    window.fill(0)
    pygame.draw.polygon(window, (255, 0, 0), [
                        (100, 100), (100, 120), (130, 100)], True)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit()
