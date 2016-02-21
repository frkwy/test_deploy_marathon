FROM python:latest

ADD wheel /wheel
RUN pip3 install --upgrade pip
RUN pip3 install --use-wheel --find-links=/wheel -r /wheel/requirements.txt
RUN ls
COPY testtesttest/ .
#CMD ["python3", "manage.py", "test", "--settings=tests.test_settings"]
CMD ["python3", "manage.py", "test"]
