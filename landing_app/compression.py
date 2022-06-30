import os
import time

from PIL import Image, ExifTags


def compress_product_image(directory: str, required_quality: int, time_to_compress: int):
    """ Сжатие изображений изделий """
    now = time.time()
    try:
        files = [f for f in os.listdir(directory) if
                 now - os.path.getmtime(f'{directory}/{f}') <= time_to_compress]
    except FileNotFoundError:
        pass
    for f in files:
        im = Image.open(f'{directory}/{f}')
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        exif = im._getexif()
        try:
            if exif[orientation] == 3:
                im = im.rotate(180, expand=True)
            elif exif[orientation] == 6:
                im = im.rotate(270, expand=True)
            elif exif[orientation] == 8:
                im = im.rotate(90, expand=True)
        except (TypeError, KeyError):
            im.save(f'{directory}/{f}', quality=required_quality, optimize=True)
        else:
            im.save(f'{directory}/{f}', quality=required_quality, optimize=True)
