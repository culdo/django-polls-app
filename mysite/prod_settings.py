from mysite.settings import *

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = ["dj-polls-app.herokuapp.com"]
