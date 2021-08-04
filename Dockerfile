FROM ubuntu:latest

WORKDIR /usr/app

RUN apt-get update && \
    apt-get -y install python3 && \
    apt-get -y install python3-pip && \
    pip3 install wheel && \
    pip3 install twine && \
    pip3 install setuptools && \
    pip3 install pytz

COPY ./ ./ 

RUN python3 setup.py install

CMD ["app" ,"--period", "1mo" ,"--tz", "Europe/Athens", "--t1", "20200101T000000Z", "--t2", "20211212T0000Z"]


