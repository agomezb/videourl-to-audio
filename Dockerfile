FROM python:3.11-slim

# Install FFmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Set working directory for app
WORKDIR /app

# Copy project files
COPY pyproject.toml .

# Install dependencies
RUN uv pip install --system typer yt-dlp

# Copy application files
COPY main.py .
COPY downloader.py .

# Create output directory and set it as working directory
WORKDIR /output

# Set entrypoint
ENTRYPOINT ["python", "/app/main.py"]

