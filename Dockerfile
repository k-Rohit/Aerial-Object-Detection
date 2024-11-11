FROM python:3.10

# Set the working directory
WORKDIR /code


# Copy all files to ensure local dependencies are available
COPY . .

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ffmpeg libsm6 libxext6 unzip && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 50505

# Start the application with gunicorn
ENTRYPOINT ["gunicorn", "app:app"]
