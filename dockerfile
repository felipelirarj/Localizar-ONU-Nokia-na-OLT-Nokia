FROM python:3.11

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Setup the virtualenv
RUN python -m venv /venv
RUN . /venv/bin/activate

COPY requirements.txt ./
RUN /venv/bin/python -m pip install --upgrade pip && \
    python -m pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 5000