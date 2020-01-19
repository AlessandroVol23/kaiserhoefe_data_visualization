FROM python:3.7
RUN apt update && apt-get install -y libspatialindex-dev
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY . /kaiser_hoefe
WORKDIR /kaiser_hoefe