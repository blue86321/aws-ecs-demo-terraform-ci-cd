FROM python:3.12-slim

WORKDIR /app
COPY . .

# To resolve `psycopg2` install problem
# Source: https://stackoverflow.com/questions/11618898/pg-config-executable-not-found
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  libpq-dev \
  python3-dev \
  gcc \
  # for health check on AWS ECS
  curl

# Install dependencies
RUN pip install -r requirements.txt

# Don't buffer `stdout` and `stderr`
ENV PYTHONUNBUFFERED 1

EXPOSE 80

# CMD ["fastapi", "dev", "main.py"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]