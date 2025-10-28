import typer
import yt_dlp

app = typer.Typer()


@app.command()
def main(
    url: str = typer.Argument(..., help="URL of the video to download"),
    output: str = typer.Option("audio", help="Name of the output audio file (without extension)"),
    download_video: bool = typer.Option(False, "--download-video", help="Download video file in addition to extracting audio"),
):
    """
    Download video from URL and extract audio.
    """
    try:
        # Configure yt-dlp options
        ydl_opts = {
            'format': 'best' if download_video else 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'outtmpl': f'{output}.%(ext)s',
            'keepvideo': download_video
        }
        
        # Download and extract audio
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            if download_video:
                typer.echo(f"Downloading video from: {url}")
            else:
                typer.echo(f"Downloading audio from: {url}")
            info = ydl.extract_info(url, download=True)
        
        output_file = f"{output}.mp3"
        typer.echo(f"Audio extracted successfully: {output_file}")
        
        if download_video:
            video_file = ydl.prepare_filename(info)
            typer.echo(f"Video file kept: {video_file}")
            
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()

