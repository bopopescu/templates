set -e

# install azurerm library for easy demonstration of REST API
apt-get install -y unzip build-essential libssl-dev libffi-dev python-dev python-pip

wget https://github.com/gbowerman/azurerm/archive/master.zip
unzip master.zip
cd azurerm-master
python setup.py build
python setup.py install

# get_topology_notifications.py plays the role of the customer app that is monitoring notifications
# we pass in AAD tenant ID, application ID, and application secret to app so it can auth to activity log
# we also pass in the resource ID of the scale set to monitor
wget https://raw.githubusercontent.com/gatneil/templates/topologyNotifications/topologyNotifications/get_topology_notifications.py
python get_topology_notifications.py $1 $2 $3 $4
