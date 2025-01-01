
FROM python:3.9


WORKDIR /app

# Instalar curl
RUN apt-get update && apt-get install -y curl

# Instalar dependencias necesarias para compilar psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt /app/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


COPY ./app /app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]