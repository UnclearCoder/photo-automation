import os
from camera import Camera


path = '/Users/ouslan/Downloads/test'
target = '/Users/ouslan/Downloads/target'
x = ['enhance', 'denoise', 'superres','denoise_superres', 'finished']
for i in x:
    print(i)
    if i.startswith('denoise'):
        print('yes')
    else:
        print('no')
    if i.endswith('superres'):
        print('yes')
    else:
        print('no')


# script = scpt2.format(
#             path=auto.target + '/' + i, 
#             target=auto.target + '/finished', 
#             denoise=' ', 
#             superres=' ')
#         p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
#         stdout, stderr = p.communicate(script)