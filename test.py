from pytube import Playlist

playlist = Playlist('https://www.youtube.com/watch?v=Oh3dq5V9y40&list=PLDAdYI-EeSPBneHaSKgehE2GKnhpfpgom')


for down in playlist.videos:
    print(down.title)
    down.streams.filter(progressive=True,res ="360p").first().download("/home/vishnudas/Desktop/panda-downloader/Test")