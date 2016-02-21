FROM python:latest

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY latest_container_name.py .
CMD ["python3", "latest_container_name.py"]
