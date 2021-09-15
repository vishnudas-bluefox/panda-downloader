from pytube import Playlist

playlist = Playlist('https://www.youtube.com/watch?v=58PpYacL-VQ&list=UUd6MoB9NC6uYN2grvUNT-Zg')
print('Number of videos in playlist: %s' % len(playlist.video_urls))