apt update
apt install python3-pip
pip3 install -r requirements.txt
apt install default-jre
apt install openjdk-11-jre-headless
apt install openjdk-8-jre-headless
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.8.0-linux-x86_64.tar.gz
tar -xvzf elasticsearch-7.8.0-linux-x86_64.tar.gz
mv elasticsearch-7.8.0 ../MovieRama/
