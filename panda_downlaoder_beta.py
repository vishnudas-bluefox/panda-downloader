import yt_dlp
import os
from pathlib import Path
import sys
import time
import threading
from itertools import cycle
from typing import Dict, Any

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class LoadingSpinner:
    def __init__(self, message="Loading..."):
        self.spinner = cycle(['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏'])
        self.stop_spinner = False
        self.spinner_thread = None
        self.message = message

    def spin(self):
        while not self.stop_spinner:
            sys.stdout.write(f"\r{Colors.BLUE}{self.message} {next(self.spinner)}{Colors.ENDC}")
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r' + ' ' * (len(self.message) + 2) + '\r')
        sys.stdout.flush()

    def __enter__(self):
        self.stop_spinner = False
        self.spinner_thread = threading.Thread(target=self.spin)
        self.spinner_thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_spinner = True
        if self.spinner_thread:
            self.spinner_thread.join()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    clear_screen()
    print(f"{Colors.HEADER}{'=' * 50}")
    print("YouTube Video/Playlist Downloader")
    print(f"{'=' * 50}{Colors.ENDC}\n")

def get_url() -> str:
    while True:
        url = input(f"{Colors.BLUE}Enter YouTube URL (video or playlist): {Colors.ENDC}").strip()
        if 'youtube.com' in url or 'youtu.be' in url:
            return url
        print(f"{Colors.RED}Invalid YouTube URL. Please try again.{Colors.ENDC}")

def is_playlist() -> bool:
    return 'n'
    while True:
        choice = input(f"{Colors.YELLOW}Is this a playlist? (y/n): {Colors.ENDC}").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print(f"{Colors.RED}Please enter 'y' or 'n'{Colors.ENDC}")

