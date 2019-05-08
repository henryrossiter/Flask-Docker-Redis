FROM python:3-onbuild
RUN apt-get update
RUN apt-get install -y redis-tools
RUN pip install -r requirements.txt
EXPOSE 5005
CMD ["python", "./main.py"]
