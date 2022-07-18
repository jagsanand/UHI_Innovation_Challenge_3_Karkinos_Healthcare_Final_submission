from flask import Flask,render_template, request, Markup,url_for
app = Flask("app")

app.secret_key = 'fooBarBaz'
from app import consultation
