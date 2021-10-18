#!/usr/bin/env python3

from pytube import YouTube
from pytube import Playlist	
from pytube.cli import on_progress
import os
import time
import spin



class color:
	white='\033[37m'
	green='\033[32m'
	red='\033[31m'
	cyan='\033[36m'
class backcolor:
	cyan='\033[0m 1;36;40m'

panda ="[DCHACKZzz-Panda-downloader-Github-]"
os.system('clear')


youtube_name='''


░█──░█ █▀▀█ █──█ ▀▀█▀▀ █──█ █▀▀▄ █▀▀ 　 ── 　 ░█▀▀▄ █▀▀█ █───█ █▀▀▄ █── █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█ 
░█▄▄▄█ █──█ █──█ ─░█── █──█ █▀▀▄ █▀▀ 　 ▀▀ 　 ░█─░█ █──█ █▄█▄█ █──█ █── █──█ █▄▄█ █──█ █▀▀ █▄▄▀ 
──░█── ▀▀▀▀ ─▀▀▀ ─░█── ─▀▀▀ ▀▀▀─ ▀▀▀ 　 ── 　 ░█▄▄▀ ▀▀▀▀ ─▀─▀─ ▀──▀ ▀▀▀ ▀▀▀▀ ▀──▀ ▀▀▀─ ▀▀▀ ▀─▀▀
'''

youtube_logo='''


▄███████████▄
█████░▀██████
█████░░░▀████
█████░░░▄████
█████░▄██████
█████████████
─▀▀▀▀▀▀▀▀▀▀▀─
'''
for i in youtube_name:
	print(color.white+i,end="")
	time.sleep(.0005)


print("\033[0;31;47m"+youtube_logo+" \033[0m")
input(color.white+"Hit Enter to continue.....")
print("Panda is wakeing up...",end="")
spin.spin(3)
panda_logo='''



    ____  ____ _____  ____/ /___ _      ____/ /___ _      ______  / /___  ____/ /__  _____
   / __ \/ __ `/ __ \/ __  / __ `/_____/ __  / __ \ | /| / / __ \/ / __ \/ __  / _ \/ ___/
  / /_/ / /_/ / / / / /_/ / /_/ /_____/ /_/ / /_/ / |/ |/ / / / / / /_/ / /_/ /  __/ /    
 / .___/\__,_/_/ /_/\__,_/\__,_/      \__,_/\____/|__/|__/_/ /_/_/\____/\__,_/\___/_/     
/_/                                                                                                     
                                    
                      
            __..                     ..__              
         .gd$$$$$b                 .$$$$$bp.           
        d$$$$$$$$$$               $$$$$$$$$$b          
       g$$$$$$$$$$$$     ___     $$$$$$$$$$$$p         
      !$$$$$$$$$$$$$.--''   ''--.$$$$$$$$$$$$$!        
      !$$$$$$$$$P^"               '-$$$$$$$$$$!        
       T$$$$$$P"                     '-$$$$$$P         
       !$$$$P"                          $$$$$!         
        T$$P                             $$$P           '########::'########::		
         ^$        .             .        $^           	 ##.... ##: ##.... ##:		
         :      .d$$             $$b.      :           	 ##.... ##: ##.... ##:		
         :   .d$$$$$b           d$$$$$b.   :           	 ##:::: ##: ##:::: ##:		
        :   g$$$$$$$$           $$$$$$$$p   :          	 ########:: ##:::: ##:		
        :  d$$$$$$$$$b         d$$$$$$$$$b  :          	 ##.....::: ##:::: ##:
       :  !$$$$$$$$$$$         $$$$$$$$$$$!  :         	 ##:::::::: ##:::: ##:
       :  $$$$$$$(O)$$b _..._ d$$(O)$$$$$$$  :           ##:::::::: ########::
       :  $$$$$$$$$$P^"       "^T$$$$$$$$$$  :          ..:::::::::........:::
        : T$$$$$$$P"     _._     "T$$$$$$$P :          		
        : '$$$$$P       $$$$$       T$$$$$' :          		
        :  "$$$P        "T$P"        T$$$"  :          	Credit:DCHACKZzz(github)
         :   T$           :           $P   :           	Panda-Downloader
         :                :                :           	for
          :    "      _..' '.._      "    :            	powerfull Youtube-downloading
           :   '.                   .'   :             
            '-.                       .-'              
               '-. '-._  __   _.-' .-'                 
                  '--.._ ___ _..--'                    
           ....eee$P"   """""    "T$aaa..._             
      _.ee$$$$$P""                  ""T$$$$$aa.
   .gd$$$$$$$P"                        "T$$$$$$bp.     
                                                       
                                                       

'''
for i in panda_logo:
	print(color.white+i,end="")
	time.sleep(.0005)
