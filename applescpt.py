from subprocess import Popen, PIPE

scpt ='''
    property test : 1
    {args}set test to 0
    tell application "spotify"
        if test = 1 then
        play track "spotify:track:622qBEeu9xL0aIXLUypQbS"
        else
        play track "spotify:track:4DOxrGpSp1hP81huUYM6jp"
        end if
    end tell
    '''
scpt2 ='''
set folderPath to "{path}"
set exportPath to "{target}"

tell application "Pixelmator Pro"
	set originalImages to list folder folderPath without invisibles
	repeat with currentImage in originalImages
		set currentImageFile to (folderPath & currentImage) as POSIX file
		set openedImage to open currentImageFile
		enhance openedImage
		{denoise}denoise openedImage
		{superres}super resolution openedImage
		set currentImage to currentImage as text
		set timestamp to do shell script "date +%Y%m%d_%H%M%S"
		set fileName to currentImage & "_" & timestamp & ".jpeg"
		set exportLocation to exportPath & "/" & fileName
		export openedImage to exportLocation as JPEG with properties {compression}
		close openedImage without saving
	end repeat
end tell
'''

if __name__ == '__main__':
	path = '/Users/ouslan/Downloads/test/'
	target = '/Users/ouslan/Downloads/target/'
	script = scpt2.format(
				path=path,
				target=target,
				denoise='-- ',
				superres='-- ',
				compression='{compression factor:100}')
	p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
	stdout, stderr = p.communicate(script)
	