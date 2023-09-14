FROM python:3.11-bullseye
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app .
COPY ./instance .
COPY config.py .
COPY wsgi.py .
ENTRYPOINT [ "flask","run","--host","0.0.0.0"]