#for i in panda_logo:
#	print(color.white+i,end="")
	


laster='''


╔════╦╗───────╔╗
║╔╗╔╗║║───────║║
╚╝║║╚╣╚═╦══╦═╗║║╔╗╔╗─╔╦══╦╗╔╗
──║║─║╔╗║╔╗║╔╗╣╚╝╝║║─║║╔╗║║║║
──║║─║║║║╔╗║║║║╔╗╗║╚═╝║╚╝║╚╝║
──╚╝─╚╝╚╩╝╚╩╝╚╩╝╚╝╚═╗╔╩══╩══╝
──────────────────╔═╝║
──────────────────╚══╝


'''

donist='''


█▀▄ █▀█ █▄░█ █▀▀
█▄▀ █▄█ █░▀█ ██▄
'''

def done():
	for i in donist:
		print(i,end="")
		time.sleep(.0016)

def last():
	for i in laster:
		print(color.cyan+i+"\033[0m",end="")
		time.sleep(.0015)

#print the pathfile after download
def printoli(path):
	done()
	print("Panda downloaded you file...\n")
	option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
	if option=="*":
		print("\n \n",path,"\n\n")
		input("Hit Enter to continue....")


# download instance for playlist

def playlist():
	desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/panda-downloader/Videos')
	try:
		url =input("Enter the url: ")
		p=Playlist(url)
	except:
		print(color.red+"An Error occured please try again..",end="")
		playlist()
	print("Downloading playlist: ",p.title)
	print(color.green+"\n\n++++++++++++++++++++++++++++\033[0m\nThe videos or Audio gonna download is:...\n"+color.green+"++++++++++++++++++++++++++++\n \033[0m")
	def names():
		count =0
		for video in p.videos:
			print(color.cyan+ video.title +"\033[0m")
			count = count+1
		return count
	count =names()
	print(color.green +"\n\nWe gonna download  " , count ," number of videos" +"\033[0m",end="")

	option = input("Hit enter to continue || Press *  for main menu")
	if option == "*":
		startmain()
	else:
		print("Downloading starts ..")

		# downloading starts
		for video in p.videos:
			i=1
			resolution_yt = video.streams.filter(progressive=True)
			for stream in resolution_yt:
				data = stream.resolution
			#print(resolution_yt)
				print(str(i)+". "+data)
				int(i)
				i+=1
			break # fro stoping print the all resolutions 
		
		def download():
			resolution_for_download = input("\nEnter the option (ex:360p) : ")
			resolution_for_download = str(resolution_for_download)+"p"
			
			#download
			
			for down in p.videos:
				
				print(down.title)
				down.register_on_progress_callback(on_progress)
				Rename = down.streams.filter(progressive=True,res=resolution_for_download).first().download(desktop)
				convert_video(Rename)
				print("\n")
		try:
			download()
		except:
			print(color.red + "An Error Occured in Downloading"+"\033[0m",end="")
			download()
			startmain()
			

		

	
#print video resolutions

def printvideo_res(yt):
	print("Available resolutions..")
	print("______________________")
	resolution_yt = [stream.resolution for stream in yt.streams.filter(progressive=True).order_by('resolution').desc()]
	for i in resolution_yt:
		print(color.cyan+i+"\033[0m"+color.white)

#print audio resolutions

def printvideo_reso():
	pass
def printaudio_res(yt):
	print("Available Qualities...")
	print("____________________")
	resolution_yt = [stream.abr for stream in yt.streams.filter(only_audio=True).order_by('abr').desc()]
	for i in resolution_yt:
		print(color.cyan+i+"\033[0m"+color.white)



#rename the video file
def convert_video(out_file):
	base, ext = os.path.splitext(out_file)
	new_file = base +panda+ ext
	os.rename(out_file, new_file)
	
	
#video downlaod section

