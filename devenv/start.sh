#!/bin/bash 

docker compose -p video-download up -d 

# echo to ../.env
cat > ../.env << EOF
BROKER=amqp://admin:admin@localhost:5672
BACKEND=mongodb://root:1111@localhost:27017
EOF