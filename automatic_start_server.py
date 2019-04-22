import subprocess
import time
while True:
	status = subprocess.call("netstat -a | grep *:8070" , shell=True)
	if status== 1:
		print 'not running'
		print 'starting'
		subprocess.Popen("./odoo-bin", cwd="/home/sumit/Downloads/odoo-10.0/")

	else:
		print 'running'
	time.sleep(10)