#download for linux
def download_linux(yt,res_video):
	desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/panda-downloader/Videos') 
	try:
		
		try:
			out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="mp4").first().download(desktop)
			convert_video(out_file)
			print("Panda downloaded you file...\n")
			done()
			option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
			if option=="*":
				print("\n \n",desktop,"\n\n")
				input("Hit Enter to continue....")
		except:
				out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="webm").first().download(desktop)
				convert_video(out_file)
				print("Panda downloaded you file...\n")
				done()
				option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
				if option=="*":
					print("\n \n",desktop,"\n\n")
					input("Hit Enter to continue....")
	except:
			out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="3gpp").first().download(desktop)
			convert_video(out_file)
			print("Panda downloaded you file...\n")
			done()
			option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
			if option=="*":
				print("\n \n",desktop,"\n\n")
				input("Hit Enter to continue....")
	
		
#downlaod video for windows
def download_windows(yt,res_video):
	path= os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop/panda-downloader/Videos')
	try:
		
		try:
			out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="mp4").first().download(path)
			convert_video(out_file)
			print("Panda downloaded you file...\n")
			done()
			option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
			if option=="*":
				print("\n \n",path,"\n\n")
				input("Hit Enter to continue....")
		except:
				out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="webm").first().download(path)
				convert_video(out_file)
				print("Panda downloaded you file...\n")
				done()
				option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
				if option=="*":
					print("\n \n",path,"\n\n")
					input("Hit Enter to continue....")
	except:
			out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="3gpp").first().download(path)
			convert_video(out_file)
			print("Panda downloaded you file...\n")
			done()
			option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
			if option=="*":
				print("\n \n",path,"\n\n")
				input("Hit Enter to continue....")
				

	
		
#downlaod videos foe termux
def download_termux(yt,res_video):
	path="/storage/emulated/0/Download/panda-downloader/videos"
	try:
		
		try:
			out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="mp4").first().download(path)
			convert_video(out_file)
			print("Panda downloaded you file...\n")
			done()
			option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
			if option=="*":
				print("\n \n",path,"\n\n")
				input("Hit Enter to continue....")
		except:
				out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="webm").first().download(path)
				convert_video(out_file)
				print("Panda downloaded you file...\n")
				done()
				option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
				if option=="*":
					print("\n \n",path,"\n\n")
					input("Hit Enter to continue....")
	except:
			out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="3gpp").first().download(path)
			convert_video(out_file)
			print("Panda downloaded you file...\n")
			done()
			option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
			if option=="*":
				print("\n \n",path,"\n\n")
				input("Hit Enter to continue....")

#download video in same directory	
def downlaod_current(yt,res_video):
	path="In this metod Panda download your file in current directory"
	try:
		
		try:
			out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="mp4").first().download()
			convert_video(out_file)
			print("Panda downloaded you file...\n")
			done()
			option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
			if option=="*":
				print("\n \n",path,"\n\n")
				input("Hit Enter to continue....")
		except:
				out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="webm").first().download()
				convert_video(out_file)
				print("Panda downloaded you file...\n")
				done()
				option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
				if option=="*":
					print("\n \n",path,"\n\n")
					input("Hit Enter to continue....")
	except:
			out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="3gpp").first().download()
			convert_video(out_file)
			print("Panda downloaded you file...\n")
			done()
			option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
			if option=="*":
				print("\n \n",path,"\n\n")
				input("Hit Enter to continue....")

#audio download section


#rename and convert mp4 to mp3 
def convert_audio(out_file):
	base, ext = os.path.splitext(out_file)
	new_file = base +panda+ ".mp3"
	os.rename(out_file, new_file)	


#download audio for linux
def download_audio_linux(yt,res_video):
	path= os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop/panda-downloader/Audio') 
	try:
			out_file=yt.streams.filter(only_audio=True, abr=res_video, subtype='mp4').first().download(path)
			convert_audio(out_file)
			printoli(path)
	except:
			out_file=yt.streams.filter(only_audio=True, abr=res_video, subtype='webm').first().download(path)
			convert_audio(out_file)
			printoli(path)
		

#download for windows

def download_audio_windows(yt,res_video):
	path= os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
	try:
			out_file=yt.streams.filter(only_audio=True, abr=res_video, subtype='mp4').first().download(path)
			convert_audio(out_file)
			printoli(path)
	except:
			out_file=yt.streams.filter(only_audio=True, abr=res_video, subtype='webm').first().download(path)
			convert_audio(out_file)
			printoli(path)

#download for termux

