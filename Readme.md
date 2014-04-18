# AnalysisScripts
A list of scripts released publicly used for malware analysis.
This repository will be updated as soon as a new tool is developed.

## Script lists

- Downloader.Upatre Icon Extractor
- MD5 generator for extracted Downloader.Upatre icons
- IDA script to decrypt encrypted strings in Zbot samples
- Zelix Klassmaster String Decryptor
 
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

### ZbotDecryptString IDA Python Information
The script "ida_python_zbot_string_decrypter.py" is an IDA Python script used to decrypt encrypted strings
in Zbot samples. The algorithm used is the same among different Zbot samples.
The following image shows the encrypted strings:
<p align="center">
  <img src="https://raw.githubusercontent.com/Ptr32Void/AnalysisScript/master/IDAScripts/enc_strings_screen.JPG"/>
</p>
The following image shows the decrypted strings:
<p align="center">
  <img src="https://raw.githubusercontent.com/Ptr32Void/AnalysisScript/master/IDAScripts/dec_strings_screen.JPG"/>
</p>

### Zelix Klassmaster String Decryptor
Zelix Klassmaster String Decryptor is a script that can be used to decrypt strings within Java Classes
obfuscated with Zelix Klassmaster. It requires:
- the keys to be changed (the keys can be found within the .class)
- the strings to be decrypted