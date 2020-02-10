FROM python:3.6

ARG COMPRESS_ENABLED

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install -y \
    varnish \
    gettext \
    supervisor \
    curl \
    npm \
    nodejs \
    software-properties-common

# RUN adduser -G django django

RUN npm install npm@latest -g

RUN npm install --global --unsafe-perm \
  coffeescript \
  less \
  yarn \
  tslib

COPY ./package.json /app
RUN npm install

COPY ./pip-freeze.txt /app
RUN pip install --no-cache-dir -r pip-freeze.txt
RUN pip install gevent

COPY . /app
RUN ln -s /app/ureport/settings.py.prod /app/ureport/settings.py

COPY start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
# RUN chown django /start

# RUN chown -R django /app
# USER django

EXPOSE 8000
ENTRYPOINT ["/start"]