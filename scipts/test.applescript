property trackName1 : "spotify:track:622qBEeu9xL0aIXLUypQbS"
property trackName2 : "spotify:track:4DOxrGpSp1hP81huUYM6jp"
property test : True

tell application "spotify"
    if test = True then
    play track "spotify:track:622qBEeu9xL0aIXLUypQbS"
    else
    play track "spotify:track:4DOxrGpSp1hP81huUYM6jp"
    end if
end tell