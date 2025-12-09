docker stop $(docker ps -aq)
docker rm -f nginx-lb

