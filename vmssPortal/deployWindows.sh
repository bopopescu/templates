set -exv

echo "{" > azuredeploy.parameters.json
echo "  \"$schema\": \"http://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#\"," >> azuredeploy.parameters.json
echo "  \"contentVersion\": \"1.0.0.0\"," >> azuredeploy.parameters.json
echo "  \"parameters\": {" >> azuredeploy.parameters.json
echo "    \"WindowsServerVersion\": {" >> azuredeploy.parameters.json
echo "      \"value\": \"$2\"" >> azuredeploy.parameters.json
echo "    }," >> azuredeploy.parameters.json
echo "    \"vmssName\": {" >> azuredeploy.parameters.json
echo "      \"value\": \"$1\"" >> azuredeploy.parameters.json
echo "    }," >> azuredeploy.parameters.json
echo "    \"instanceCount\": {" >> azuredeploy.parameters.json
echo "      \"value\": 2" >> azuredeploy.parameters.json
echo "    }," >> azuredeploy.parameters.json
echo "    \"adminUsername\": {" >> azuredeploy.parameters.json
echo "      \"value\": \"negat\"" >> azuredeploy.parameters.json
echo "    }," >> azuredeploy.parameters.json
echo "    \"adminPassword\": {" >> azuredeploy.parameters.json
echo "      \"value\": \"P4ssw0rd\"" >> azuredeploy.parameters.json
echo "    }" >> azuredeploy.parameters.json
echo "  }" >> azuredeploy.parameters.json
echo "}" >> azuredeploy.parameters.json


azure group create -n $1rg -d $1dep -l "West US" -f $3 -e azuredeploy.parameters.json
rm -f azuredeploy.parameters.json
