# pass credentials from template to scripts
echo "" > credentials.py
echo "username = '$1'" >> credentials.py
echo "password = '$2'" >> credentials.py
echo "hostname = '$3'" >> credentials.py

# install necessary components from source
cd pypng-master
python setup.py install
cd ..

cd mysql-connector-python-2.1.3
python setup.py install
cd ..

# install necessary components from apt
# can have temporary issues, so wrapped in an infinite loop
while true
do
    apt-get -y update && apt-get install -y python-numpy && break
    sleep 15
done

# start worker
python do_work.py > stdout.txt 2> stderr.txt &
