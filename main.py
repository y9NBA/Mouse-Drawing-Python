import pygame as pg

WIDTH, HEIGHT = 1200, 800
SIZE = 5
FPS = pg.time.Clock()

pg.init()
dis = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Draw")


def render(display: pg.Surface, color: tuple[int, int, int], cells: list, size: int) -> None:
    for cell in cells:
        if len(cell) == 2:
            pg.draw.rect(display, color, [cell[0], cell[1], size, size])
        if len(cell) == 4:
            pg.draw.rect(display, color, [cell[0], cell[1], size, size])
            pg.draw.rect(display, color, [cell[2], cell[3], size, size])


def loop() -> None:
    close_window = False
    cells = []

    x0 = -1
    y0 = -1

    while not close_window:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                close_window = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_r:
                    loop()
                if event.key == pg.K_q:
                    close_window = True

            # Рисование одной линией
            if pg.mouse.get_pressed()[0]:
                x = event.pos[0] // SIZE * SIZE
                y = event.pos[1] // SIZE * SIZE
                if cells.count([x, y]) == 0:
                    cells.append([x, y])

            # Рисование симметричной линией относительно оси Oy
            if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[2]:
                x0 = event.pos[0] // SIZE * SIZE
            if pg.mouse.get_pressed()[2]:
                x = event.pos[0] // SIZE * SIZE
                y = event.pos[1] // SIZE * SIZE
                x1 = x + abs(x - x0) * 2 if x <= x0 else x - abs(x - x0) * 2
                y1 = event.pos[1] // SIZE * SIZE
                if cells.count([x, y, x1, y1]) == 0:
                    cells.append([x, y, x1, y1])
            if event.type == pg.MOUSEBUTTONUP and not pg.mouse.get_pressed()[2]:
                x0 = -1

            # Рисование симметричной линией относительно оси Ox
            if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed()[1]:
                y0 = event.pos[1] // SIZE * SIZE
            if pg.mouse.get_pressed()[1]:
                x = event.pos[0] // SIZE * SIZE
                y = event.pos[1] // SIZE * SIZE
                x1 = event.pos[0] // SIZE * SIZE
                y1 = y + abs(y - y0) * 2 if y <= y0 else y - abs(y - y0) * 2
                if cells.count([x, y, x1, y1]) == 0:
                    cells.append([x, y, x1, y1])
            if event.type == pg.MOUSEBUTTONUP and not pg.mouse.get_pressed()[1]:
                y0 = -1

        dis.fill((255, 255, 255))

        render(dis, (90, 255, 60), cells, SIZE)

        pg.display.update()

        FPS.tick(1000)

    pg.quit()
    quit()


if __name__ == "__main__":
    loop()
