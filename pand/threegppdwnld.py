def threegppli(yt,system_name,res_video):
	
	try:
		try:
			yt.streams.filter(progressive=True, subtype="3gpp").first().download("/storage/emulated/0/Download/panda-downloader/videos")
		except:
			yt.streams.filter(progressive=True, subtype="3gpp").first().download("C:/Users/"+system_name+"/Desktop/panda-downloader/Videos")
	except:
		try:
			yt.streams.filter(progressive=True, subtype="3gpp").first().download("/home/"+system_name+"/Desktop/panda-downloader/Videos")
		except:
			yt.streams.filter(progressive=True, subtype="3gpp").first().download()
		
		