set -vx # show commands for debugging

# pass credentials from template to scripts
echo "" > credentials.py
echo "username = '$1'" >> credentials.py
echo "password = '$2'" >> credentials.py
echo "hostname = 'localhost'" >> credentials.py

# set selections for when mysql asks for a root password
#echo 'mysql-server mysql-server/root_password password $2' | debconf-set-selections
#echo 'mysql-server mysql-server/root_password_again password $2' | debconf-set-selections 

# install necessary components from apt
apt-get -y update
DEBIAN_FRONTEND=noninteractive apt-get install -y nginx mysql-server

# install necessary components from source
cd mysql-connector-python-2.1.3
python setup.py install
cd ..

# make /var/lib waagent world readable/executable so that nginx can serve it without 403
sudo chmod 705 /var/lib/waagent/

# set up nginx for serving static files
cp nginx.conf /etc/nginx
service nginx restart

# set password
mysqladmin --user=root password $2

# mysql listens only on localhost by default;
# want it to be public and allow root access from anywhere,
# so we restart with bind-address 0.0.0.0 and
# grant root access to all ip's and
service mysql stop
mysqld --bind-address=0.0.0.0 &
sleep 5
mysql --host=localhost --user=root --password=$2 -e "\"GRANT ALL ON *.* TO 'root'@'%' IDENTIFIED BY '$2';\""

# initialize db for parseling out work
python create_db.py

# continuously poll the db for finished work
# put such work in the right place for nginx to serve
python gen_substitutes_from_db.py > genOut.txt 2> genErr.txt &
