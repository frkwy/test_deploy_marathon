FROM python:latest

COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY deploy_marathon.py .
CMD ["python3", "deploy_marathon.py", "yusukefurukawa/test"]
