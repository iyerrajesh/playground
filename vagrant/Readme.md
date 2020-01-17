Install vagrant
---------------
Install virtual box 6.0 for Mac (later versions don’t work)
Change Settings->user & privacy settings to allow install to complete.

Using vagrant file, 
$vagrant up

After vagrant up, do this for docker,
sudo usermod -aG docker $USER
Logout & ssh again


Running ES.mongo and postgres
-----------------------------
docker run --name es -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:5.5.1

docker run -p 27017:27017 --name mongodb -v ~/data/db:/data/db -d mongo

docker run --rm --name pg -e POSTGRES_PASSWORD=docker -e 
POSTGRES_USER=nakuldesai -d -p 5432:5432 -v /home/nakuldesai/pg_data:/var/lib/postgresql/data postgres

Tomcat example
--------------
git clone https://github.com/softwareyoga/docker-tomcat-tutorial.git
 cd docker-tomcat-tutorial/
docker build -t mywebapp .
