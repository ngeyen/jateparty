#!/bin/bash

# Define variables
DOCKER_IMAGE_NAME="jateparty_image"
DOCKER_CONTAINER_NAME="jateparty_container"
PORT=8000

# Build the Docker image using buildx
# Build the Docker image
docker build -t $DOCKER_IMAGE_NAME -f Dockerfile .

# Run the Docker container
docker run -d --name $DOCKER_CONTAINER_NAME -p $PORT:8000 $DOCKER_IMAGE_NAME

# Wait for a moment to ensure the container is up and running
sleep 5

# Perform database migrations and collect static files
docker exec -it $DOCKER_CONTAINER_NAME python manage.py migrate
docker exec -it $DOCKER_CONTAINER_NAME python manage.py collectstatic --noinput

# Display deployment information
echo "Deployment completed successfully!"
echo "Django application is running on http://localhost:$PORT/"
echo "Container ID: $DOCKER_CONTAINER_NAME"
