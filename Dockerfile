FROM python:3.8.10-slim-buster
WORKDIR /project
RUN cd /project
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "app.py"]