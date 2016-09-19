import azurerm
import pprint
import sys
sys.path.insert(0, '/home/negat/credentials/aad/')

from aadcredentials import *

pp = pprint.PrettyPrinter(indent=2)

access_token = azurerm.get_access_token(
    tenant_id,
    application_id,
    application_secret
)

metrics = azurerm.get_metrics_for_resource(access_token, subscription_id, 'nsghostmetrics', 'Microsoft.Compute', 'virtualMachineScaleSets', 'nsghostme')['value'][0]

real_data = []
for datum in metrics['data']:
        if 'average' in datum:
                real_data.append(datum)

pp.pprint(real_data)

