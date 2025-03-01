FROM python:3.11-slim

WORKDIR /src
RUN apt-get update \
    && apt-get install gcc build-essential -y
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY Makefile requirements.txt /src/
RUN make install
RUN pip install psycopg2-binary
COPY ./app ./app

CMD make run
EXPOSE 80
