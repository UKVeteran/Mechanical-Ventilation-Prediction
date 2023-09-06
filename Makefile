
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

docker_deploy:
	gcloud run deploy --image ${GCR_REGION}/${GCP_PROJECT}/${GCR_IMAGE}:prod --memory ${GCR_MEMORY} --region ${GCP_REGION} --env-vars-file .env.ta.yaml
# after deploying url will be available for external use
