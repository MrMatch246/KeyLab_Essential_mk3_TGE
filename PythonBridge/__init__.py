from __future__ import absolute_import, print_function, unicode_literals
import os
import subprocess

from .KeystrokeProxie import KeystrokeProxie
from ..Settings import PY_PORT
#from ..Log import log

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

def dispatch_hotkey(hotkey='CTRL+s'):
    KeystrokeProxie().send(hotkey)

def setup_requirements():
    proc=subprocess.run(['python3', '-m', 'pip', 'install','--user', '-r', FILE_PATH + '/requirements.txt'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    #log(proc.stdout)
    #log(proc.stderr)
    return

def start_server():
    subprocess.Popen(['python3', FILE_PATH + '/KeystrokeServer.py',str(PY_PORT)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)


