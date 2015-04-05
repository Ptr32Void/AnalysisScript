# AnalysisScripts
A list of scripts released publicly used for malware analysis.
This repository will be updated as soon as a new tool is developed.

## Script & Analysis list

- Downloader.Upatre Icon Extractor
- MD5 generator for extracted Downloader.Upatre icons
- IDA script to decrypt encrypted strings in Zbot samples
- Zelix Klassmaster String Decryptor
- Backdoor.Miniduke!gen4 strings decryptor
- Trojan.Netweird logged keys Decryptor
- Analysis of the Advapi32.dll System DLL infected with Trojan.Ransomlock.AP (Trojan.Ransomlk.AP!inf)
 
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

### ZbotDecryptString IDA Python Information  (for IDA)
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

### Zelix Klassmaster String Decryptor (for IDA)
Zelix Klassmaster String Decryptor is a script that can be used to decrypt strings within Java Classes
obfuscated with Zelix Klassmaster. It requires:
- the keys to be changed (the keys can be found within the .class)
- the strings to be decrypted

### Malware Downloader Class
Malware Downloader Class is a Python class that I used to:
- automatically download polymorphic generated files from infected servers
- download Exploit Kit landing pages bypassing User-Agent and Referer checks

### RTF Object extractor
Script used to extract embedded objects (eg.: MZ/DOC) from an RTF file.
Eg.: cee7d315fe5c81c5aaf058e7c76a055a
https://www.virustotal.com/en/file/29f7e528282c39e10f4d377de96219bf7c1aac4ce28df9d2d76a890f05c8e7d6/analysis/

### VBS/Dunihi Uninstaller
This script is a remote VBS.Dunihi Malware Uninstaller. It is a small web server that 
will be able to replace the Dunihi C&C server in order to send the "uninstall command"
to the infected machines. Infected machines must re-route the C2 server traffic to 
the Dunihi Uninstaller server.

### Backdoor.Miniduke!gen4 strings decryptor (for IDA)
Backdoor.Miniduke!gen4 strings decryptor is a script that can be used to decrypt strings related to Miniduke samples.
Example MD5: c8eb6040fd02d77660d19057a38ff769
It works the same way as the Zbot string decryptor works. It needs the start of the list of the encrypted strings and the end of the 
list.

### Trojan.Netweird logged keys Decryptor
Trojan.Netweird logged keys Decryptor is a script that can be used to decrypt keylogged data.
Log files are encrypted and normally stored in: %APPDATA%\Logs\dd-mm-yyyyy
Example MD5: 78ff589aa5e8e174ce66db4bf8c19d84

### Analysis of the Advapi32.dll System DLL infected with Trojan.Ransomlock.AP (Trojan.Ransomlk.AP!inf)
This report is an analysis of an infected system DLL named "Advapi32.dll" with a Ransomlock variant.