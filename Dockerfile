FROM docker.io/library/python:3.14-slim

WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt 

COPY . .

EXPOSE 8080
CMD ["python3", "src/main.py"]