def get_video_info(url: str) -> Dict[str, Any]:
    with LoadingSpinner("Fetching video information"):
        try:
            ydl_opts = {
                'quiet': True,
                'extract_flat': True,
                'socket_timeout': 10,  # 10 seconds timeout
                'retries': 3,  # Retry 3 times if download fails
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    return ydl.extract_info(url, download=False)
                except yt_dlp.utils.DownloadError as e:
                    print(f"\n{Colors.RED}Error: Could not fetch video information. {str(e)}{Colors.ENDC}")
                    retry = input(f"\n{Colors.YELLOW}Would you like to retry? (y/n): {Colors.ENDC}").lower()
                    if retry == 'y':
                        return get_video_info(url)
                    sys.exit(1)
                except Exception as e:
                    print(f"\n{Colors.RED}An unexpected error occurred: {str(e)}{Colors.ENDC}")
                    sys.exit(1)
        except KeyboardInterrupt:
            print(f"\n{Colors.YELLOW}Operation cancelled by user.{Colors.ENDC}")
            sys.exit(0)

def select_quality() -> str:
    qualities = {
        '1': ('best', 'Best Quality'),
        '2': ('1080p', '1080p'),
        '3': ('720p', '720p'),
        '4': ('480p', '480p'),
        '5': ('worst', 'Lowest Quality')
    }
    
    print(f"\n{Colors.GREEN}Available Quality Options:{Colors.ENDC}")
    for key, (_, desc) in qualities.items():
        print(f"{key}. {desc}")
    
    while True:
        choice = input(f"\n{Colors.YELLOW}Select quality (1-5): {Colors.ENDC}")
        if choice in qualities:
            return qualities[choice][0]
        print(f"{Colors.RED}Invalid choice. Please select 1-5.{Colors.ENDC}")

def select_format() -> str:
    formats = {
        '1': ('mp4', 'MP4'),
        '2': ('mkv', 'MKV'),
        '3': ('webm', 'WebM')
    }
    
    print(f"\n{Colors.GREEN}Available Formats:{Colors.ENDC}")
    for key, (_, desc) in formats.items():
        print(f"{key}. {desc}")
    
    while True:
        choice = input(f"\n{Colors.YELLOW}Select format (1-3): {Colors.ENDC}")
        if choice in formats:
            return formats[choice][0]
        print(f"{Colors.RED}Invalid choice. Please select 1-3.{Colors.ENDC}")

def get_output_path() -> str:
    default_path = "downloads"
    path = input(f"\n{Colors.BLUE}Enter output directory path (press Enter for '{default_path}'): {Colors.ENDC}").strip()
    return path if path else default_path

def create_format_selector(quality: str) -> str:
    if quality == 'best':
        return 'bestvideo+bestaudio/best'
    elif quality == 'worst':
        return 'worstvideo+worstaudio/worst'
    elif quality in ['1080p', '720p', '480p']:
        height = quality[:-1]
        return f'bestvideo[height<={height}]+bestaudio/best[height<={height}]'
    return 'bestvideo+bestaudio/best'

class DownloadProgress:
    def __init__(self):
        self.start_time = time.time()
    
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            filename = d.get('filename', '').split('/')[-1]
            percent = d.get('_percent_str', '').strip()
            speed = d.get('_speed_str', '').strip()
            eta = d.get('_eta_str', '').strip()
            
            clear_screen()
            print(f"{Colors.GREEN}Downloading: {filename}{Colors.ENDC}")
            print(f"Progress: {percent}")
            print(f"Speed: {speed}")
            print(f"ETA: {eta}")

def download_content(url: str, output_path: str, quality: str, format: str, is_playlist: bool):
    Path(output_path).mkdir(parents=True, exist_ok=True)
    
    progress_tracker = DownloadProgress()
    
    ydl_opts = {
        'format': create_format_selector(quality),
        'merge_output_format': format,
        'outtmpl': (
            os.path.join(output_path, '%(playlist_title)s', '%(playlist_index)s-%(title)s.%(ext)s')
            if is_playlist
            else os.path.join(output_path, '%(title)s.%(ext)s')
        ),
        'progress_hooks': [progress_tracker.progress_hook],
        'ignoreerrors': True,
        'continuedl': True,
        'quiet': False,
        'no_warnings': False,
        'socket_timeout': 10,
        'retries': 3,
    }

    if is_playlist:
        ydl_opts.update({
            'extract_flat': 'in_playlist',
            'playlistrandom': False,
            'playliststart': 1,
            'playlistend': None,
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            error_code = ydl.download([url])
            
            if error_code == 0:
                print(f"\n{Colors.GREEN}Download completed successfully!{Colors.ENDC}")
            else:
                print(f"\n{Colors.RED}Some errors occurred during download. Error code: {error_code}{Colors.ENDC}")
    
    except Exception as e:
        print(f"\n{Colors.RED}An error occurred: {str(e)}{Colors.ENDC}")
        retry = input(f"\n{Colors.YELLOW}Would you like to retry? (y/n): {Colors.ENDC}").lower()
        if retry == 'y':
            download_content(url, output_path, quality, format, is_playlist)

def main():
    try:
        while True:
            print_header()
            
            # Get download information
            url = get_url()
            playlist_flag = is_playlist()
            
            # Get video/playlist information
            info = get_video_info(url)
            if info:
                if playlist_flag:
                    print(f"\n{Colors.GREEN}Playlist: {info.get('title', 'Unknown')}")
                    print(f"Number of videos: {len(info.get('entries', []))}{Colors.ENDC}")
                else:
                    print(f"\n{Colors.GREEN}Video: {info.get('title', 'Unknown')}{Colors.ENDC}")
            
                # Get download preferences
                quality = select_quality()
                format_choice = select_format()
                output_path = get_output_path()
                
                # Show summary
                print(f"\n{Colors.BOLD}Download Summary:{Colors.ENDC}")
                print(f"URL: {url}")
                print(f"Type: {'Playlist' if playlist_flag else 'Single Video'}")
                print(f"Quality: {quality}")
                print(f"Format: {format_choice}")
                print(f"Output: {output_path}")
                
                # Confirm and download
                if input(f"\n{Colors.YELLOW}Start download? (y/n): {Colors.ENDC}").lower() == 'y':
                    download_content(url, output_path, quality, format_choice, playlist_flag)
            
            # Ask for another download
            if input(f"\n{Colors.BLUE}Download another video/playlist? (y/n): {Colors.ENDC}").lower() != 'y':
                break
        
        print(f"\n{Colors.GREEN}Thank you for using YouTube Downloader!{Colors.ENDC}")
    
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Download cancelled by user.{Colors.ENDC}")
        sys.exit(0)

if __name__ == "__main__":
    main()