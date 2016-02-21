FROM python:latest
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY latest_container_name.py .
COPY notice_container_name_to_slack.py .
CMD ["python3", "notice_container_name_to_slack.py"]
