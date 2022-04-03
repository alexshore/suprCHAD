from pathlib import Path
from typing import List
from PIL import Image
from datetime import datetime


TOP_LEFT_X = 1400
TOP_LEFT_Y = 1338


def load_image_from_file(file: str) -> Image:
    image = Image.open(Path(file))
    image.convert("RGBA")
    return image


def create_blank_canvas() -> Image:
    blank_canvas = Image.new("RGBA", (6000, 6000), (0, 0, 0, 0))
    return blank_canvas


def convert_image_to_overlay(image: Image) -> Image:
    new_image = Image.new("RGBA", (image.size[0] * 3, image.size[1] * 3), (0, 0, 0, 0))
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            new_image.putpixel(((i * 3) + 1, (j * 3) + 1), image.getpixel((i, j)))
    return new_image


def place_overlay_on_canvas(overlay: Image, canvas: Image, x: int, y: int) -> Image:
    for i in range(overlay.size[0]):
        for j in range(overlay.size[1]):
            canvas.putpixel((x * 3 + i, y * 3 + j), overlay.getpixel((i, j)))
    return canvas


def save_image(image: Image, name: str) -> None:
    image.save(Path("output_images/archive") / f"{name}-{int(datetime.timestamp(datetime.now()))}.png")
    image.save(Path("output_images") / f"{name}.png")


def main():
    start_CHAD = load_image_from_file(file="start_CHAD_with_link.png")
    start_JRPG = load_image_from_file(file="start_JRPG.png")
    blank_canvas = create_blank_canvas()
    overlay_CHAD = convert_image_to_overlay(image=start_CHAD)
    overlay_JRPG = convert_image_to_overlay(image=start_JRPG)
    canvas_with_chad = place_overlay_on_canvas(overlay=overlay_CHAD, canvas=blank_canvas, x=TOP_LEFT_X, y=TOP_LEFT_Y)
    canvas_with_jrpg = place_overlay_on_canvas(overlay=overlay_JRPG, canvas=canvas_with_chad, x=1688, y=1452)
    save_image(image=canvas_with_jrpg, name="final_CHAD")


if __name__ == "__main__":
    main()
