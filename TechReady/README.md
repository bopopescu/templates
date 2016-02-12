Currently runs lots of things as root that really should be run as other users with properly-scoped priveleges.
Also uses publicly viewable password that is insecure.
Also runs flask server and nginx separately on different ports; should probably be working together on the same port