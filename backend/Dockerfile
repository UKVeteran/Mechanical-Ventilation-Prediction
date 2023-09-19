#each line of Docker file is shaping the image
FROM python:3.10.6-buster
#can use a base image which has tensorflow involved / pytorch
#launch a virtual machine, make set up, clone of repository, do docker actions there
# virtex ai notebook, log in to machine, work from there (gh repo clone, clone github)

COPY app /app
COPY requirements.txt /requirements.txt
COPY model/model_tanh.h5 model/model_tanh.h5
COPY mechvent/predict.py mechvent/predict.py
COPY demo_samples /demo_samples

RUN pip install --upgrade pip
# inside image upgrade the latest version of pip
RUN pip install -r requirements.txt
# list all the package name inside the file and install them inside the container image
# ENV PORT=8080
# EXPOSE $PORT
#in order to expose image to port that you want since make docker_build dont have port #
CMD uvicorn app.build_api:app --host 0.0.0.0 --port $PORT
# allow you to run command inside of image
# --host 0.0.0.0 this will let uvicorn inside docker fileto communicate with outside world
# this command starts uvicorn server 2nd app is the instance of the class api (FastAPI)
