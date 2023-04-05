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
tell application "Pixelmator Pro"
	-- Open a prompt that lets you pick multiple Pixelmator Pro files to process 
	-- and save references to all those images in the originalImages variable
	set originalImages to choose file with prompt Â
		"Please select the images to process:" with multiple selections allowed
	-- Open a prompt to choose the location where the files should be exported 
	set exportLocation to choose folder with prompt Â
		"Please select where you'd like export the images:"
	-- Start a repeat loop that loops over each image
	repeat with a from 1 to number of originalImages
		-- Open the current image in the loop
		set currentImage to open item a of originalImages
		-- Apply the auto white balance adjustments
		enhance currentImage
		-- Apply denoising
		-- denoise currentImage
		-- Export the images to the location chosen previously as JPEG files
		export currentImage to file ((exportLocation as text) & Â
			name of currentImage & "-edited" & ".JPEG") as JPEG with properties {compression factor:100}
		-- Close the current image without saving
		close currentImage without saving
	end repeat
	display notification (number of originalImages as text) & Â
		" images have been successfully edited." with title "Auto WB and Auto Lightness"
end tell
'''