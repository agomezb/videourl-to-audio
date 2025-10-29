import typer
import yt_dlp


class AudioDownloader:
    """
    Handles audio/video download and extraction.
    """
    def __init__(self, download_video: bool = False):
        self.download_video = download_video
    
    def download(self, url: str, output: str):
        """
        Download and extract audio from a URL.
        """
        ydl_opts = {
            'format': 'best' if self.download_video else 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'outtmpl': f'{output}.%(ext)s',
            'keepvideo': self.download_video
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            typer.echo(f"Downloading {'video' if self.download_video else 'audio'} from: {url}")
            info = ydl.extract_info(url, download=True)
        
        typer.echo(f"Audio extracted successfully: {output}.mp3")
        
        if self.download_video:
            video_file = ydl.prepare_filename(info)
            typer.echo(f"Video file kept: {video_file}")

