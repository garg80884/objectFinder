# Use an official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Copy files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip

# Install segment-anything and groundingdino from GitHub
RUN pip install \
    git+https://github.com/facebookresearch/segment-anything.git \
    git+https://github.com/IDEA-Research/GroundingDINO.git

# Install local requirements
RUN pip install -r requirements.txt

# Expose port (important for Render)
ENV PORT=10000
EXPOSE 10000
ENV PYTHONPATH="${PYTHONPATH}:/opt/render/project/src/GroundingDINO"

# Start the app
CMD ["python", "universal_locator.py"]
