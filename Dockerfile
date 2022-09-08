FROM python:3.10.7-slim-bullseye

COPY Pipfile Pipfile.lock ./
COPY ./ /app
WORKDIR /app

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  pipenv install --deploy --system

ENV PATH="/py/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]