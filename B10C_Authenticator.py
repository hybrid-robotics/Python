#!/usr/bin/env python
import requests
import json

class B10C_Authenticator:
	urlbase = "https://api.10centuries.org/auth/login"
	app_id = "YOUR APP ID"

	def __init__ (self, username, userpass):
		acct_data = {
			"client_guid" :  self.app_id,
			"acctname" :  username,
			"acctpass" :  userpass
		}

		result = requests.post(self.urlbase, data=acct_data)

		print ("library: result = '{0}'".format(result))
		print ("library: result.text = '{0}'".format(result.text))

		#self.result = result.text
		self.result = json.loads(result.text)

		return None
