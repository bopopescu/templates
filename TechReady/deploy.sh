rm -f web_node.tar.gz
rm -f vmss_node.tar.gz

tar -cvf web_node.tar.gz web_node/
tar -cvf vmss_node.tar.gz vmss_node/

git add .
git commit -m "autocommit"
git push origin master

echo "{" > template/vmss_node.parameters.json
echo "  \"$schema\": \"http://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#\"," >> template/vmss_node.parameters.json
echo "  \"contentVersion\": \"1.0.0.0\"," >> template/vmss_node.parameters.json
echo "  \"parameters\": {" >> template/vmss_node.parameters.json
echo "    \"resourceLocation\": {" >> template/vmss_node.parameters.json
echo "      \"value\": \"West US\"" >> template/vmss_node.parameters.json
echo "    }," >> template/vmss_node.parameters.json
echo "    \"vmSku\": {" >> template/vmss_node.parameters.json
echo "      \"value\": \"Standard_A1\"" >> template/vmss_node.parameters.json
echo "    }," >> template/vmss_node.parameters.json
echo "    \"vmssName\": {" >> template/vmss_node.parameters.json
echo "      \"value\": \"$1\"" >> template/vmss_node.parameters.json
echo "    }," >> template/vmss_node.parameters.json
echo "    \"instanceCount\": {" >> template/vmss_node.parameters.json
echo "      \"value\": 1" >> template/vmss_node.parameters.json
echo "    }," >> template/vmss_node.parameters.json
echo "    \"adminUsername\": {" >> template/vmss_node.parameters.json
echo "      \"value\": \"ubuntu\"" >> template/vmss_node.parameters.json
echo "    }," >> template/vmss_node.parameters.json
echo "    \"adminPassword\": {" >> template/vmss_node.parameters.json
echo "      \"value\": \"Passw0rd\"" >> template/vmss_node.parameters.json
echo "    }" >> template/vmss_node.parameters.json
echo "  }" >> template/vmss_node.parameters.json
echo "}" >> template/vmss_node.parameters.json

azure group create -n $1rg -d $1dep -l "West US" -f template/vmss_node.json -e template/vmss_node.parameters.json


#echo "{" > template/web_node.parameters.json
#echo  "\"$schema\": \"https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#\"," >> template/web_node.parameters.json
#echo  "\"contentVersion\": \"1.0.0.0\"," >> template/web_node.parameters.json
#echo  "\"parameters\": {" >> template/web_node.parameters.json
#echo    "\"location\": {" >> template/web_node.parameters.json
#echo      "\"value\": \"West US\"" >> template/web_node.parameters.json
#echo    "}," >> template/web_node.parameters.json
#echo    "\"username\": {" >> template/web_node.parameters.json
#echo      "\"value\": \"ubuntu\"" >> template/web_node.parameters.json
#echo    "}," >> template/web_node.parameters.json
#echo    "\"password\": {" >> template/web_node.parameters.json
#echo      "\"value\": \"Passw0rd\"" >> template/web_node.parameters.json
#echo    "}," >> template/web_node.parameters.json
#echo    "\"newStorageAccountName\": {" >> template/web_node.parameters.json
#echo      "\"value\": \"$1\"" >> template/web_node.parameters.json
#echo    "}," >> template/web_node.parameters.json
#echo    "\"vmSize\": {" >> template/web_node.parameters.json
#echo      "\"value\": \"Standard_D4\"" >> template/web_node.parameters.json
#echo    "}," >> template/web_node.parameters.json
#echo    "\"dnsNameForPublicIP\": {" >> template/web_node.parameters.json
#echo      "\"value\": \"$1\"" >> template/web_node.parameters.json
#echo    "}" >> template/web_node.parameters.json
#echo  "}" >> template/web_node.parameters.json
#echo "}" >> template/web_node.parameters.json


#azure group create -n $1rg -d $1dep -l "West US" -f template/web_node.json -e template/web_node.parameters.json
