from pathlib import Path
from typing import List
from PIL import Image
from datetime import datetime


TOP_LEFT_X = 1895
TOP_LEFT_Y = 3


def load_start() -> Image:
    start_CHAD = Image.open(Path("start_CHAD.png"))
    return start_CHAD


def create_blank_image() -> Image:
    blank_image = Image.new("RGB", (6000, 3000), color="white")
    return blank_image


def convert_image_to_overlay(image: Image) -> Image:
    new_image = Image.new("RGB", (image.size[0] * 3, image.size[1] * 3), color="white")
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            new_image.putpixel(((i * 3) + 1, (j * 3) + 1), image.getpixel((i, j)))
    return new_image


def place_overlay_on_canvas(overlay: Image, canvas: Image) -> Image:
    for i in range(overlay.size[0]):
        for j in range(overlay.size[1]):
            canvas.putpixel((TOP_LEFT_X * 3 + i, TOP_LEFT_Y * 3 + j), overlay.getpixel((i, j)))
    return canvas


def save_image(image: Image, name: str) -> None:
    image.save(Path("output_images") / f"{name}-{int(datetime.timestamp(datetime.now()))}.png")
    image.save(Path("output_images") / f"{name}.png")


def get_colour_pallet_from_image(image: Image) -> list:
    pallet = []
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            if (pixel := image.getpixel((i, j))) not in pallet:
                pallet.append(pixel)
    return pallet


def main():
    start_CHAD = load_start()
    blank_canvas = create_blank_image()
    overlay_CHAD = convert_image_to_overlay(image=start_CHAD)
    save_image(image=overlay_CHAD, name="overlay_CHAD")
    final_CHAD = place_overlay_on_canvas(overlay=overlay_CHAD, canvas=blank_canvas)
    save_image(image=final_CHAD, name="final_CHAD")


if __name__ == "__main__":
    main()
