tar -cvf web_node.tar.gz web_node/
tar -cvf vmss_node.tar.gz vmss_node/

git add .
git commit -m "autocommit"
git push origin master

echo "{" > templates/web_node.parameters.json
echo  "\"$schema\": \"https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#\"," >> templates/web_node.parameters.json
echo  "\"contentVersion\": \"1.0.0.0\"," >> templates/web_node.parameters.json
echo  "\"parameters\": {" >> templates/web_node.parameters.json
echo    "\"location\": {" >> templates/web_node.parameters.json
echo      "\"value\": \"West US\"" >> templates/web_node.parameters.json
echo    "}," >> templates/web_node.parameters.json
echo    "\"username\": {" >> templates/web_node.parameters.json
echo      "\"value\": \"ubuntu\"" >> templates/web_node.parameters.json
echo    "}," >> templates/web_node.parameters.json
echo    "\"password\": {" >> templates/web_node.parameters.json
echo      "\"value\": \"azure\"" >> templates/web_node.parameters.json
echo    "}," >> templates/web_node.parameters.json
echo    "\"newStorageAccountName\": {" >> templates/web_node.parameters.json
echo      "\"value\": \"$1\"" >> templates/web_node.parameters.json
echo    "}," >> templates/web_node.parameters.json
echo    "\"vmSize\": {" >> templates/web_node.parameters.json
echo      "\"value\": \"Standard_D4\"" >> templates/web_node.parameters.json
echo    "}," >> templates/web_node.parameters.json
echo    "\"dnsNameForPublicIP\": {" >> templates/web_node.parameters.json
echo      "\"value\": \"$1\"" >> templates/web_node.parameters.json
echo    "}" >> templates/web_node.parameters.json
echo  "}" >> templates/web_node.parameters.json
echo "}" >> templates/web_node.parameters.json


azure group create -n nsgtrrg -d nsgtrdep -l "West US" -f template/web_node.json -e template/web_node.parameters.json
