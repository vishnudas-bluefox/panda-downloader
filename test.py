#!/usr/bin/env python3

import os
import re
import yt_dlp
from typing import Optional, Dict, List, Tuple
from dataclasses import dataclass
from enum import Enum

class Format(Enum):
    VIDEO = "video"
    AUDIO = "audio"

@dataclass
class DownloadOptions:
    url: str
    format_type: Format
    quality: str
    output_path: str

class Colors:
    GREEN = '\033[32m'
    RED = '\033[31m'
    CYAN = '\033[36m'
    YELLOW = '\033[33m'
    END = '\033[0m'

class YouTubeDownloader:
    def __init__(self):
        self.base_output_template = "%(title)s.%(ext)s"

    def _get_info(self, url: str) -> Optional[Dict]:
        """Get video information including available formats"""
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(url, download=False)
        except Exception as e:
            print(f"{Colors.RED}Error fetching video info: {str(e)}{Colors.END}")
            return None

    def _parse_formats(self, formats: List[Dict]) -> Tuple[List[str], List[str]]:
        """Parse available video and audio formats"""
        video_qualities = set()
        audio_qualities = set()

        for f in formats:
            # Video formats
            if f.get('vcodec') != 'none' and f.get('acodec') != 'none':
                height = f.get('height')
                if height:
                    video_qualities.add(f'{height}p')

            # Audio formats
            if f.get('acodec') != 'none' and f.get('vcodec') == 'none':
                abr = f.get('abr')
                if abr:
                    audio_qualities.add(f'{int(abr)}k')

        return (sorted(list(video_qualities), key=lambda x: int(x[:-1]), reverse=True),
                sorted(list(audio_qualities), key=lambda x: int(x[:-1]), reverse=True))

    def get_available_qualities(self, url: str) -> Tuple[List[str], List[str]]:
        """Get available video and audio qualities"""
        info = self._get_info(url)
        if info and 'formats' in info:
            return self._parse_formats(info['formats'])
        return ([], [])

    def _create_output_path(self, url: str, is_playlist: bool) -> str:
        """Create and return output directory path"""
        try:
            info = self._get_info(url)
            if is_playlist and info:
                # Clean playlist title for folder name
                playlist_title = re.sub(r'[<>:"/\\|?*]', '_', info.get('title', 'playlist'))
                output_path = os.path.join(os.getcwd(), playlist_title)
            else:
                output_path = os.getcwd()

            os.makedirs(output_path, exist_ok=True)
            return output_path
        except Exception as e:
            print(f"{Colors.RED}Error creating output directory: {str(e)}{Colors.END}")
            return os.getcwd()

    def _get_format_string(self, quality: str, format_type: Format) -> str:
        """Generate format string based on quality and type"""
        if format_type == Format.VIDEO:
            return f'bestvideo[height<={quality[:-1]}]+bestaudio/best[height<={quality[:-1]}]/best'
        else:
            return 'bestaudio/best'

    def _get_download_options(self, options: DownloadOptions) -> Dict:
        """Get yt-dlp options based on download options"""
        format_string = self._get_format_string(options.quality, options.format_type)
        
        ydl_opts = {
            'format': format_string,
            'outtmpl': os.path.join(options.output_path, self.base_output_template),
            'progress_hooks': [self._progress_hook],
        }

        if options.format_type == Format.AUDIO:
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': options.quality[:-1],  # Remove 'k' from quality
            }]

        return ydl_opts

    def _progress_hook(self, d):
        """Display download progress"""
        if d['status'] == 'downloading':
            percentage = d.get('_percent_str', '0%')
            speed = d.get('_speed_str', 'N/A')
            print(f"\rDownloading... {percentage} at {speed}", end='')
        elif d['status'] == 'finished':
            print(f"\n{Colors.GREEN}Download completed!{Colors.END}")

    def download(self, options: DownloadOptions) -> bool:
        """Download video or audio from URL"""
        try:
            ydl_opts = self._get_download_options(options)
            
            print(f"{Colors.CYAN}Starting download...{Colors.END}")
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([options.url])
            return True

        except Exception as e:
            print(f"{Colors.RED}Error during download: {str(e)}{Colors.END}")
            return False

class UserInterface:
    @staticmethod
    def print_banner():
        banner = """
        ╔═══════════════════════════════════════╗
        ║           YouTube Downloader          ║
        ║        Video and Audio Grabber       ║
        ╚═══════════════════════════════════════╝
        """
        print(f"{Colors.CYAN}{banner}{Colors.END}")

    @staticmethod
    def print_qualities(video_qualities: List[str], audio_qualities: List[str]):
        """Print available qualities"""
        print(f"\n{Colors.YELLOW}Available Video Qualities:{Colors.END}")
        for i, q in enumerate(video_qualities, 1):
            print(f"{i}. {q}")

        print(f"\n{Colors.YELLOW}Available Audio Qualities:{Colors.END}")
        for i, q in enumerate(audio_qualities, 1):
            print(f"{i}. {q}")

    def get_download_options(self, downloader: YouTubeDownloader) -> DownloadOptions:
        """Get download options from user input"""
        url = input(f"{Colors.CYAN}Enter URL: {Colors.END}")
        
        # Get available qualities
        video_qualities, audio_qualities = downloader.get_available_qualities(url)
        
        format_choice = input(
            f"{Colors.CYAN}Select format:\n"
            "1. Video\n"
            "2. Audio (MP3)\n"
            f"Choice (1/2): {Colors.END}"
        )
        
        format_type = Format.VIDEO if format_choice == "1" else Format.AUDIO
        
        # Show available qualities and get user choice
        self.print_qualities(video_qualities, audio_qualities)
        qualities = video_qualities if format_type == Format.VIDEO else audio_qualities
        
        if not qualities:
            print(f"{Colors.YELLOW}No quality information available. Using best quality.{Colors.END}")
            quality = "best"
        else:
            try:
                quality_index = int(input(f"\n{Colors.CYAN}Select quality (1-{len(qualities)}): {Colors.END}")) - 1
                quality = qualities[quality_index]
            except (ValueError, IndexError):
                print(f"{Colors.YELLOW}Invalid selection. Using best quality.{Colors.END}")
                quality = qualities[0] if qualities else "best"

        # Create output path (handles playlist folders)
        is_playlist = "playlist" in url.lower()
        output_path = downloader._create_output_path(url, is_playlist)
        
        return DownloadOptions(url, format_type, quality, output_path)

def main():
    ui = UserInterface()
    downloader = YouTubeDownloader()
    
    ui.print_banner()
    
    while True:
        try:
            options = ui.get_download_options(downloader)
            downloader.download(options)
            
            if input(f"\n{Colors.CYAN}Download another? (y/n): {Colors.END}").lower() != 'y':
                break
                
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}Download cancelled by user{Colors.END}")
            break
        except Exception as e:
            print(f"{Colors.RED}An error occurred: {str(e)}{Colors.END}")
            continue

if __name__ == "__main__":
    main()