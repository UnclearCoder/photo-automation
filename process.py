import io
import pyheif
import exifread

f = open('data/IMG_0478.CR2', 'rb')

tags = exifread.process_file(f, details=False)
    
for tag in tags.keys():
    if tag == 'EXIF ISOSpeedRatings':
        print(tags[tag])