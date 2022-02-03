import pywhatkit
from pywhatkit.remotekit import start_server
from flask import Flask, request
pywhatkit.sendwhatmsg('+91 93267 68185', 'Good Morning', 11, 11)
 # 16, 20 is the timing at which you want to send the msg