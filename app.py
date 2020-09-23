from flask import Flask, request, jsonify
from flask_sqlalchemy import flask_sqlalchemy
from flask_marshmallow import flask_marshmallow
import os

app = Flask(__name__)

if __name__ == '__main__':
  app.run(debug=True)
