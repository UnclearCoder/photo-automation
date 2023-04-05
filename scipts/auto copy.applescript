set folderPath to "/Users/ouslan/Downloads/test/"
set exportPath to "/Users/ouslan/Downloads/finished"

tell application "Pixelmator Pro"
	set originalImages to list folder folderPath without invisibles
	repeat with currentImage in originalImages
		set currentImageFile to (folderPath & currentImage) as POSIX file
		set openedImage to open currentImageFile
		enhance openedImage
		-- denoise openedImage
		set currentImage to currentImage as text
		
		-- Construct a new file name with a timestamp
		set timestamp to do shell script "date +%Y%m%d_%H%M%S"
		set fileName to currentImage & "_" & timestamp & ".jpeg"
		set exportLocation to exportPath & "/" & fileName
		
		-- Export the image with the new file name
		export openedImage to exportLocation as JPEG with properties {compression factor:100}
		close openedImage without saving
	end repeat
end tell