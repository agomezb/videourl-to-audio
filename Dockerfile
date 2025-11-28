# Builder stage
FROM python:3.11-slim AS builder

# Install uv
RUN pip install uv

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml .

# Install dependencies into a virtual environment
RUN uv venv /app/.venv && \
    uv pip install --system typer yt-dlp

# Final stage
FROM python:3.11-slim

# Copy ffmpeg from static image
COPY --from=mwader/static-ffmpeg:6.1.1 /ffmpeg /usr/local/bin/
COPY --from=mwader/static-ffmpeg:6.1.1 /ffprobe /usr/local/bin/

# Copy python dependencies from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin/yt-dlp /usr/local/bin/yt-dlp
COPY --from=builder /usr/local/bin/typer /usr/local/bin/typer

# Set working directory
WORKDIR /app

# Copy application files
COPY main.py .
COPY downloader.py .

# Create output directory
WORKDIR /output

# Set entrypoint
ENTRYPOINT ["python", "/app/main.py"]

