def mpfour(yt,system_name,res_video):
	
	try:
		try:
			yt.streams.filter(progressive=True, subtype="mp4").first().download("/storage/emulated/0/Download/panda-downloader/videos")
			path="/storage/emulated/0/Download/panda-downloader/videos"
		except:
			yt.streams.filter(progressive=True, subtype="mp4").first().download("C:/Users/"+system_name+"/Desktop/panda-downloader/Videos")
	except:
		try:
			yt.streams.filter(progressive=True, subtype="mp4").first().download("/home/"+system_name+"/Desktop/panda-downloader/Videos")
		except:
			yt.streams.filter(progressive=True, subtype="mp4").first().download()
		
		