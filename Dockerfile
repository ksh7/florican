# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /root

COPY . .
RUN pip3 install .

# Install optional dependencies for notifiers
RUN pip3 install slack_sdk hikari twilio python-telegram-bot

RUN florican init

CMD [ "florican", "run" ]
