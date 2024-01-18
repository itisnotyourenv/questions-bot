import pytest

from image_generator.builder import calculate_font_size_by_text


@pytest.mark.parametrize(
    "text_size, expected_font_size",
    [
        (10, 60),
        (100, 50),
        (200, 40),
        (300, 30),
        (400, 20),
        (500, 10),
    ],
)
def test_calculate_font_size_by_text(text_size: int, expected_font_size: int):
    text = "a" * text_size
    assert calculate_font_size_by_text(text) == expected_font_size
