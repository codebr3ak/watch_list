from flask import Flask
from .config import DevConfig 

# Initializin application 
app = Flask(__name__)

#Setting up configurations
app.config.from_object(DevConfig)

from app import views 
