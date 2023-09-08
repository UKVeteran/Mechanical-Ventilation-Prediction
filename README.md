# Steps to follow to create an API and connect it to world

1. Use **FastAPI** to create an API for your model create a .py file
pip install fastapi
pip install uvicorn
uvicorn build_api:app --reload | python file and api name to browse rootpage
2. Run that API on your machine
create dockerfile (from,copy,run,cmd)
create docker image by docker_build
create container by docker_run
3. Put it in production (already in production via Makefile codes)
4. Push image to Container Registry (CR Docker hub like pushing it to github)


## Docker Terminal codes
docker images | to list all images in the disk
docker rmi --force <image code> | to remove image from disk
docker run python:3.10.6-buster | to run container
docker run -it python:3.10.6-buster sh | to see inside of the container (it:interactive)
docker container ls (-a) | to list the files inside container (-a to see past)
docker build . -t mvp_api | build the new image and name it api
make docker_build | shortcut of build
docker run -it mvp_api sh | run it in shell after you name it api
docker run mvp_api | to run it
docker run -p 2323:8000 mvp_api | map the 2389 port on your machine to the 8000 -(uvicorn default) port inside container, p for port
docker ps | to list the running containers
docker stop <container ID>
docker kill <container ID> | use only is image refuses to stop
docker ps -q | xargs docker kill | to kills all


## Inside docker shell codes after docker run -it mvp_api sh
ls -la | to list all files
cat requirements.txt | to see the contents
cat app/build_api.py | to see the .py file inside app folder
pip freeze | to bring the latest version of packages


## .env files how to initialize and reload
direnv allow .  | initialize environment
direnv reload . | reload everytime you make changes
echo $GCR_IMAGE | to print the variable


## authentication for docker in gcr
gcloud services enable containerregistry.googleapis.com
gcloud auth configure-docker


## how to check which libraries or tools you need in requirements
pip install pipreqs
pipreqs .  --force
