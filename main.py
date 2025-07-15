from math import *
from classes import *

pygame.init()

class MainScreen:
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 800))

        self.running = True
        self.clock = pygame.time.Clock()
        self.entry = Entry(20, 20, 200, 40)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

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
        #horizonal lines
        for i in range(self.screen.get_height()//100):
            startpos = (0, i*100)
            endpos = (screen_width, i*100)
            pygame.draw.line(self.screen, "gray", startpos, endpos)
        #vertical lines
        for i in range(screen_width//100):
            startpos = (i*100, 0)
            endpos = (i*100, screen_width)
            pygame.draw.line(self.screen, "gray", startpos, endpos)
        #vertical line
        start_pos = (0, screen_height//2)
        end_pos = (screen_width, screen_height//2)
        pygame.draw.line(self.screen,"black", start_pos, end_pos)
        #horizontal line
        startpos = (screen_width//2, 0)
        endpos = (screen_width//2, screen_height)
        pygame.draw.line(self.screen, "black", startpos, endpos)

    def draw_function(self,func):
        center = (self.screen.get_width() // 2, self.screen.get_height() // 2)
        scale_factor = 15
        points = []
        func = func.split(":")
        if len(func) > 1:
            function, scale_factor = func[0], eval(func[1])
        else:
            function = func[0]
        for i in range(-100, 100, 1):
            x = i
            function = function.replace('x',str(x))
            y = eval(function)
            function = function.replace(str(x),'x')
            screen_x = center[0] + x * scale_factor
            screen_y = center[1] - y * scale_factor

            points.append((screen_x, screen_y))
        for i in range(len(points)-1):
            pygame.draw.line(self.screen, "red", points[i],points[i+1])


if __name__ == '__main__':
    main = MainScreen()
    main.run()
    str1 = "x/2"
    func = str1.split(":")
    if len(func) > 1:
        function, scale_factor = func[0], eval(func[1])
    else:
        function = func[0]
    x = 20
    function = function.replace('x', str(x))
    y = eval(function)
    function = function.replace(str(x), 'x')
    print(function)