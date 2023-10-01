FROM python:3.9.1

RUN apt-get update 
RUN apt-get install python3-opencv -y
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install python3-pip -y
RUN pip3 install tensorflow



    
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]

