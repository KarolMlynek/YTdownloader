from pytube import YouTube


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
    itnumber1 = int('Enter itag')
    sound = yt.streams.get_by_itag(int(itnumber1))
    stream.download()
    sound.download()
def check_itag(link):
    yt= YouTube(link)
    print(yt.streams.filter(adaptive=True))
link = input("Enter the YouTube video URL: ")
check_quality(link)