FROM debian:latest

LABEL maintainer="zubeax@kippel.de"

USER root

RUN apt-get update && apt-get -y install build-essential python3 python3-pip python3-dev python3-venv

ADD ./app/ /app

RUN python3 -m venv /app/quizenv
RUN . /app/quizenv/bin/activate && pip3 install -r /app/requirements.txt

#we need a numeric user to be compliant with OCP rules
RUN chown -R 1000480000 /app
USER 1000480000

EXPOSE 8000

CMD cd /app && . /app/quizenv/bin/activate && echo "PATH=$PATH" && ls -la /app/quizenv/bin && /app/quizenv/bin/gunicorn --bind=0.0.0.0 --timeout 600 --log-level debug quiz:app
