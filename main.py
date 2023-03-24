from subprocess import Popen, PIPE
from applescpt import scpt


script = scpt.format(args='1')
p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
stdout, stderr = p.communicate(script)
