from PIL import Image, ImageDraw, ImageFont


def add_text_to_image(image_path, text):
    # Открываем изображение
    image = Image.open(image_path)

    # Создаем объект ImageDraw для рисования текста
    draw = ImageDraw.Draw(image)

    # Задаем шрифт и размер текста
    font = ImageFont.truetype("fonts/cinzel_regular.ttf", 36)  # Укажите путь к файлу шрифта и размер шрифта

    # Вычисляем размер текста
    text_width, text_height = draw.textsize(text, font)

    # Определяем координаты для выравнивания текста по центру
    image_width, image_height = image.size
    x = (image_width - text_width) // 2
    y = (image_height - text_height) // 2

    # Рисуем текст на изображении
    draw.text((x, y), text, fill="black", font=font)

    # Сохраняем измененное изображение
    image.save("output_image.jpg")  # Укажите путь для сохранения


if __name__ == "__main__":
    image_path = "image.jpg"  # Укажите путь к изображению
    text = "Ваш текст здесь будет очень красивым! Но а здесь не очень! ат авывафыв фыафыва фывава фывафыва ывафыва "  # Укажите свой текст
    add_text_to_image(image_path, text)
