This is a demo of VM Scale Sets and autoscale. It sets up a MySQL database, an NGINX web front end, and an Ubuntu compute back end. Each compute node is given an image (Mona Lisa) and a set of 10,000 small images (cifar 10 group 1). It queries the database for a list of chunks of Mona Lisa. Once it knows which chunks to work on, it searches through the smaller images for good matches to those chunks. It replies to the database with the images that match well. There is a script running on the front end VM that queries the database for which images matched well and has NGINX display these images. The result is a Photo Mosaic of Mona Lisa made up of many smaller images.

TODO HOW TO USE THE DEMO

vmss_node.json is the main deployment file. If you don't modify anything, all you need to do is deploy this file to Azure (be sure to change the parameters in templates/vmss_node.parameters.json first, though; in particular, vmssName must be unique across all of Azure). You can do via portal, XPlat CLI, Powershell, etc. If you do modify something, you will need to use github to make a fork of this repo, make your modifications, push your changes to your fork, then deploy the vmss_node.json file in your fork. Be sure to change urls because as is they point to my repo. If you are on a *nix box, you can use the sh deploy.sh script to automate this somewhat. It takes in the vmssName as its first argument. If you change the username or password parameters, be aware that the demo is likely to fail if they contain special characters with meaning in bash.


TODO
Currently runs lots of things as root that really should be run as other users with properly-scoped priveleges.
Also uses publicly viewable password that is insecure.
Also runs flask server and nginx separately on different ports; should probably be working together on the same port
Fix sanitization so that usernames and passwords can contain special characters with meaning in bash.