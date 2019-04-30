FROM python:3-onbuild
RUN apt-get update
RUN apt-get install -y redis-tools
EXPOSE 5000
CMD ["python", "./main.py"]
