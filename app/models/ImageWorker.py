import os
import secrets
from PIL import Image, ImageDraw, ImageFont
from app.models import Product
from flask import url_for


class ImageWorker:
    def customize(product, text):
        # Create image with input image
        image = Image.open(f'app/static/img/{product.thumb}')

        # Initialise the drawing context with the image
        # object as background
        draw = ImageDraw.Draw(image)

        # Create font object with the font file and specify
        # desired size
        font = ImageFont.truetype(f'app/static/fonts/{product.font_path}', product.font_size)

        # starting position of message
        (x, y) = (product.box_x, product.box_y)

        w, h = draw.textsize(text)

        # Draw message on the background
        font_color = (product.font_color_r, product.font_color_g, product.font_color_b)
        draw.text(((x-w)/2, (y-h)/2), text, fill=font_color, font=font)

        # Return the edited image
        filename, file_extension = os.path.splitext(product.thumb)

        os.makedirs('app/temporary', exist_ok=True)
        custom_file = f'{filename}_custom_{secrets.token_urlsafe(16)}{file_extension}'
        image.save(f'app/temporary/{custom_file}')

        return custom_file


if __name__ == '__main__':
    file = '../static/img/white_shirt.jpeg'
    font = '../static/fonts/square.ttf'

    product = Product(0, file, 'dummy', 0.0, 'a_dummy_product')
    font = Font(font, 20, (0, 200, 100))
    product.add_customization('Name', font, 100, 50, 20, 20)

    print(customize(product, ['Dummy']))
