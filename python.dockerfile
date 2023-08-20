FROM python:3.11.4

WORKDIR /src/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python","-u", "api.py"]

EXPOSE 5000