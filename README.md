# Video URL to Audio

A simple Python console application to download audio from video URLs. Supports both single URL downloads and batch processing via CSV files.

## Features

- 🎵 Extract audio from video URLs (YouTube, Vimeo, etc.)
- 📦 Batch processing with CSV files
- 🎬 Optional video download
- 🐳 Docker support
- 🧩 Modular architecture

# TL;DR Usage with Docker

Download audio from a video URL:
```bash
docker run -v $(pwd):/app ghcr.io/agomezb/videourl-to-audio:latest "https://example.com/video.mp4"
```

Batch process multiple videos from CSV:
```bash
docker run -v $(pwd):/app ghcr.io/agomezb/videourl-to-audio:latest --csv sample_videos.csv
```

Specify custom output filename:
```bash
docker run -v $(pwd):/app ghcr.io/agomezb/videourl-to-audio:latest "https://example.com/video.mp4" --output my_audio
```

Download video file in addition to audio:
```bash
docker run -v $(pwd):/app ghcr.io/agomezb/videourl-to-audio:latest "https://example.com/video.mp4" --download-video
```



## Requirements

- Python 3.8+
- FFmpeg (required for audio extraction)
- Docker (optional)

## Installation

Install dependencies with uv:

```bash
uv pip install -e .
```

## Usage

### Single Video Download

Download audio only (default):
```bash
python main.py "https://example.com/video.mp4"
```

Specify custom output filename:
```bash
python main.py "https://example.com/video.mp4" --output my_audio
```

Download video file in addition to audio:
```bash
python main.py "https://example.com/video.mp4" --download-video
```

### Batch Processing with CSV

Process multiple videos from a CSV file:
```bash
python main.py --csv sample_videos.csv
```

With video download:
```bash
python main.py --csv sample_videos.csv --download-video
```

**CSV Format:**
```csv
url,output
https://www.youtube.com/watch?v=dQw4w9WgXcQ,song1
https://www.youtube.com/watch?v=9bZkp7q19f0,song2
https://www.youtube.com/watch?v=kJQP7kiw5Fk,song3
```

- `url` (required): The video URL
- `output` (optional): Output filename without extension (defaults to "audio" if not provided)

See `sample_videos.csv` for a working example.

### Parameters

- `url` (optional): URL of the video (required if not using `--csv`)
- `--output` (optional): Output filename without extension (default: "audio")
- `--download-video` (optional): Keep video file after extraction (default: False)
- `--csv` (optional): Path to CSV file for batch processing

### Docker Usage

Build the image:
```bash
docker build -t videourl-to-audio .
```

Run single download:
```bash
docker run -v $(pwd):/app videourl-to-audio "https://example.com/video.mp4"
```

Run batch processing:
```bash
docker run -v $(pwd):/app videourl-to-audio --csv sample_videos.csv
```

With options:
```bash
docker run -v $(pwd):/app videourl-to-audio "https://example.com/video.mp4" --output my_audio --download-video
```

## Project Structure

```
.
├── main.py              # CLI interface and input handling
├── downloader.py        # AudioDownloader class (download logic)
├── sample_videos.csv    # Example CSV file for batch processing
├── pyproject.toml       # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md
```

The project follows a modular design:
- **`main.py`**: Handles CLI arguments and orchestrates the download process
- **`downloader.py`**: Contains the `AudioDownloader` class with all download logic
- **`sample_videos.csv`**: Example CSV file showing the format for batch processing

## Output

- Audio files are saved as MP3 format (192 kbps)
- By default, only the audio file is created
- Use `--download-video` to also keep the original video file
- Output files are saved in the current directory

