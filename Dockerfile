FROM python:3.10.5

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip -y
RUN pip3 install -U pip
RUN mkdir /main/
WORKDIR /main/
COPY . /main/
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
