from subprocess import Popen, PIPE
from applescpt import scpt
from camera import Camera
import os
import shutil

path = '/Users/ouslan/Downloads/test'
target = '/Users/ouslan/Downloads/target'
os.chdir(path)
c = Camera(path)
iso = c.get_iso()
date = c.get_date()
os.mkdir(target, )


#for i in iso:
#    shutil.move(i, target + '/' + str(iso[i]) + '_' + str(date[i]) + '.CR2')


# script = scpt.format(args='')
# p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
# stdout, stderr = p.communicate(script)
