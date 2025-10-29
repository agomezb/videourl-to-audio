import csv
import typer
from downloader import AudioDownloader

app = typer.Typer()


@app.command()
def main(
    url: str = typer.Argument(None, help="URL of the video to download"),
    output: str = typer.Option("audio", help="Name of the output audio file (without extension)"),
    download_video: bool = typer.Option(False, "--download-video", help="Download video file in addition to extracting audio"),
    csv_file: str = typer.Option(None, "--csv", help="CSV file with URLs (columns: url,output)"),
):
    """
    Download video from URL and extract audio. Supports batch processing via CSV.
    """
    try:
        downloader = AudioDownloader(download_video=download_video)
        
        if csv_file:
            # Batch mode: process CSV file
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    video_url = row.get('url')
                    video_output = row.get('output', 'audio')
                    if video_url:
                        downloader.download(video_url, video_output)
        elif url:
            # Single mode: process one URL
            downloader.download(url, output)
        else:
            typer.echo("Error: Provide either a URL or --csv file", err=True)
            raise typer.Exit(code=1)
            
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()

