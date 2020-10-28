from pytube import YouTube
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



#print video resolutions
def printvideo_res(yt):
	print("Available resolutions..")
	print("______________________")
	resolution_yt = [stream.resolution for stream in yt.streams.filter(progressive=True).order_by('resolution').desc()]
	for i in resolution_yt:
		print(color.cyan+i+"\033[0m"+color.white)

#print audio resolutions


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
def download_linux(yt,system_name,res_video):
	try:
		
		try:
			out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="mp4").first().download("/home/"+system_name+"/Desktop/panda-downloader/Videos")
			path="/home/"+system_name+"/Desktop/panda-downloader/Videos"
			convert_video(out_file)
			print("Panda downloaded you file...\n")
			done()
			option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
			if option=="*":
				print("\n \n",path,"\n\n")
				input("Hit Enter to continue....")
		except:
				out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="webm").first().download("/home/"+system_name+"/Desktop/panda-downloader/Videos")
				path="/home/"+system_name+"/Desktop/panda-downloader/Videos"
				convert_video(out_file)
				print("Panda downloaded you file...\n")
				done()
				option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
				if option=="*":
					print("\n \n",path,"\n\n")
					input("Hit Enter to continue....")
	except:
			out_file=yt.streams.filter(progressive=True, resolution=res_video, subtype="3gpp").first().download("/home/"+system_name+"/Desktop/panda-downloader/Videos")
			path="/home/"+system_name+"/Desktop/panda-downloader/Videos"
			convert_video(out_file)
			print("Panda downloaded you file...\n")
			done()
			option=input("Hit Enter for countinue../\npress('*') to display the downloaded path")
			if option=="*":
				print("\n \n",path,"\n\n")
				input("Hit Enter to continue....")
	
		
#downlaod video for windows
def download_windows(yt,system_name,res_video):
	path="C:/Users/"+system_name+"/Desktop/panda-downloader/Videos"
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
def download_audio_linux(yt,system_name,res_video):
	path="/home/"+system_name+"/Desktop/panda-downloader/Videos"
	try:
			out_file=yt.streams.filter(only_audio=True, abr=res_video, subtype='mp4').first().download(path)
			convert_audio(out_file)
			printoli(path)
	except:
			out_file=yt.streams.filter(only_audio=True, abr=res_video, subtype='webm').first().download(path)
			convert_audio(out_file)
			printoli(path)
		

#download for windows

def download_audio_windows(yt,system_name,res_video):
	path="C:/Users/"+system_name+"/Desktop/panda-downloader/Videos"
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
	url=input("[eg:Enter the url:https://youtu.be/gQeYpdXPdE8\n\nEnter the url:")
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
			
			system_name=input("\n [eg Enter  the machines name:DCHACKZzz]\n\nEnter the machines name:")
			download_linux(yt,system_name,res_video)
		elif machine=="2":
			system_name=input("\n [eg Enter  the machines name:DCHACKZzz]\n\nEnter the machines name:")
			download_windows(yt,system_name,res_video)
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
			print("[eg:   Enter the resolution:720]\n\nEnter the option: ",end="")
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
			
			system_name=input("\n [eg Enter  the machines name:DCHACKZzz]\n\nEnter the machines name:")
			download_audio_linux(yt,system_name,res_video)
		elif machine=="2":
			system_name=input("\n [eg Enter  the machines name:DCHACKZzz]\n\nEnter the machines name:")
			download_audio_windows(yt,system_name,res_video)
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


