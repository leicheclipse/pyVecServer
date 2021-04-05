import annoy 
import json 
import logging
from flask import Flask,abort, make_response, request, jsonify

logger = logging.getLogger('mainlogger')
def vec_search():
    logger.info('request json {}'.format(request.json))
    itemid = request.json["itemid"]
    logger.info('vec_search:{}'.format(itemid))
    res = {'code': 200, 'message': 'vec_serach:{}'.format(itemid)}
    return jsonify(res)