APP_DIR = "/home/ec2-user/csc346flaskdemo/cgi-bin"

# add the CGI directory to the python import path (so that we can import the
# application below
import sys
sys.path.insert(0, APP_DIR)

# chdir to the CGI directory so that when we open local config files,
# we'll also get the right files.
import os
os.chdir(APP_DIR)

# now import the application
from flask_demo import app as application
