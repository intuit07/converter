import os
import sys

from PIL import Image

print("Hi, I am image format converter :-) PNG <-> JPEG")

image_path = sys.argv[1] if len(sys.argv) > 1 else None
if not image_path:
    print('Usage:\n$ python3 conv3.py <path_to_image>')
    sys.exit(0)

if os.path.exists(image_path):

    img = Image.open(image_path)
    print("Image Size: {}x{}".format(*img.size))
    image_format = img.format
    print("Old Image format:", image_format)

    new_path = img.filename.rpartition('.')[0]  # This is a built-in string method, read more about it.
    if image_format == "PNG":
        img.save(new_path + '.jpg')
        print("Image saved in new format JPG ")
    elif image_format in ("JPG", "JPEG"):
        img.save(new_path + '.png')
        print("Image saved in new format PNG")
