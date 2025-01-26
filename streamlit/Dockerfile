FROM python:3.11-slim

WORKDIR /app

# Встановлення необхідних системних залежностей
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gfortran \
    libatlas-base-dev \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Оновлення pip
RUN pip install --upgrade pip

# Встановлення Python-залежностей
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

# docker-compose down --rmi all --volumes --remove-orphans
# docker-compose up --build

 ## Стягиваем последние изменения из удаленного репозитория
 #git pull origin main

 ## Переключаемся на main
 #git checkout main
 #
 #git pull origin main --rebase
 #

 ## Сливаем ветку master в main
 #git merge master
 #
 ## Если есть конфликты - разрешите их, затем:
 #git commit -am "Resolved merge conflicts"
 #
 ## Отправляем изменения в удаленный репозиторий
 #git push origin main
#
#
#
#
#
#
#
