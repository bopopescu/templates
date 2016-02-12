tar -cvf web_node.tar.gz web_node/
tar -cvf vmss_node.tar.gz vmss_node/

git add .
git commit -m "autocommit"
git push origin master

azure group create -n nsgtrrg -d nsgtrdep -l "West US" -f template/web_node.json -e template/web_node.parameters.json
