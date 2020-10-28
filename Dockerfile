# set base image (host OS)
FROM python:3.8
# set the working directory in the container
WORKDIR /vector-api

ADD setup_api.sh /

COPY . .

# install dependencies
RUN pip install -r requirements.txt

RUN chmod +x /setup_api.sh
RUN /setup_api.sh