def download_audio_termux(yt,res_video):
	path="/storage/emulated/0/Download/panda-downloader/Audio"
	try:
			out_file=yt.streams.filter(only_audio=True, abr=res_video, subtype='mp4').first().download(path)
			convert_audio(out_file)
			printoli(path)
	except:
			out_file=yt.streams.filter(only_audio=True, abr=res_video, subtype='webm').first().download(path)
			convert_audio(out_file)
			printoli(path)



#download for current

def download_audio_current(yt,res_video):
	path="This downloaded file is in this directory \nBecause panda can't find proper location for your machine"
	try:
			out_file=yt.streams.filter(only_audio=True, abr=res_video, subtype='mp4').first().download(path)
			convert_audio(out_file)
			printoli(path)
	except:
			out_file=yt.streams.filter(only_audio=True, abr=res_video, subtype='webm').first().download(path)
			convert_audio(out_file)
			printoli(path)


def runagain():
	option=input("1.Download more content  else:Hit Enter.........")
	if option == "1":
		startmain()
	else:
		last()
		print(color.white+"Panda is going to sleep .....",end="")
		spin.spin(3)
		print("\n\n")
		quit()
		

def startmain():
	option = input("1.Playlist [Note:Linux Only] \nElse Hit Enter....\nEnter the Option: ")

	if option =="1" :
		playlist()
	else:
		url=input("Enter the url: ")
		main(url)


def main(url):
	try:
		#url=input("Enter the url:")
		yt=YouTube(url,on_progress_callback=on_progress)
	except:
		print("pinging...")
		main(url)
	print("Panda is getting up...",end="")
	spin.spin(3)
	print("Name:",yt.title)
	print("Select the for format you want download\n____________________________________\n\n")
	print(color.cyan+"1.Video	 2.Audio\n")
	option=input(color.white+"Enter the option: ")
	if option=="1":
		resolution_videos=[stream.resolution for stream in yt.streams.filter(progressive=True).order_by('resolution').desc()]
		printvideo_res(yt)
		
		def resolut():
			print("[eg:   Enter the resolution:720]\n\nEnter the option: ",end="")
			res=input()
			return res
		
		res_vido=resolut()
		res_video=str(res_vido)+"p"
		flag=0
		for i in resolution_videos:
			if i==res_video:
				flag=1
				
		if flag==1:
			print("THE VALUE ASSIGNED CORRECTLY")
		else:
			print("Try again the resolution you entered is not available")
			res_video=""
			res_vido=""
			resolut()
			
		print()
		print("Enter your machine model")
		print(color.cyan+"1.Linux		2.Windows	3.Termux	4.Same directory\033[0m")
		machine=input(color.white+"Enter the option:")
		if machine=="1":
			download_linux(yt,res_video)
		elif machine=="2":
			download_windows(yt,res_video)
		elif machine=="3":
			download_termux(yt,res_video)
		elif machine=="4":
			downlaod_current(yt,res_video)
		else:
			print(color.red+"*****Unexpected input try again()*****\033[0m"+color.white)
			main(url)
				
	
		runagain()
	elif option =="2":
		resolution_audio=[stream.abr for stream in yt.streams.filter(only_audio=True).order_by('abr').desc()]
		printaudio_res(yt)
		
		def resolut():
			print("[eg:   Enter the Quality:160]\n\nEnter the option: ",end="")
			res=input()
			return res
	
		
		res_vido=resolut()
		res_video=res_vido+"kbps"
		flag=0
		for i in resolution_audio:
			if i==res_video:
				flag=1
				
		if flag==1:
			print("THE VALUE ASSIGNED CORRECTLY")
		else:
			print("Try again the resolution you entered is not available")
			res_video=""
			res_vido=""
			resolut()
		
		print("Enter your machine model")
		print(color.cyan+"1.Linux		2.Windows	3.Termux	4.Same directory\033[0m")
		machine=input(color.white+"Enter the option:")
		if machine=="1":
			download_audio_linux(yt,res_video)
		elif machine=="2":
			download_audio_windows(yt,res_video)
		elif machine=="3":
			download_audio_termux(yt,res_video)
		elif machine=="4":
			download_audio_current(yt,res_video)
		else:
			print(color.red+"*****Unexpected input try again()*****\033[0m"+color.white)
			main(url)
		runagain()
	else:
			print(color.red+"*****Unexpected input try again()*****\033[0m"+color.white)
			main(url)
startmain()
