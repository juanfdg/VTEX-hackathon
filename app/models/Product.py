class Box:
    def __init__(self, x, y, length, height):
        self.x = x
        self.y = y
        self.length = length
        self.height = height


class Font:
    def __init__(self, font, font_size, font_color):
        self.font = font
        self.size = font_size
        self.color = font_color


class Customization:
    def __init__(self, name, font, x, y, l, h):
        self.name = name
        self.font = font
        self.box = Box(x, y, l, h)


class Product:
    def __init__(self, id, thumb, name, price, description):
        self.id = id
        self.thumb = thumb
        self.name = name
        self.price = price
        self.description = description
        self.customizations = []

    def add_customization(self, name, font, x, y, l, h):
        self.customizations.append(Customization(name, font, x, y, l, h))

