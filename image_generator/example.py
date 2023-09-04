from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(text: str, option: str = "1.jpg"):
    """
    :param text: text to add to image
    :param option: option of image
    :return:
    """
    image_path = f"image_generator/images/options/{option}"
    # Открываем изображение
    image = Image.open(image_path)

    # Создаем объект ImageDraw для рисования текста
    draw = ImageDraw.Draw(image)

    # Задаем шрифт и размер текста
    font_name = "SuperWebcomicBros_Rusbyyakustick_-Regular_0.ttf"
    # font = ImageFont.truetype("image_generator/fonts/cinzel_regular.ttf", 50)  # Укажите путь к файлу шрифта и размер шрифта
    font = ImageFont.truetype(f"image_generator/fonts/{font_name}", 50)  # Укажите путь к файлу шрифта и размер шрифта

    # Определяем максимальную ширину текста (90% ширины изображения)
    max_text_width = int(image.width * 0.9)

    # Разбиваем текст на строки, учитывая перенос
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

    # Определяем координаты для выравнивания текста по центру
    text_height = 0
    for line in lines:
        line_width, line_height = draw.textsize(line, font)
        text_height += line_height

    image_width, image_height = image.size
    x = (image_width - max_text_width) // 2
    y = (image_height - text_height) // 2

    # Рисуем текст на изображении
    for line in lines:
        line_width, line_height = draw.textsize(line, font)
        x = (image_width - line_width) // 2
        draw.text((x, y), line, fill="white", font=font)
        y += line_height

    # Сохраняем измененное изображение
    result_path = f"image_generator/images/results/{option}"
    image.save(result_path)  # Укажите путь для сохранения
    return result_path


if __name__ == "__main__":
    image_path = "1.jpg"  # Укажите путь к изображению
    text = "Ваш очень длинный текст здесь, который автоматически переносится на новую строку, если не помещается на одной строке."  # Замените на нужный текст
    add_text_to_image(text, image_path)
