# AnalysisScripts
A list of scripts released publicly used for malware analysis.
This repository will be updated as soon as a new tool is developed.

## Script lists

 - [UpatreIcon] Downloader.Upatre Icon Extractor
 - [Md5UpatreIcons] MD5 generator for extracted Downloader.Upatre icons
 
### Downloader.Upatre Script Information
The script should be copied inside a directory containing a list of samples (Upatre). 
It will extract the icon from all the samples, saving them into the "icon" directory.
The icon is within the resource directory of the samples and have the following characteristics:
- resource type RT_ICON (0x3)
- language 1033 (ENG - US)

I have been doing some research on Upatre samples and I found out that lots of them shares 
the same icon (PDF, WORD, MediaPlayer).
The extracted icons are very similar and can be used (in conjunction with other methods) 
to identify Upatre samples. 
Example:
After extracting the icons from 99 Upatre samples and generating their MD5s, I have identified that 
76.77% of the samples have the same icon.

Moreover, among these icons, some of them are similar and might be possible to identify them with fuzzy 
hashing or other technques. This last idea has not been tested.