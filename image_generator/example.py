from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(image_path, text):
    # Открываем изображение
    image = Image.open(image_path)

    # Создаем объект ImageDraw для рисования текста
    draw = ImageDraw.Draw(image)

    # Задаем шрифт и размер текста
    font = ImageFont.truetype("fonts/cinzel_regular.ttf", 36)  # Укажите путь к файлу шрифта и размер шрифта

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
        draw.text((x, y), line, fill="black", font=font)
        y += line_height

    # Сохраняем измененное изображение
    image.save("output_image.jpg")  # Укажите путь для сохранения


if __name__ == "__main__":
    image_path = "image.jpg"  # Укажите путь к изображению
    text = "Ваш очень длинный текст здесь, который автоматически переносится на новую строку, если не помещается на одной строке."  # Замените на нужный текст
    add_text_to_image(image_path, text)
