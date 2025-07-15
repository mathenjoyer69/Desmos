from math import *
from classes import *

pygame.init()

class MainScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 800))

        self.running = True
        self.clock = pygame.time.Clock()
        self.entry = Entry(20, 20, 200, 40)

        self.offset = [0, 0]
        self.dragging = False
        self.last_mouse_pos = (0, 0)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        self.dragging = True
                        self.last_mouse_pos = pygame.mouse.get_pos()

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 3:
                        self.dragging = False

                elif event.type == pygame.MOUSEMOTION:
                    if self.dragging:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        dx = mouse_x - self.last_mouse_pos[0]
                        dy = mouse_y - self.last_mouse_pos[1]
                        self.offset[0] += dx
                        self.offset[1] += dy
                        self.last_mouse_pos = (mouse_x, mouse_y)

                self.entry.handle_event(event)

            self.screen.fill((255, 255, 255))
            self.draw()
            try:
                self.draw_function(self.entry.get_text())
            except (SyntaxError, NameError, TypeError, AttributeError, IndexError):
                print("invalid")
            self.entry.draw_entry(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def draw(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        ox, oy = self.offset
        #horizonal lines
        for i in range(0, screen_height, 100):
            startpos = (0, i + oy % 100)
            endpos = (screen_width, i + oy % 100)
            pygame.draw.line(self.screen, "gray", startpos, endpos)
        #vertical lines
        for i in range(0, screen_width, 100):
            startpos = (i + ox % 100, 0)
            endpos = (i + ox % 100, screen_width)
            pygame.draw.line(self.screen, "gray", startpos, endpos)
        #vertical line
        start_pos = (0, screen_height // 2 + oy)
        end_pos = (screen_width, screen_height // 2 + oy)
        pygame.draw.line(self.screen,"black", start_pos, end_pos)
        #horizontal line
        startpos = (screen_width // 2 + ox, 0)
        endpos = (screen_width // 2 + ox, screen_height)
        pygame.draw.line(self.screen, "black", startpos, endpos)

    def draw_function(self, func_input):
        center = (self.screen.get_width() // 2 + self.offset[0], self.screen.get_height() // 2 + self.offset[1])
        scale_factor = 10
        points = []

        parts = func_input.split(":")
        function = parts[0]
        if len(parts) > 1:
            try:
                scale_factor = float(parts[1])
            except ValueError:
                pass

        for i in range(-1000, 1000, 1):
            x = i / 10
            temp_function = function.replace('x', f'({x})')
            y = eval(temp_function)
            screen_x = center[0] + x * scale_factor
            screen_y = center[1] - y * scale_factor
            points.append((screen_x, screen_y))

        for point in points:
            pygame.draw.circle(self.screen, "red", point, 1)
        #for i in range(len(points)-1):
        #    pygame.draw.line(self.screen, "black", points[i], points[i + 1])


if __name__ == '__main__':
    main = MainScreen()
    main.run()