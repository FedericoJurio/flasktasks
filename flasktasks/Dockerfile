FROM python:3.8-alpine

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# add app
COPY . /usr/src/app

# run server
CMD ["/usr/src/app/entrypoint.sh"]
