tell application "Pixelmator Pro"
	-- Open a prompt to choose the location where the files should be exported 
	set exportLocation to choose folder with prompt "Please select where you'd like export the images:"
	
	-- Get all the images in the selected directory
	set originalImages to every file of exportLocation ¬
		as alias list ¬
		with extension "jpg"
	
	-- Start a repeat loop that loops over each image
	repeat with currentImageAlias in originalImages
		-- Open the current image in the loop
		set currentImage to open currentImageAlias
		
		-- Check if the image needs to be enhanced
		if not (needs auto white balance adjustments of currentImage) then
			-- If the image does not need enhancement, skip to the next image
			close currentImage without saving
			continue repeat
		end if
		
		-- Apply the auto white balance adjustments
		enhance currentImage
		
		-- Check if the image needs to be denoised
		if (noise level of currentImage) < 20 then
			-- If the image has low noise, skip denoising and export the image
			export currentImage to file ((exportLocation as text) & name of currentImage & "-edited" & ".JPEG") as JPEG with properties {compression factor:100}
			-- Close the current image without saving
			close currentImage without saving
		else
			-- If the image has high noise, apply denoising before exporting the image
			denoise currentImage
			-- Export the images to the location chosen previously as JPEG files
			export currentImage to file ((exportLocation as text) & name of currentImage & "-edited" & ".JPEG") as JPEG with properties {compression factor:100}
			-- Close the current image without saving
			close currentImage without saving
		end if
	end repeat
	
	display notification (number of originalImages as text) & " images have been successfully edited." with title "Auto WB and Auto Lightness"
end tell
