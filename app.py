from flask import Flask, abort, make_response, request, jsonify
from flask_restful import Resource, Api
import yaml
import logging
from logging.handlers import RotatingFileHandler

from src.vec_similarity import vec_search
from src.utils.logger import init_logging

app = Flask(__name__)
api = Api(app)
init_logging()

@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/ping')
def ping():
    return jsonify({ "code": "200", "message": "" })


@app.route('/search', methods=['POST', 'GET'])
def search():
    logging.info('search request json:{}'.format(request.json))
    return vec_search()


if __name__ == '__main__':
    conf = yaml.load('conf/config.yaml')
    app.run()