from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open('data/IMG_0411-edited.JPEG')
exifdata = image.getexif()

for k,v in exifdata.items():
    if k in TAGS:
        print(TAGS[k], v)