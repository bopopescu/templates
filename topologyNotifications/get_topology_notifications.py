import azurerm
import sys
import datetime
import json
import time

# P0 - get an access token from a user-generated service principal (shown below)
# P1 - instead of the below, get an access token from MSI (should just be a call to an internal IP)

tenantId = sys.argv[1]
applicationId = sys.argv[2]
applicationSecret = sys.argv[3]
scaleSetResourceId = sys.argv[4]
subscriptionId = scaleSetResourceId.split('/')[2]

access_token = azurerm.get_access_token(
    tenantId,
    applicationId,
    applicationSecret
)

startTimestamp = str(datetime.datetime.now())
while True:
    # do a GET on the activity log for the scale set
    endpoint = ''.join(['https://management.azure.com/subscriptions/', subscriptionId,
                        '/providers/microsoft.insights/eventtypes/management/values?api-version=2015-04-01&$filter=eventTimestamp ge \'',
                        startTimestamp, '\' and resourceUri eq \'', scaleSetResourceId, '\''])
    res = azurerm.do_get(endpoint, access_token)

    # react to events in the activity log; you may wish to sort them first (e.g. by timestamp), but we don't here
    for event in res["value"]:

        # ignore debug events
        if (event["channels"] == "Debug"):
            continue

        if (event["operationName"]["value"] == "Microsoft.Insights/AutoscaleSettings/Scaledown/Action"):
            # do things based on the autoscale scale down event
            print("TAKING ACTION ON AUTOSCALE SCALE DOWN!!!")
            

        if (event["operationName"]["value"] == "Microsoft.Compute/virtualMachineScaleSets/write"):
            # do things based on the scale set write event
            print("TAKING ACTION ON SCALE SET WRITE!!!")

        print(json.dumps(event, indent=2))
        print("")
        print("")
        print("")

    # update the startTimestamp to just after the most recent event so we only see new events in the next loop iteration
    datetime.datetime.strptime(startTimestamp[0:-2]'2017-05-16T18:27:22.6883207Z', '%Y-%m-%dT%H:%M:%S.%f')
        
    # wait before polling again
    time.sleep(60)
