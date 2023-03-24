from subprocess import Popen, PIPE
import os

script = '''
    property test : {args}
    tell application "spotify"
        if test = 1 then
        play track "spotify:track:622qBEeu9xL0aIXLUypQbS"
        else
        play track "spotify:track:4DOxrGpSp1hP81huUYM6jp"
        end if
    end tell
    '''
script = script.format(args='1')
p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
stdout, stderr = p.communicate(script)
