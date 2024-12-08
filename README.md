# Update
So it seems that shortly after I posted this one of the places I designed this to work for, specifically because I want to watch Anime with the burned subtitles & the dubbed audio, has now started doing various things to make it no longer work for that.  
One of my biggest frustrations with the Dubbed Anime Market is that The Dubbed videos usually lack the translation of text on-screen or, if they do have it, it is never as nice looking as the fan-made versions.  
Plus the fact that I personally like being able to see the direct subtitles on the screen when I watch rather than just text versions of the Dubbed Audio. 

This is important specifically when the Dub changes things that sometimes do not actually mean the same thing. This was more of a problem with older Anime but still happens today. I could give a dozen examples but an example of a recent one is:
> `I Got a Cheat Skill in Another World and Became Unrivaled in the Real World, Too (2023)` S01E01 @ 13:39
>
> He has just finished testing out, literally swinging once, each overpowered weapon he has inherited.
>
> Sub: {TEXT ON SCREEN} `All prerequisites have been met. All Martial arts skills have been combined. "True Martial Arts 1" Acquired.`  
Sub: {TEXT ON SCREEN} `True Martial Arts: 	 A mental state only accessible to those who have studied all weapons & forms of hand-to-hand combat. It allows for the deft use of all weapons & forms of hand-to-hand combat.`  
Sub: ' None of this makes any sense.  "True Martial Arts"? Really!?,  I can't even really use them!,  But the status display changed regardless.  The huge number of weapon & fighting skills disappeared,  & turned into something called "True Martial Arts" '
> 
> Dub: {TEXT ON SCREEN} No Translation into English  
Dub: {TEXT ON SCREEN} No Translation into English  
Dub: ' None of this makes any sense  True Martial Arts?  I can't even use them!  Despite never raising a fist, the status display changed.  The huge number of weapon & fighting skills disappeared. Guess I'm focusing on close combat now. '

With just the Dub translation you will think he lied every time he uses his weapons, which is quite often. This is just one example, & one I think is pretty bad, but the same problem happens often.

I have developed ways to make it still work, but they are much more complicated & cannot be done with a simple script anymore, as they require analyzing framerates, compressing audio streams, a generally more extreme measures, & require a third-party, non-open-source application.  
If you are interested feel free to PM me for the information, but I will no longer be updating this repository unfortunately.


# Compare_Offset_PySceneDetect
 A script using Python & PySceneDetect results to detect alignment points for 2 video files.

* This script requires Python to run
* This script uses CSV files created with [PySceneDetect](https://www.scenedetect.com/) using the command `scenedetect -i "D:\path\to\file\filename.mp4" detect-content list-scenes` (Other commands may work this is just the one I do to create the CSV file)
* [PySceneDetect](https://www.scenedetect.com/) requires ffmpeg & OpenCV to function

## How To Use
1) Create CSV files for the videos to be aligned using the command 
    -  ***`scenedetect -i "{FULLPATH}\{FILENAME}.{EXT}" detect-content list-scenes`***
    -  ***`scenedetect -i "D:\path\to\file\filename2.mp4" detect-content list-scenes`***
2) Drag both CSV files onto the Script
    - <sup><sub>The file loaded 1st will determine the +/- of the offset in results. It should not be used to determine offset direction</sub></sup>
3) You will get results similar to
    ```
    Comparing files:
    1. D:\path\to\file\filename1\filename1-Scenes.csv
    2. D:\path\to\file\filename1\filename2-Scenes.csv
    
    Best sync offset (in seconds):            -0.057
    Number of matching scenes at this offset:       (247)
    Confidence percentage:                     65.3%

    File Ahead:  D:\path\to\file\filename1\filename2-Scenes.csv
    Other Possible Offsets:
                        -0.056    (127)  -  33.6%
                        +1.438    (19)  -  5.0%
                        -4.004    (15)  -  4.0%
    ------ (Sub) Ahead = (Audio -) | Dub Ahead = (Audio +) ------
    Press Enter to exit...
4) The Results are
    - `Comparing files:` The files being compared
    - `Best sync offset (in seconds):` This is the offset that has the highest number of scenes that align
    - `Number of matching scenes at this offset:` This is the number of scenes that match at the given offset
    - `Confidence percentage:` This is the percentage of the scenes that align at the given offset. 
      - <sub><sup>In the example there are 378 scenes in each file. 247 out of 378 gives us 65.3% of the scenes that align</sub></sup>
    - `File Ahead:` This is the file that is ahead. 
      - <sub><sup>If altering ***this*** file you would need to subtract the offset from this file, making this file start that much sooner</sub></sup>
      - <sub><sup>If altering the ***other*** file you would need to add the offset to this file, making that file start that much later</sub></sup>
    - `Other Possible Offsets:` These are the 3 next most likely offsets displayed as 
      - <sub><sup>`{offset}`  ({Number of matching scenes}) - {Confidence Percentage}</sub></sup>
    - `(Sub) Ahead = (Audio -) | Dub Ahead = (Audio +)` 
      - <sub><sup><sub><sup>This is a note as my normal use of this script is align align Hardcoded Subtitled videos with dubbed audio. This tells me which direction to offset the audio track in MKVtoolNix. The same applies to other videos; (Sub) is Video File, (Dub) is Audio File</sub></sup></sub></sup>
5) If combining the files using `MKVtoolNix`:
    1) Add the 2 files
    2) Turn off the video for the file you want the audio from & the audio for the one you want the video from
    3) Select the audio track
       - Under `[Properties]` > `[Timestamps & Default Duration]` select `Delay (in ms):` & enter the offset without the decimal. In the example it would be `-57` Determine the -/+ by the file that is ahead.


This script is designed to align 2 video files. It works well on 2 files of the same video with different languages, but should work just as well on any videos where the scene transitions are the same, 2 cameras recording the same stage play, High Resolution & Low Resolution versions of the same movie or TV Show, etc. 

This script has a function to detect which file is *"ahead"* but does not seem to work correctly. Hopefully it will be fixed in future updates, but as of now it will show a filename, but running on the same files multiple times will sometimes return a different result. I'm still trying to figure out why & get this sorted out, but the rest of the script works properly. 

I run this on a Windows 11 system, I can make no guarantees that it will work on Linux, but assuming python & PySceneDetect are installed it should work without any major changes.

This script was created with the aid of ChatGPT. It went through many revisions before a working one was finished. I believe there is some leftovers from attempts that did not work, but the script as-is functions.

Any suggestions or modifications are welcome