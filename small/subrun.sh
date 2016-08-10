#!/bin/bash

#set -e

vhdName=nsg$1.vhd
namingBase=nsg$1$2
vhdPath=~/data/$vhdName
tmpFile=tmp/tmp$namingBase

echo '{' > $tmpFile
echo '  "$schema": "http://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#",' >> $tmpFile
echo '  "contentVersion": "1.0.0.0",' >> $tmpFile
echo '  "parameters": {' >> $tmpFile
echo '    "vmSku": {' >> $tmpFile
echo '      "value": "Standard_A1"' >> $tmpFile
echo '    },' >> $tmpFile
echo '    "vmssName": {' >> $tmpFile
echo "      \"value\": \"$namingBase\"" >> $tmpFile
echo '    },' >> $tmpFile
echo '    "instanceCount": {' >> $tmpFile
echo '      "value": 20' >> $tmpFile
echo '    },' >> $tmpFile
echo '    "adminUsername": {' >> $tmpFile
echo "      \"value\": \"$namingBase\"" >> $tmpFile
echo '    },' >> $tmpFile
echo '    "vhdUri": {' >> $tmpFile
echo "      \"value\": \"https://$namingBase.blob.core.windows.net/$namingBase/$vhdName\"" >> $tmpFile
echo '    },' >> $tmpFile
echo '    "adminPassword": {' >> $tmpFile
echo '      "value": "P4$$w0rd"' >> $tmpFile
echo '    }' >> $tmpFile
echo '  }' >> $tmpFile
echo '}' >> $tmpFile

azure group create -n $namingBase -l $3
azure storage account create --sku-name LRS --kind Storage --location $3 -g $namingBase $namingBase
rawKey=$(azure storage account keys list $namingBase -g $namingBase --json | jq '.[0].value')
key=${rawKey//"\""/}
azure storage container create -a $namingBase --container $namingBase -k $key -p Off
blobxfer --no-progressbar --numworkers 1 --upload --pageblob --remoteresource $vhdName --storageaccountkey $key $namingBase $namingBase $vhdPath

/usr/bin/time  -f "%e" azure group deployment create -g $namingBase -n nsgsmall -f azuredeploy.json -e $tmpFile

# sometimes get ECONNRESET, so try 3 times
for i in `seq 1 3`
do
    azure group delete $namingBase -q
    sleep 5
done
