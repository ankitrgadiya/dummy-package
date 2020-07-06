FROM ros:melodic-ros-core

RUN apt update && apt install python-pip -y
RUN pip install Flask

WORKDIR /app
COPY . .

CMD ["python2", "app.py"]
