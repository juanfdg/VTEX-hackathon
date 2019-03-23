import os
from PIL import Image, ImageDraw, ImageFont
from app.models import Product
from flask import url_for


class ImageWorker:
    def customize(product, texts):
        # Create image with input image
        image = Image.open(f'app/static/img/{product.thumb}')

        # Initialise the drawing context with the image
        # object as background
        draw = ImageDraw.Draw(image)

        for idx, custom in enumerate(product.customizations):
            # Create font object with the font file and specify
            # desired size
            font = ImageFont.truetype(custom.font.font, custom.font.size)

            # starting position of message
            (x, y) = (custom.box.x, custom.box.y)

            # Draw message on the background
            draw.text((x, y), texts[idx], fill=custom.font.color, font=font)

        # Return the edited image
        filename, file_extension = os.path.splitext(product.thumb)

        custom_file = '../temporary/' + filename + "_custom" + file_extension
        image.save(custom_file)

        return custom_file


if __name__ == '__main__':
    file = '../static/img/white_shirt.jpeg'
    font = '../static/fonts/square.ttf'

    product = Product(0, file, 'dummy', 0.0, 'a_dummy_product')
    font = Font(font, 20, (0, 200, 100))
    product.add_customization('Name', font, 80, 50, 20, 20)

    print(customize(product, ['Dummy']))
