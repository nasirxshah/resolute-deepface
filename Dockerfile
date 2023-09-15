FROM python:3.11-bullseye
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./app ./app
COPY ./instance ./instance
COPY config.py .
COPY wsgi.py .
EXPOSE 5000
CMD ["gunicorn","-b","0.0.0.0:5000","wsgi:app"]