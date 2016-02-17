sleep 30s
wget https://github.com/gatneil/templates/raw/master/TechReady/web_node.tar.gz
tar -xvf web_node.tar.gz
cd web_node
sh initialize.sh root $1
