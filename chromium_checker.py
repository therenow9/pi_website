'''
Pendant Automation
Contact:(410) 939-7707

@author: Jeremy Scheuerman

@version: 0.5

Created:7/29/20

Last Updated:7/29/20

Changes:N/A

#notes my bash method didnt work as expected so im using a combination of another application and python
'''
import os, sys;

import webbrowser;

import subprocess;
import psutil;


# from selenium import webddriver;
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


deploy_url = "https://www.pendantautomation.com/";
# url to go into chromium
y = 1;
if y == 1:
    subprocess.Popen(['/usr/share/applications/firefox.desktop']);
    # need to get sudo priveledges within this script
    y = 2;
# open chromium

# while running==False;

