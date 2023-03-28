from flask import Flask, request
import json
import requests
import redis

app = Flask(__name__)

gene_data = []

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
def data() -> list:
    """
    """
    if request.method == 'POST':
        response = requests.get(url = 'https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json')
        gene_data = response.json()
        for item in gene_data:
            key = f"{item['response']['docs']['hgnc_id']}"
            rd.hset(key, mapping = item)
        return("HGNC data has been loaded to a Redis database.\n")
    elif request.method == 'GET':
        gene_data = []
        for item in rd.keys():
            gene_data.append(rd.hgetall(item))
        return(gene_data)
    elif request.method == 'DELETE':
        rd.flushdb()
        return("HGNC data has ben deleted from Redis database.\n")
    else:
        return("The method you used is not available.\n")

@app.route('/genes', methods = ['GET'])
def get_hgnc_ids() -> list:
    """
    Returns a json-formatted list of all HGNC_ID fields

    Args:
        No arguments

    Returns:
        hgnc_ids_list: A list of HGNC IDs from HGNC data set
    """
    
    hgnc_ids_list = []
    for key in rd.keys():
        gene_data  = rd.hgetall(key)
        if gene_data[hgnc_id] not in hgnc_ids_list:
            hgnc_ids_list.append(gene_data['hgnc_id'])
    return(hgnc_ids_list)

@app.route('/genes/<hgnc_id>', methods = ['GET'])
def get_hgnc_id_data(hgnc_id) -> list:
    """
    """
    hgnc_id_data = []
    if hgnc_id in get_hgnc_ids():
        for key in rd.keys():
            gene_data = rd.hgetall(key)
            if gene_data['hgnc_id'] == hgnc_id:
                hgnc_id_data.append(gene_data)
    return(hgnc_id_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
