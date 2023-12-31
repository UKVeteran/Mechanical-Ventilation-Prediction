
docker_build:
	docker build -t ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:prod .

docker_run:
	docker run -e PORT=8000 -p 8000:8000 --env-file .env ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:prod

docker_interactive:
	docker run -it --env-file .env ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:prod /bin/bash

#only the final version
docker_push:
	docker push ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:prod
#by pushing you are instantiating the image into a running container
# make sure you dont have any container running locally, docker ps

docker_deploy:
	gcloud run deploy --image ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:prod --memory ${GCR_MEMORY} --region ${GCP_REGION}
#--env-vars-file .env.yaml
# after deploying url will be available for external use
# -- means options rest is the name of the image, can also be 1 dash only
