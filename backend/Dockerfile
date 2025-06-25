FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    ffmpeg \
    libsm6 \
    libxext6 \
  && rm -rf /var/lib/apt/lists/*

# Copy your application files
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install GroundingDINO via pip
RUN pip install groundingdino-py

# Install Segment Anything
RUN pip install git+https://github.com/facebookresearch/segment-anything.git

# Install other dependencies
RUN pip install \
    flask \
    flask-cors \
    requests \
    torch==2.7.1 \
    torchvision==0.22.1 \
    opencv-python \
    openmim \
    mmdet

# Expose port (ensure your app uses this when deployed)
ENV PORT=10000
EXPOSE 10000

# Start your Flask app
CMD ["python", "universal_locator.py"]
