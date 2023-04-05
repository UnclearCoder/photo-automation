tell application "Pixelmator Pro"
	set originalImages to choose file with prompt �
		"Please select the images to process:" with multiple selections allowed
	set exportLocation to choose folder with prompt �
		"Please select where you'd like export the images:"
	repeat with a from 1 to number of originalImages
		set currentImage to open item a of originalImages
		enhance currentImage
		-- Apply denoising
		-- denoise currentImage
		export currentImage to file ((exportLocation as text) & �
			name of currentImage & "-edited" & ".JPEG") as JPEG with properties {compression factor:100}
		close currentImage without saving
	end repeat
	display notification (number of originalImages as text) & �
		" images have been successfully edited." with title "Auto WB and Auto Lightness"
end tell