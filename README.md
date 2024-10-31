# Compare_Offset_PySceneDetect
 A script using Python & PySceneDetect results to detect alignment points for 2 video files.

* This script requires Python to run
* This script uses CSV files created with [PySceneDetect](https://www.scenedetect.com/) using the command `scenedetect -i "D:\path\to\file\filename.mp4" detect-content list-scenes` (Other commands may work this is just the one I do to create the CSV file)
* [PySceneDetect](https://www.scenedetect.com/) requires ffmpeg & OpenCV to function

This script is designed to align 2 video files. It works well on 2 files of the same video with different languages, but should work just as well on any videos where the scene transitions are the same, 2 cameras recording the same stage play, High Resolution & Low Resolution versions of the same movie or TV Show, etc. 

This script has a function to detect which file is *"ahead"* but does not seem to work correctly. Hopefully it will be fixed in future updates, but as if now it will show a filename, but running on the same files multiple times will return both results.

I run this on a Windows 11 system, I can make no guarantees that it will work on Linux, but assuming python & PySceneDetect are installed it should work without any major changes.

This script was created with the aid of ChatGPT. It went through many revisions before a working one was finished. I believe there is some leftovers from attempts that did not work, but the script as-is functions.

Any suggestions or modifications are welcome