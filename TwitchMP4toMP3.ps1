#version09.6.2021-2

$space = " "
Get-ChildItem *.mp4 | ForEach-Object  {
$fileoutputname = $_.BaseName
$vlcconvertparameter = "--sout=#transcode{acodec=mp3,ab=320,vcodec=dummy}:std{access=`"file`",mux=`"raw`",dst="" $fileoutputname "".mp3} vlc://quit "

Write-Host  -ForegroundColor Cyan "converting:" $fileoutputname


$argument = "`"$_`"" + $space + $vlcconvertparameter
 Write-Host -ForegroundColor DarkRed $argument
            Start-Process -FilePath 'C:\Program Files\VideoLAN\VLC\vlc.exe' -ArgumentList "$argument " -Wait

#log
$argument  | Out-File -FilePath twitch.log -Append
Get-Date | Out-File -FilePath twitch.log -Append
 
  } 


