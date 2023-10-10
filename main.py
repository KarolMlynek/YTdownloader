from pytube import YouTube
from tkinter import Tk


root = Tk()
root.title("YTDownloader")
root.geometry("800x600")
def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

root.mainloop()
link = input("Enter the YouTube video URL: ")
Download(link)
