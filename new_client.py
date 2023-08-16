import requests
import http.client
import urllib.request
import os
#import urllib3

#urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)
path = os. getcwd()
c_cert_file_path = path + '/cert/client.crt'
c_key_file_path = path + '/cert/client.key'
certServer =  path + '/cert/derms.crt'
#certServer =  path + '\cdta.crt'


#host_name = 'psupwrlabcdta.ddns.net'
host_name = 'psupwrlabderms.ddns.net'
host_port = 443
host_address = 'https://psupwrlabderms.ddns.net:443'
#host_address = 'https://psupwrlabcdta.ddns.net:443'
# -------------------------------------------

xml = """<?xml version = "1.0" encoding = "UTF-8"?>
<Order>
  <Id>78912</Id>
  <to>gsp</to>
  <from>client</from>
  <Customer>SPC</Customer>
  <message>Simple Test Message</message>
</Order>"""

headers = {'Content-Type': 'application/xml'}
# example1: post request
#cert = (c_cert_file_path, c_key_file_path)

r = requests.post(host_address, data=xml, verify=certServer, headers=headers, cert=(c_cert_file_path, c_key_file_path))
print(r.status_code)
print(r.text)



