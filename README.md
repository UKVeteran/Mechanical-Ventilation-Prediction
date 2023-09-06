
## Docker Terminal codes
docker images | to list all images in the disk
docker rmi --force <image code> | to remove image from disk
docker run python:3.10.6-buster | to run container
docker run -it python:3.10.6-buster sh | to see inside of the container (it:interactive)
docker container ls (-a) | to list the files inside container (-a to see past)
docker build . -t mvp_api | build the new image and name it api
docker run -it mvp_api sh | run it in shell after you name it api
docker run mvp_api | to run it
docker run -p 2323:8000 mvp_api | map the 2389 port on your machine to the 8000 -
(uvicorn default) port inside container, p for port
docker ps | to list the running containers
docker stop <container ID>
docker kill <container ID> | use only is image refuses to stop
docker ps -q | xargs docker kill | to kills all
docker

## Inside docker shell codes after docker run -it mvp_api sh
ls -la | to list all files
cat requirements.txt | to see the contents
cat app/build_api.py | to see the .py file inside app folder
pip freeze | to bring the latest version of packages


## .env files how to ini
direnv allow .  | initialize environment
direnv reload . | reload everytime you make changes
make docker_build | shortcut of
echo $GCR_IMAGE | to print the variable

We may need pickle file to put the model inside
