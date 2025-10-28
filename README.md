# Video URL to Audio

A simple Python console application to download audio from video URLs.

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

### Basic Usage

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

### Parameters

- `url` (required): URL of the video
- `--output` (optional): Output filename without extension (default: "audio")
- `--download-video` (optional): Keep video file after extraction (default: False)

### Docker Usage

Build the image:
```bash
docker build -t videourl-to-audio .
```

Run:
```bash
docker run -v $(pwd):/app videourl-to-audio "https://example.com/video.mp4"
```

With options:
```bash
docker run -v $(pwd):/app videourl-to-audio "https://example.com/video.mp4" --output my_audio --download-video
```

## Output

- Audio files are saved as MP3 format
- By default, only the audio file is created
- Use `--download-video` to also keep the original video file

