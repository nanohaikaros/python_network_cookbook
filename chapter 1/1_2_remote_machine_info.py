#!/usr/bin/env python
# Python Network Programming Cookbook -- Chapter -1
# This program is optimized for Python 2.7. It may run on any
# It may run on any other version with/without modification

import socket

def get_remote_machine_info():
    remote_host = 'www.python.org'
    try:
        print "IP address: %s" % socket.gethostbyname(remote_host)
    except socket.error as err_msg:
        print "%s: %s" % (remote_host, err_msg)

if __name__ == '__main__':
        get_remote_machine_info()