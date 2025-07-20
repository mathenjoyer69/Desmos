import pygame

class Entry:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.entry_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.base_color = (130, 130, 130)
        self.active_color = (150, 150, 150)
        self.text_color = 'black'
        self.font = pygame.font.Font(None, 32)
        self.text = ''
        self.active = False

    def draw_entry(self, surface):
        color = self.active_color if self.active else self.base_color
        pygame.draw.rect(surface, color, self.entry_rect)
        txt_surface = self.font.render(self.text, True, self.text_color)
        surface.blit(txt_surface, (self.entry_rect.x + 10, self.entry_rect.y + 10))
        pygame.draw.rect(surface, 'black', self.entry_rect, 2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.entry_rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def get_text(self):
        return self.text
