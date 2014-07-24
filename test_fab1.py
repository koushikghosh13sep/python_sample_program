from __future__ import with_statement
import sys
from fabric.api import env,run,hide,settings

env.host_string = 'root@127.0.0.1'

def exec_remote_cmd(cmd):
	with hide('output','running','warnings'), settings(warn_only=True):
		return run(cmd)

def main(cmd_list):
#	cmd_list = ['ls', 'lss','whoami']
	for cmd in cmd_list:
		result = exec_remote_cmd(cmd)
		if result.succeeded:
			sys.stdout.write('\n* Command succeeded: '+cmd+'\n')
			sys.stdout.write(result+"\n")
		else:
			sys.stdout.write('\n* Command failed: '+cmd+'\n')
			sys.stdout.write(result+"\n")

if __name__ == '__main__':
#	for arg in sys.argv:
	print sys.argv[1]
	main(sys.argv[1:])

