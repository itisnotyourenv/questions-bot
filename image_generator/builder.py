from PIL import Image, ImageDraw, ImageFont


def generate_image(text: str, option: str = "1.jpg") -> str:
    """
    Add text to an image and save the result.

    :param text: Text to add to the image.
    :param option: Option of the image.
    :return: Path to the saved result image.
    """
    # Construct absolute paths for image and font files
    # todo - replace with Path lib
    root_path = "image_generator/"
    image_path = f"{root_path}/images/options/{option}"
    font_path = f"{root_path}/fonts/DejaVuSans-Bold.ttf"

    # Open the image
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Image file not found at {image_path}")

    # Create an ImageDraw object for drawing text
    draw = ImageDraw.Draw(image)

    # Load the font and set the font size
    try:
        font = ImageFont.truetype(font_path, 60)
    except FileNotFoundError:
        raise FileNotFoundError(f"Font file not found at {font_path}")

    # Determine the maximum text width (90% of image width)
    max_text_width = int(image.width * 0.9)

    # Split the text into lines, considering line breaks
    lines = []
    line = ""
    for word in text.split():
        test_line = line + word + " "
        test_width, _ = draw.textsize(test_line, font)
        if test_width <= max_text_width:
            line = test_line
        else:
            lines.append(line.rstrip())
            line = word + " "
    lines.append(line)

    # Calculate coordinates for center alignment
    text_height = 0
    for line in lines:
        line_width, line_height = draw.textsize(line, font)
        text_height += line_height

    image_width, image_height = image.size
    x = (image_width - max_text_width) // 2
    y = (image_height - text_height) // 2

    # Draw text on the image
    for line in lines:
        line_width, line_height = draw.textsize(line, font)
        x = (image_width - line_width) // 2
        draw.text((x, y), line, fill="black", font=font)
        y += line_height

    # Save the modified image
    result_path = f"image_generator/images/results/{option}"
    image.save(result_path)  # Specify the path to save the image
    return result_path


if __name__ == "__main__":
    your_image_name = "1.jpg"  # Укажите путь к изображению
    your_text = "Ваш очень длинный текст ddd, переносится на новую строку, если не помещается на одной строке."  # Замените на нужный текст
    generate_image(your_text, your_image_name)
