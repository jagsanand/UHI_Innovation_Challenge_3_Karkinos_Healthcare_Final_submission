from flask import Flask

app = Flask("app")
app.secret_key = 'Karkinos'
from app import get_hip_response
