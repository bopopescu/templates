import azurerm
import sys
import datetime


# P0 - get an access token from a user-generated service principal (shown below)
# P1 - instead of the below, get an access token from MSI (should just be a call to an internal IP)

tenantId = sys.argv[1]
applicationId = sys.argv[2]
applicationSecret = sys.argv[3]
scaleSetResourceId = sys.argv[4]
subscriptionId = scaleSetResourceId.split('/')[1]

access_token = azurerm.get_access_token(
    tenantId,
    applicationId,
    applicationSecret
)


startTimestamp = str(datetime.datetime.now() - datetime.timedelta(days=1))

endpoint = ''.join(['https://management.azure.com/subscriptions/', subscriptionId,
                    '/providers/microsoft.insights/eventtypes/management/values?api-version=2015-04-01&$filter=eventTimestamp ge \'',
                    startTimestamp, '\''])
res = azurerm.do_get(endpoint, access_token)

print(res)
print(res.text)
