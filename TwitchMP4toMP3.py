import os

#manual folder path
path = "D:\python_mp4_test"

files = os.listdir(path)
print (files)


for f in files:
    if f.endswith(".mp4"):
        
        full_MP4_path =( path + "\\" + f)
        #print(f"MP4 input file: "+ full_MP4_path)
        fileoutputname = f.replace("mp4","mp3")
        #print (f"MP3 output name: " + fileoutputname)
        filename_input_doublequotes = '"' + full_MP4_path + '"'
        print (f"converting file"+ filename_input_doublequotes)
        import subprocess
        FNULL = open(os.devnull, 'w')            
        args = "c:\PROGRA~1\VideoLAN\VLC\\vlc.exe  " +   filename_input_doublequotes  + " " + "--sout=#transcode{acodec=mp3,ab=320,vcodec=dummy}:std{access=\"file\",mux=\"raw\",dst=\"" +fileoutputname  +"\"} vlc://quit """
        print(f"starting app: " +args)
        subprocess.call(args, cwd=path, stdout=FNULL, stderr=FNULL, shell=False)


