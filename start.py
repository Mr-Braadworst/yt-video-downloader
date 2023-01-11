from pytube import YouTube
import os, time
import pyfiglet 

os.system('clear') 
os.system('cls') 

ascii_banner = pyfiglet.figlet_format("Yt Downloader")
print(ascii_banner)

print("Mr_Braadworst")
print("https://github.com/Mr-Braadworst")
print("")

link = input("Enter the link: ")
yt = YouTube(link)
print("Title: ",yt.title)
print("Length of video: ",yt.length,"sec")
ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download("video's")
print("Download completed!!")
print("Your video is ready")

os.system('clear') 
os.system('cls') 

os.system("python start.py")
time.sleep(0.2) # 200ms to CTR+C twice






  


  
