# TwitchMP4toMP3
Simple batch file to convert downloaded MP4 vods from TwitchLeecher to MP3

batch file will create MP3 file for every MP4 in same folder


Requirements:
VLC media player

Recommendations:
Disable repeat/loop function in VLC

Steps:
1. Download vods via https://github.com/Franiac/TwitchLeecher 
2. In folder with MP4 vods run TwitchMP4toMP3.bat
3. Wait until VLC quit 
4. profit


Powershell version:
+ works on UNC paths (network shares)
+ log input + output file names with date to current folder 

Python version:
+ currently with hardcoded source path
