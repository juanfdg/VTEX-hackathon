from PIL import Image, ImageDraw, ImageFont
import os


def customize(image_file, customizations):
    # Create image with input image
    image = Image.open(image_file)

    # Initialise the drawing context with the image
    # object as background
    draw = ImageDraw.Draw(image)

    for custom in customizations:
        # Create font object with the font file and specify
        # desired size
        font = ImageFont.truetype(custom.font, custom.font_size)

        # starting position of message
        (x, y) = (custom.box.lenght, custom)

        # Draw message on the background
        draw.text((x, y), custom.text, fill=custom.color, font=font)

    # Return the edited image
    filename, file_extension = os.path.splitext(image_file)

    custom_file = filename + "_custom" + file_extension
    image.save(custom_file)

    return custom_file


if __name__ == '__main__':
    file = ''
    print(customize(file))
