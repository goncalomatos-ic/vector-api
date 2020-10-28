# set base image (host OS)
FROM python:3.8
# set the working directory in the container
WORKDIR /vector-api

COPY . .

# install dependencies
RUN pip install -r requirements.txt

ADD check_postgres.py /

ADD setup_api.sh /
RUN chmod +x /setup_api.sh
CMD sh /setup_api.sh