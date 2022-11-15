FROM python:3.11-rc-bullseye


ENV PYTHONUNBUFFERED 1

WORKDIR /OBLIG5

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./OBLIG5 .

RUN python3 manage.py makemigrations mysite
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
