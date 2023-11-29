#!/usr/bin/env python
import requests

logouturl = "https://api.10centuries.org/auth/logout"

from B10C_Authenticator import B10C_Authenticator

u_name = "YOUR EMAIL ADDRESS"
u_pass = "YOUR PASSWORD"

code = 0
error = ""
token = ""

# Authenticate the user account with 10Centuries
b10c = B10C_Authenticator(u_name, u_pass)

result = b10c.result
print ("application: result = '{0}'".format(result))

data = result["data"]
#print ("application: data = '{0}'".format(data))

meta = result["meta"]
#print ("application: meta = '{0}'".format(meta))

code = meta["code"]
#print ("application: code = {0}".format(code))

if code == 200:
	token = data["token"]
	print ("Login was successful: token = '{0}'".format(token))
else:
	print ("Login failed - error = {0}".format(meta["error"]))

print ("application: Logging out")
result = requests.post(logouturl, data="")
