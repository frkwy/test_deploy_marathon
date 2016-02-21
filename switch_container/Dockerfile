FROM python:latest
RUN pip3 install --upgrade pip
RUN pip3 install wheel 
RUN pip3 install wheel --use-wheel --find-links=wheel marathon slackclient requests
COPY latest_container_name.py .
COPY notice_container_name_to_slack.py .
CMD ["python3", "notice_container_name_to_slack.py"]
