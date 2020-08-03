'''
Pendant Automation
Contact:(410) 939-7707

@author: Jeremy Scheuerman

@version: 1.0

Created:7/29/20

Last Updated:7/29/20

Changes:N/A

'''
'''
# Imports

import subprocess;

# Deployment Variables
deploy_url = "https://www.pendantautomation.com/";

while True:
    v = subprocess.Popen("chromium-browser --fast --fast-start  --app=" + deploy_url, shell=True);
    # open up browser in kiosk mode
    v.wait();
    # wait for program to close then reopen
