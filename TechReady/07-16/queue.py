from azure.servicebus import ServiceBusService, Message, Queue

namespace = "nsgtrnamespace"
endpoint = "sb://" + namespace + ".servicebus.windows.net/"
keyName = "all"
key = "KbuVe06trwIaVPeYYg/F+WfmojIi+pdWe4SrD5BBczY="
queueName = "nsgtrqueue"

bus_service = ServiceBusService(
    service_namespace=namespace,
    shared_access_key_name=keyName,
    shared_access_key_value=key
)

sentMsg = Message(b'hi')
bus_service.send_queue_message(queueName, sentMsg)
receivedMsg = bus_service.receive_queue_message(queueName, peek_lock=False)
print(receivedMsg.body)

#print(bus_service.receive_queue_message(queueName, peek_lock=False))
