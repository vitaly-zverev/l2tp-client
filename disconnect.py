#!/usr/bin/env python3
import sys
import os
def sh(script):
    os.system("bash -c '%s'" % script)

def run_script(script, stdin=None):
    """Returns (stdout, stderr), raises error on non-zero return code"""
    import subprocess
    # Note: by using a list here (['bash', ...]) you avoid quoting issues, as the
    # arguments are passed in exactly this order (spaces, quotes, and newlines won't
    # cause problems):
    proc = subprocess.Popen(['bash', '-c', script],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        stdin=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode('utf-8', 'ignore')

    if proc.returncode:
        raise ScriptException(proc.returncode, stdout, stderr, script)
    return stdout, stderr

class ScriptException(Exception):
    def __init__(self, returncode, stdout, stderr, script):
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr
        Exception.__init__('Error in script')

import time

def checkRunning():
    try:
        strongswan, err = run_script("service strongswan-starter status | grep Active")
        xl2tpd, err = run_script("service xl2tpd status | grep Active")
    except:
        return False
    if "running" in strongswan and "running" in xl2tpd:
        return  True
    return False

def diconnect():
		if  checkRunning():
			print("stopping service...")
			sh("service xl2tpd stop")

			time.sleep(0.5)
			print("ipsec down......")
			try:	stdout, stderror = run_script(r"ipsec down XXX-YOUR-CONNECTION-NAME-XXX")
			except:	pass
		else:
			print("nothing to stop. connect first, please...")
diconnect()
print("finished")
