import os
import exifread
from datetime import datetime
import shutil

# class to get images from camera and get metadata
class Camera:
    def __init__(self, path):
        self.path = path
        self.files = []
        self.iso = {}
        self.date = {}
    
    def get_images(self):
        for file in os.listdir(self.path):
            if file.endswith('.CR2'):
                self.files.append(file)
        return self.files
    
    def get_iso(self):
        self.get_images()
        for file in self.files:
            f = open(self.path + '/' + file, 'rb')
            tags = exifread.process_file(f, details=False)
            for tag in tags.keys():
                if tag == 'EXIF ISOSpeedRatings':
                    self.iso[file] = tags[tag]
        for i in self.iso:
            self.iso[i] = str(self.iso[i])
            self.iso[i] = int(self.iso[i])
        return self.iso
    
    def get_date(self):
        self.get_images()
        for file in self.files:
            f = open(self.path + '/' + file, 'rb')
            tags = exifread.process_file(f, details=False)
            for tag in tags.keys():
                if tag == 'EXIF DateTimeOriginal':
                    self.date[file] = tags[tag]
        for i in self.date:
            self.date[i] = str(self.date[i])
            self.date[i] = datetime.strptime(self.date[i], '%Y:%m:%d %H:%M:%S')
        return self.date

class Process(Camera):
    def __init__(self, path, target, copy):
        self.target = target
        self.path = path
        self.copy = copy
        self.files = []
        self.iso = {}
        self.date = {}
        self.dir = ['enhance', 'denoise', 'superres','denoise_superres']

    def mkdir(self):
        os.chdir = self.path
        for i in self.dir:
            os.mkdir(self.target + '/' + i)
    
    def move(self,super=False):
        self.get_images()
        self.get_iso()
        self.get_date()
        if super == False:
            for i in self.iso:
                if self.iso[i] > 400:
                    shutil.move(self.path + '/' + i, self.target + '/denoise/' + str(self.iso[i]) + '_' + str(self.date[i]) + '.CR2')
                else:
                    shutil.move(self.path + '/' + i, self.target + '/enhance/' + str(self.iso[i]) + '_' + str(self.date[i]) + '.CR2')
        else:
            for i in self.iso:
                if self.iso[i] > 400:
                    shutil.move(self.path + '/' + i, self.target + '/denoise_superres/' + str(self.iso[i]) + '_' + str(self.date[i]) + '.CR2')
                else:
                    shutil.move(self.path + '/' + i, self.target + '/superres/' + str(self.iso[i]) + '_' + str(self.date[i]) + '.CR2')
    def rmdir(self):
        for i in self.dir:
            for file in os.listdir(self.target + '/' + i):
                src = os.path.join(self.target + '/' + i, file)
                dst = os.path.join(self.copy, file)
                shutil.move(src, dst)
            os.rmdir(self.target + '/' + i)
            

if __name__ == '__main__':
    path = '/Users/ouslan/Downloads/test'
    target = '/Users/ouslan/Downloads/target'
    copy = '/Users/ouslan/Downloads/finished'
    pro = Process(path, target, copy)
    pro.mkdir()
    pro.move(super=True)
    pro.rmdir()