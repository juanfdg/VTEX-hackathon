from app.models.Box import Box


class Customization:
    def __init__(self, font, font_size, font_color, x, y, l, h):
        self.font = font
        self.font_size = font_size
        self.font_color = font_color
        self.box = Box(x, y, l, h)

