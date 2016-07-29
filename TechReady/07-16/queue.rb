require "azure"


Azure.config.sb_namespace = "nsgtrnamespace"
Azure.config.sb_access_key = "KbuVe06trwIaVPeYYg/F+WfmojIi+pdWe4SrD5BBczY="

message = Azure::ServiceBus::BrokeredMessage.new("test queue message")
message.correlation_id = "test-correlation-id"
azure_service_bus_service.send_queue_message("test-queue", message)

message = azure_service_bus_service.receive_queue_message("test-queue",
                                                          { :peek_lock => false })

print message
