from PIL import Image


def mess_up(in_image_path, out_image_path):
    img = Image.open(in_image_path)
    (width, height) = img.size
    (new_width, new_height) = (width // 2, height * 2)
    img = img.resize((new_width, new_height), Image.BILINEAR)
    img = img.transpose(Image.ROTATE_90)
    img.save(out_image_path)
