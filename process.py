from PIL import Image
from PIL.ExifTags import TAGS
import exifread

image = Image.open('data/IMG_0411-edited.JPEG')
exifdata = image.getexif()

for k,v in exifdata.items():
    if k in TAGS:
        print(TAGS[k], v)


f = open('data/IMG_0478.CR2', 'rb')

tags = exifread.process_file(f, details=False)
    
for tag in tags.keys():
    if tag == 'EXIF ISOSpeedRatings':
        print(tags[tag])