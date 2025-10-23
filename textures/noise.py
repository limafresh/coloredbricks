from PIL import Image
import random
import argparse


def apply_noise_to_image(image_path, output_path, intensity):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            noise = random.randint(-intensity, intensity)
            r = min(max(r + noise, 0), 255)
            g = min(max(g + noise, 0), 255)
            b = min(max(b + noise, 0), 255)
            pixels[x, y] = (r, g, b)

    img.save(output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Применить шум к текстуре")
    parser.add_argument("input", help="Путь к исходной текстуре")
    parser.add_argument("output", help="Путь к выходной текстуре")
    parser.add_argument(
        "-i",
        "--intensity",
        type=int,
        default=15,
        help="Интенсивность шума (по умолчанию 15)",
    )

    args = parser.parse_args()
    apply_noise_to_image(args.input, args.output, args.intensity)
