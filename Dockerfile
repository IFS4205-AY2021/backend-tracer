FROM python:3
ENV PYTHONUNBUFFERED 1

RUN mkdir /home/tracer
RUN mkdir /home/tracer/app
WORKDIR /home/tracer

COPY requirements.txt ./
RUN pip install -r ./requirements.txt
COPY ./run.sh ./

ENTRYPOINT [ "/bin/bash", "./run.sh" ]
