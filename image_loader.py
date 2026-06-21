from PIL import Image

def load_image(image_path: str, is_invert: bool, threshold: float) -> Image:
    image = Image.open(image_path.strip('"'))
    gray_img = image.convert("L")
    if is_invert:
        bw_img = gray_img.point(lambda x: 255 if x < threshold else 0, '1')
    else:
        bw_img = gray_img.point(lambda x: 0 if x < threshold else 255, '1')
    return bw_img