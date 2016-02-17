SUMMARY
=======

This is a demo of VM Scale Sets and autoscale. It sets up a MySQL database, an NGINX web front end, and an Ubuntu compute back end. The compute back end starts with a single VM but scales up to roughly 15 VMs once the first one starts doing work (the autoscale rules are based on CPU). Each compute node is given an image (Mona Lisa) and a set of 10,000 small images (cifar 10 group 1). It queries the database for a list of chunks of Mona Lisa. Once it knows which chunks to work on, it searches through the smaller images for good matches to those chunks. It replies to the database with the images that match well. There is a script running on the front end VM that queries the database for which images matched well and has NGINX display these images. The result is a photo mosaic of Mona Lisa made up of many smaller images.

IMPORTANT NOTE: This demo is fundamentally insecure. It does not follow security best practices (look through the TODOs for a non-exhaustive list of ways it is insecure). Please don't put any sensitive information on VMs and VMSSes created through this demo, and please delete the resource group for this demo once you are done using it.

SUPER EASY DEPLOY
=================
Click on the following link. It will take you to the Azure portal. Fill in your desired parameters (make sure the vmssName is globally unique and less than 9 characters in length), and hit "ok". From here on in this README, the vmssName you provide as a parameter is referred to as globally_unique_string_less_than_9_chars. Anywhere below we refer to 'ubuntu' as a username, replace that with the username you specify here as a paramters. However, root will still be the username for mysql. Also, anywhere below that refers to 'Passw0rd', replace with the password you specify here.

https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fgatneil%2Ftemplates%2Fmaster%2FTechReady%2Ftemplate%2Fvmss_node.json

EASY DEPLOY
===========
```sh deploy.sh {globally_unique_string_less_than_9_chars}```

NOTE: only works on *nix. Relies on tar, git, and azure XPlatCLI. Assumes you are running from within the git repo in the root folder.


WHERE TO LOOK FOR RESULTS
=========================
Let web_url_base := http://web{globally_unique_string_less_than_9_chars}.westus.cloudapp.azure.com.

To see Mona Lisa, open {web_url_base}:8080/cat.html in your browser.

To see the photo mosaic of Mona Lisa, open {web_url_base}:8080/cat_substitute.html

At first, you should see the first row or two being filled in by the first VM that starts working. Once autoscale kicks in, you should see alternating rows start to be filled in. This is because each VM takes on 2 rows of work at a time.


WHAT TO EXPECT
==============

While still being constructed, the Mona Lisa Photo Mosaic should look something like the following:

![alt text](https://raw.githubusercontent.com/gatneil/templates/master/TechReady/images/MidwayMona.png "image can't load")


DEBUGGING
=========
A resource group named {globally_unique_string_less_than_9_chars}rg is created in your subscription when you deploy this template. Inside, you will find public ip addresses named customscriptLinuxPublicIp and {globally_unique_string_less_than_9_chars}pip. The first is the public IP for the VM running the web front end and database. The second is the public IP for the LB fronting the VMSS. The VMs all use username 'ubuntu', and the database uses user 'root'. Both have the password 'Passw0rd'. You can ssh directly into the web/db VM, but to connect to a VM in the VMSS you need to pas through the LB via its NAT rules. To connect to VM i in the VMSS (i starting at 0), use:

ssh -p {50000+i}ubuntu@{public ip associated with the VMSS}

and use password 'Passw0rd'.

The relevant files for custom script extensions end up under /var/lib/waagent/Microsoft.CustomScriptExtensions.*/downloads/0. You might need to change the permissions on the waagent directory to navigate here (for security reasons, this is not recommended for long-running VMs).

 


DEPLOYMENT DETAILS
==================
vmss_node.json is the main deployment file. If you don't modify anything, all you need to do is deploy this file to Azure (be sure to change the parameters in templates/vmss_node.parameters.json first, though; in particular, vmssName must be unique across all of Azure). You can do via portal, XPlat CLI, Powershell, etc. If you do modify something, you will need to use github to make a fork of this repo, make your modifications, push your changes to your fork, then deploy the vmss_node.json file in your fork. Be sure to change urls because as is they point to my repo. If you are on a *nix box, you can use the sh deploy.sh script to automate this somewhat. It takes in the vmssName as its first argument. If you change the username or password parameters, be aware that the demo is likely to fail if they contain special characters with meaning in bash.




TODO
====
Currently runs lots of things as root that really should be run as other users with properly-scoped priveleges. Should also not have nginx serve static files from the waagent directory, because doing so involves opening up permissions on the waagent directory.
Also uses publicly viewable password that is insecure.
Fix sanitization so that usernames and passwords can contain special characters with meaning in bash.