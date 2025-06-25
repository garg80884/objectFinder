# ---------- Dockerfile ----------
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y git build-essential ffmpeg libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Copy all project files
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install core dependencies
RUN pip install \
    flask flask-cors requests opencv-python openmim mmdet \
    torch==2.7.1 torchvision==0.22.1

# Install GroundingDINO from PyPI
RUN pip install groundingdino-py

# Install Segment Anything (if needed)
RUN pip install git+https://github.com/facebookresearch/segment-anything.git

# Expose the port used by your app
ENV PORT=10000
EXPOSE 10000

# Run the backend
CMD ["python", "universal_locator.py"]
