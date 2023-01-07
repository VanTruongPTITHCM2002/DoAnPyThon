from Main2 import textColor,fontsize,font_default,pygame
labels = []


class Label:

    ''' CLASS FOR TEXT LABELS ON THE WIN SCREEN SURFACE '''

    def __init__(self, screen, text, x, y, size=16, color=textColor):
        if size != 20:
            self.font = fontsize(size)
        else:
            self.font = font_default
        self.image = self.font.render(text, 1, color)
        _, _, w, h = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)
        self.screen = screen
        self.text = text
        labels.append(self)

    def addText(self, text, color=textColor):
        self.text += text
        self.image = self.font.render(self.text, 1, color)

    def change_text(self, newtext, color=textColor):
        self.image = self.font.render(newtext, 1, color)

    def change_font(self, font, size, color=textColor):
        self.font = pygame.font.SysFont(font, size)
        self.change_text(self.text, color)

    def draw(self):
        self.screen.blit(self.image, (self.rect))

# Quản lý label


def show_labels():
    for _ in labels:
        _.draw()
