#!/usr/bin/env python3
from ftplib import FTP
from io import BytesIO

server_ip = input('What is the IP address of the Wii U? ')

blank_digest = (b'F' * 0x40) + (b'\0' * 0x10)
digest_path = '/storage_slc/security/digest.bin'


print('Attempting to connect to {0}:21...'.format(server_ip))
with FTP(server_ip) as f:
    resp = f.login()
    print('Server response:', resp)
    print('Overwriting {0}...'.format(digest_path))
    resp = f.storbinary('STOR ' + digest_path, BytesIO(blank_digest))
    print('Server response:', resp)

print('Done.')
