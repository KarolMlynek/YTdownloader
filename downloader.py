from pytube import YouTube

class Downloader:

    def __init__(self, link):
        self.link = link

    def get_audio(self, link, choosen_itag):
        yt = YouTube(link)
        sound = yt.streams.get_by_itag(choosen_itag)
        sound.download(filename_prefix='Audio_')
    def get_video(self, link, choosen_itag):
        yt = YouTube(link)
        stream = yt.streams.get_by_itag(choosen_itag)
        stream.download(filename_prefix='Video_')
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
