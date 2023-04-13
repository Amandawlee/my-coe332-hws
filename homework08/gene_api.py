from flask import Flask, request, send_file
import os
import json
import requests
import redis
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)

redis_ip = os.getenv('REDIS_IP')
if not redis_ip:
    raise Exception()

rd = redis.StrictRedis(host = redis_ip, port = 6379, db = 0, decode_responses = True)
rd2 = redis.StrcitRedis(host = redis_ip, port = 6379, db = 1)

@app.route('/data', methods = ['POST','GET','DELETE'])
def data():
    """
    Manipulates HGNC data with a given method

    Methods:
        "POST":     Loads data into Redis database
        "GET":      Returns data from Redis database
        "DELETE":   Deletes data in Redis database

    Args:
        No arguments

    Returns:
        "POST":     Returns string confirming data posted to Redis database
        "GET":      Returns data from Redis database
        "DELETE":   Returns string confirming data deletion
    """
    if request.method == 'POST':
        response = requests.get(url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        data = response.json()

        for item in data['response']['docs']:
            rd.set(item.get('hgnc_id'), json.dumps(item))
        return("HGNC data has been loaded to a Redis database.\n")
    elif request.method == 'GET':
        gene_data = []
        for key in rd.keys():
            gene_data.append(json.loads(rd.get(key)))
        return(gene_data)
    elif request.method == 'DELETE':
        rd.flushdb()
        return("HGNC data has ben deleted from Redis database.\n")
    else:
        return("The method you tried does not work.\n")

@app.route('/genes', methods = ['GET'])
def get_hgnc_ids():
    """
    Returns a json-formatted list of all HGNC_ID fields

    Args:
        No arguments

    Returns:
        hgnc_ids_list: A list of HGNC IDs from HGNC data set
    """
    hgnc_ids_list = []
    for key in rd.keys():
        hgnc_ids_list.append(key)
    return(hgnc_ids_list)

@app.route('/genes/<hgnc_id>', methods = ['GET'])
def get_hgnc_id_data(hgnc_id):
    """
    Returns all data associated with a given HGNC ID

    Args:
        hgnc_id: HGNC id used to query through data set

    Returns: 
        All data assocaited with given hgnce_id
    """
    if len(rd.keys()) == 0:
        return("The database is currently empty.\n")

    for key in rd.keys():
        if str(key) == str(hgnc_id):
            return(json.loads(rd.get(key)))
    
    return("The given HGNC ID does not match any IDs in the database.\n")

@app.route('/image', methods = ['POST','GET','DELETE'])
def image() -> bytes:
    """
    Args:
        No arguments

    Returns:
        gene_image: Bytes object of the image for the dataset
    """
    if request.method == 'POST':
        if len(rd.keys()) == 0:
            return("HGNC data has been loaded to a Redis database.\n")
        else:
            
    elif request.method == 'GET':
        if b'image' not in rd2.keys():
            return("Image can not be found or has not been loaded.\n")
        else:
            path = './data/getimage.png'
            with open(path, 'wb') as f:
                f.write(rd2.get('image'))
            return send_file(path, mimetype = 'image/png', as_attachment = True)
    elif request.method == 'DELETE':
        if b'image' not in rd2.keys():
            return("Image can not be found or has not been loaded.\n")
        else:
            rd2.delete('image')
            return("HGNC data image has been deleted from Redis.\n")
    else:
        return("The method you tried does not work.\n")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
