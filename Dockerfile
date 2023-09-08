#each line of Docker file is shaping the image
FROM python:3.10.6-buster

COPY app /app
COPY requirements.txt /requirements.txt
# COPY model.model_name /model.joblib
# COPY project /project

RUN pip install --upgrade pip
# inside image upgrade the latest version of pip
RUN pip install -r requirements.txt
# list all the package name inside the file and install them inside the container image

CMD uvicorn app.build_api:app --host 0.0.0.0 --port $PORT
# allow you to run command inside of image
# --host 0.0.0.0 this will let uvicorn inside docker fileto communicate with outside world
# this command starts uvicorn server 2nd app is the instance of the class api (FastAPI)