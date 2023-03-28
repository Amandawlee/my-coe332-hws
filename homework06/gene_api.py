from flask import Flask, request
import json
import requests
import redis

app = Flask(__name__)

def get_redis_client():
    """
    Generates a Python Redis client

    Args: 
        No arguments

    Returns:
        Redis client
    """
    return redis.Redis(host='redis-db', port=6379, db=0, decode_responses=True)

rd = get_redis_client()

@app.route('/data', methods = ['POST','GET','DELETE'])
def data():
    """
    """
    global rd
    if request.method == 'POST':
        response = requests.get(url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        gene_data = response.json()

        for item in gene_data['response']['docs']:
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
    """
    if len(rd.keys()) == 0:
        return("The database is currently empty.\n")

    for key in rd.keys():
        if str(key) == str(hgnc_id):
            return(json.loads(rd.get(key)))
    
    return("The given HGNC ID does not match any IDs in the database.\n")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
