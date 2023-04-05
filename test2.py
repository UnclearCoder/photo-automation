import os
from camera import Camera


path = '/Users/ouslan/Downloads/test'
target = '/Users/ouslan/Downloads/target'

c = Camera(path)
iso = c.get_iso()

for i in iso:
    print(i)