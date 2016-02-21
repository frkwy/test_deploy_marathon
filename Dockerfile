FROM python:latest

COPY requirements.txt .

RUN pip3 install --upgrade pip
RUN pip3 install wheel
RUN mkdir wheel
RUN pip3 wheel --wheel=wheel -r requirements.txt




#RUN pip3 install --upgrade pip
#RUN pip3 install -r requirements.txt
COPY testtesttest .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
