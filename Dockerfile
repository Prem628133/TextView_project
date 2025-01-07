FROM python:3.12-slim

WORKDIR /myApp

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

EXPOSE "8001:800"

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
