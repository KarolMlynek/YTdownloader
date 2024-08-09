from pytube import YouTube

class Downloader:

    def __init__(self, link):
        self.link = link

    def Download(link):
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download()
        except:
            print('An error has occurred')
            print('Download is completed succesfully')
    def check_quality(link):
        yt = YouTube(link)
        print(yt.streams.filter(adaptive=True))
        itnumber = input('Enter itag')
        stream = yt.streams.get_by_itag(int(itnumber))
        print(yt.streams.filter(only_audio=True, adaptive=True))
        itnumber1 = input('Enter itag')
        sound = yt.streams.get_by_itag(int(itnumber1))
        stream.download()
        sound.download()
    def check_itag(link):
        yt = YouTube(link)
        print(yt.streams.filter(adaptive=True))
    #link = input("Enter the YouTube video URL: ")
    #check_quality(link)
    def get_audio(self, link, choosen_itag):
        yt = YouTube(link)
        sound = yt.streams.get_by_itag(choosen_itag)
        sound.download()
    def get_video(self, link, choosen_itag):
        yt = YouTube(link)
        stream = yt.streams.get_by_itag(choosen_itag)
        stream.download()
    def create_audio_dict(self, link):
        audio_dict = {}
        yt = YouTube(link)
        for stream in yt.streams.filter(only_audio=True, adaptive=True):
            audio_dict[stream.itag] = stream.abr, stream.subtype
        return audio_dict

    def create_video_dict(self, link):
        video_dict = {}
        yt = YouTube(link)
        for stream in yt.streams.filter(only_video=True, adaptive=True):
            video_dict[stream.itag] = stream.resolution, stream.subtype
        return video_dict
