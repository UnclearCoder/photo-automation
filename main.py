from subprocess import Popen, PIPE
from applescpt import scpt2
from camera import Camera, Process
import os
import shutil

class Auto:
    
    def __init__(self, path, target, copy, superres=False):
        self.path = path
        self.target = target
        self.copy = copy
        self.superres = superres
        self.files = []
        self.iso = {}
        self.date = {}
        self.dir = ['enhance', 'denoise', 'superres','denoise_superres', 'finished']

    def main(self):
        pro = Process(self.path, self.target, self.copy, self.superres)
        pro.mkdir()
        pro.move()
        for i in self.dir[:-1]:
            if i.startswith('denoise'):
                denoise = ''
            else:
                denoise = '-- ' 
            if i.endswith('superres'):
                superres = ''
            else:
                superres = '-- '
            script = scpt2.format(
                path=self.target + '/' + i + '/',
                target=self.target + '/finished/',
                denoise=denoise,
                superres=superres,
                compression='{compression factor:100}')
            p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
            stdout, stderr = p.communicate(script)
        pro.rmdir()


if __name__ == '__main__':
    while True:
        path = input('Enter path to folder: ')
        if os.path.exists(path) == False:
            print('Path does not exist')
            continue
        target = input('Enter path to target folder: ')
        if os.path.exists(target) == False:
            print('Path does not exist')
            continue
        copy = input('Enter path to copy folder: ')
        if os.path.exists(copy) == False:
            print('Path does not exist')
            continue
        superres = input('Superres? (y/n): ')
        if superres == 'y':
            superres = True
        else:
            superres = False
        try:
            auto = Auto(path, target, copy, superres)
            auto.main()
            print('Done')
        except:
            print('Error: Please try again!')
            print('Make sure the paths are correct and the folders are empty.')
            print('If error persists, please contact the developer.')