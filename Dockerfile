FROM python:latest

COPY requirements.txt .

ADD wheel /wheel
RUN ls
RUN pip3 install --upgrade pip
RUN pip3 install --use-wheel --find-links=wheel Django requests marathon slackclient

COPY testtesttest .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
