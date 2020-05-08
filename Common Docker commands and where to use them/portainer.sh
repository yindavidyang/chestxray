docker run \
  --name portainer \
  -p 9000:9000 \
  -d \
  -v "/var/run/docker.sock:/var/run/docker.sock" \
  --restart always \
  portainer/portainer
