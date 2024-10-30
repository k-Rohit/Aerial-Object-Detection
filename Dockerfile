FROM python:3.10
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 unzip -y && pip install -r requirements.txt


# Expose port 8080
EXPOSE 8080


CMD ["python3", "app.py"]
