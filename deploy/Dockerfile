FROM python:latest
RUN pip3 install --upgrade pip
RUN pip3 install --use-wheel --find-links=wheel Django request marathon
COPY deploy_marathon.py .
CMD ["python3", "deploy_marathon.py", "yusukefurukawa/test"]
