FROM python:3.8

# create and set working directory
RUN mkdir /app
WORKDIR /app

ADD . /app

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8000
ENV DEBUG=0
ENV ALLOWED_HOST_ENV=*

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-setuptools \
        python3-pip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
# install environment dependencies
RUN pip3 install --upgrade pip 

# Install project dependencies
RUN pip3 install -r requirements.txt

EXPOSE 8000
CMD gunicorn passgen.wsgi:application --bind 0.0.0.0:$PORT