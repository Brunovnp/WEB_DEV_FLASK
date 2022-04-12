from flask import Flask
import webview

app = Flask(__name__)


from app import views
from app import calculator 

