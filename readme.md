 
 ## Tl;dr
 docker-compose up --buld
 
 ## manually the hard way
 docker network create test
 
 docker run --rm -it -p 1883:1883 -p 9001:9001 --name=broker --network=test eclipse-mosquitto
 
 cd producer
 docker build -t kicsikrumpli/prod .
 docker run --rm -it -e "BROKER_HOST=broker" -e "BROKER_PORT=1883" -e "TOPIC=hello" --network=test kicsikrumpli/prod
 
 cd consumer
 docker build -t kicsikrumpli/cons .
 docker run --rm -it -e "BROKER_HOST=broker" -e "BROKER_PORT=1883" -e "TOPIC=hello" --network=test kicsikrumpli/cons