from .base import *
import os
from dotenv import load_dotenv
load_dotenv()
DEBUG = False

SECRET_KEY = str(os.getenv('SECRET_KEY'))
try:
    from .local import *
except ImportError:
    pass
