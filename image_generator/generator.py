from PIL import Image, ImageDraw

img = Image.open("beach.jpg")
d1 = ImageDraw.Draw(img)
d1.text((28, 36), "Hello, TutorialsPoint!", fill=(255, 0, 0))
# img.show()
img.save("image_text.jpg")


class ImageGenerator:
    def __init__(self, image_path: str = "beach.jpg"):
        self.image = Image.open("beach.jpg")
        self.draw = ImageDraw.Draw(self.image)

    def start(self, text, font_size: 80, indent: 75):
        pass

    @staticmethod
    def _get_current_indent(line_len: int, indent: int) -> int:
        """
        Возвращает ширину отступа между линиями текста (по вертикали)
        """
        return indent - (line_len - 1) * 50
