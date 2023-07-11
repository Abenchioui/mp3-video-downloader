import os

userinput = input("Enter the URL video :")
os.system("cmd /c yt-dlp.exe -x --embed-thumbnail --audio-format mp3 " + userinput)
print("")
print("download complet")
print("")
os.system("pause")
