# import redis
from lib.utilities.ConfigurationReader import *
from lib.Controller import *

import threading
import time

import os
from flask import Flask, send_from_directory, jsonify, request

app = Flask(__name__, static_url_path='', static_folder='')
controller = Controller()

webClientDir = 'web'
def clientDir(relPath):
    return webClientDir + "/" + relPath

@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory(clientDir('images'), path)

@app.route('/assets/<path:path>')
def send_assets(path):
    return send_from_directory(clientDir('assets'), path)

@app.route('/styles.css')
def send_css():
    return app.send_static_file(clientDir('styles.css'))

@app.route('/map.html')
def send_map():
    return app.send_static_file(clientDir('originSelector.html'))

@app.route('/navigate.html')
def send_mapreview():
    return app.send_static_file(clientDir('navigate.html'))

@app.route('/')
def send_index():
    return app.send_static_file(clientDir('index.html'))

@app.route('/setDestination', methods=["POST"])
def api_setDestination():
    data = request.form
    return jsonify(controller.setDestination(data))

@app.route('/finalizeTravel', methods=["POST"])
def api_finalizeTravel():
    data = request.form
    return jsonify(controller.finalizeTravel(data))

@app.route('/getNav', methods=["POST"])
def api_getNav():
    data = request.form
    print("getNav", data)
    return jsonify(controller.getNav(data))


@app.route('/setOrigin', methods=["POST"])
def api_setOrigin():
    data = request.json
    controller.setOrigin(data)
    return jsonify(True)




if __name__ == '__main__':
    config = GetConfiguration()
    app.run(debug=config["flaskdebug"], host=config["flaskhost"], \
        port=config["flaskport"])
