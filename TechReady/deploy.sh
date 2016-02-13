tar -cvf web_node.tar.gz web_node/
tar -cvf vmss_node.tar.gz vmss_node/

git add .
git commit -m "autocommit"
git push origin master

echo "{" > template/web_node.parameters.json
echo  "\"$schema\": \"https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#\"," >> template/web_node.parameters.json
echo  "\"contentVersion\": \"1.0.0.0\"," >> template/web_node.parameters.json
echo  "\"parameters\": {" >> template/web_node.parameters.json
echo    "\"location\": {" >> template/web_node.parameters.json
echo      "\"value\": \"West US\"" >> template/web_node.parameters.json
echo    "}," >> template/web_node.parameters.json
echo    "\"username\": {" >> template/web_node.parameters.json
echo      "\"value\": \"ubuntu\"" >> template/web_node.parameters.json
echo    "}," >> template/web_node.parameters.json
echo    "\"password\": {" >> template/web_node.parameters.json
echo      "\"value\": \"azure\"" >> template/web_node.parameters.json
echo    "}," >> template/web_node.parameters.json
echo    "\"newStorageAccountName\": {" >> template/web_node.parameters.json
echo      "\"value\": \"$1\"" >> template/web_node.parameters.json
echo    "}," >> template/web_node.parameters.json
echo    "\"vmSize\": {" >> template/web_node.parameters.json
echo      "\"value\": \"Standard_D4\"" >> template/web_node.parameters.json
echo    "}," >> template/web_node.parameters.json
echo    "\"dnsNameForPublicIP\": {" >> template/web_node.parameters.json
echo      "\"value\": \"$1\"" >> template/web_node.parameters.json
echo    "}" >> template/web_node.parameters.json
echo  "}" >> template/web_node.parameters.json
echo "}" >> template/web_node.parameters.json


azure group create -n nsgtrrg -d nsgtrdep -l "West US" -f template/web_node.json -e template/web_node.parameters.json
