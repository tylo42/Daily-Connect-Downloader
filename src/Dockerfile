FROM debian:latest

RUN apt-get update && DEBIAN_FROINTEND=noninteractive apt-get install -yq python wget jhead
RUN apt-get clean

WORKDIR /share

ADD run.py /root/run.py
ENTRYPOINT ["/root/run.py"]
