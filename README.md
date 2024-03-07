# Cassandra_TP

1-Clone the Repository :

git clone https://github.com/Laaliji/Cassandra_TP
cd Cassandra_TP

2-Pull the Cassandra Docker Image :

docker-compose pull

3-Generate Tokens :

python tokens.py

4-Run Docker Containers :

docker-compose up -d

5-Access Bash Shell of First Node :

docker-compose exec c1 /bin/bash

6-Connect to Cassandra Cluster using cqlsh :

cqlsh c1



