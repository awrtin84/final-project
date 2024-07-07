FROM python:3.12.3

WORKDIR /var/www

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3.12", "main.py"]