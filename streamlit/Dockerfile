FROM python:3.11-alpine

WORKDIR /app

# Встановлення необхідних системних залежностей
RUN apk add --no-cache \
    g++ \
    gcc \
    musl-dev \
    cmake \
    make \
    libffi-dev \
    openblas-dev \
    lapack-dev \
    freetype-dev \
    libpng-dev \
    jpeg-dev \
    zlib-dev \
    linux-headers \
    py3-pip \
    py3-setuptools \
    py3-wheel

# Оновлення pip
RUN pip install --upgrade pip

# Встановлення Python-залежностей
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]



# docker-compose down --rmi all --volumes --remove-orphans
# docker-compose up --build