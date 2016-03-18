from subprocess import Popen, call
from test import *

call(["rm", "-f", "output/*"])

for linux_image in linux_images:
    for auth_type in AUTH_TYPES:
        cmd = ["/usr/local/lib/python2.7.9/bin/python", "/home/negat/repos/templates/vmssPortal/run_single.py", linux_image, auth_type, NAMING_INFIX + linux_image[0:2] + auth_type[0], 'l', '>', 'output/' + linux_image + auth_type + 'debug.txt']
        print(cmd)
        Popen(cmd)

for windows_image in windows_images:
    cmd = ["/usr/local/lib/python2.7.9/bin/python", "/home/negat/repos/templates/vmssPortal/run_single.py", windows_image, "password", NAMING_INFIX + "".join(windows_image.split("-")), 'w', '>', 'output/' + linux_image + auth_type + 'debug.txt']
    print(cmd)
    Popen(cmd)
