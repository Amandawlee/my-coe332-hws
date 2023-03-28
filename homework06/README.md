# "Say It' Ain't Genes

The Human Genome Organization (HUGO) is a non-profit organization that runs the HUGO Gene Noomenclature Committee (HGNC) in approving "a unique and meaningful name for every gene".

The homework06 directory consists of four files: <code>gene_api.py</code>, <code>README.md</code>, <code>Dockerfile</code>, and <code>docker-compose.yaml</code>.

The <code>gene_api.py</code> file queries and returns information about genes found in the the human genome, approved by the HGNC, setting standards for human gene nomenclature. The complete set of HGNC data was downloaded and injected into a Redis database through a Flask application.

## Instructions

First Method:

Use <code>git clone git@github.com:Amandawlee/my-coe332-hws.git</code> to clone the repository to your local system. Then, locate the file through <code>cd my-coe332-hws/homework06</code>. In order to run the code, run the Flask application through one ssh terminal and then query it through another ssh terminal.

To run the Flask application, insert the following on the command line: <code>flask --app gene_api --debug run</code>.

Second Method:

Use <code>git clone git@github.com:Amandawlee/my-coe332-hws.git</code> to clone the repository to your local system. Then, locate the file through <code>cd my-coe332-hws/homework06</code>. Build a Docker image locally from the Dockerfile with <code>docker build -t username/gene_api:1.0 .</code>. Then, run the image as a container with <code>docker run -it --rm -p 5000:5000 username/gnee_api:1.0</code>. Replace <code>username</code> with your username for Docker Hub.

Third Method:

Pull a prebuilt image on Docker Hub with <code>docker pull amandawlee/gene_api:1.0</code>  and run it using <code>docker run -it --rm -p 5000:5000 amandawlee/gene_api:1.0</code>.

Fourth Method:

Run the Flask application by using the <code>docker-compose.yaml</code> file with the command, <code>docker-compose up -d</code>.

## Example Output:

To query the Flask application, inserting the following on the command line (depending on what information you would like to see):

```
$ curl http://127.0.0.1:5000...
	/data -X POST 		Loads HGNC data to a Redis database
	/data -X GET		Returns HCNC data set as a json-formatted list from Redis database
	/data -X DELETE		Deletes HGNC data from Redis database
	/genes			Returns a json-formatted list of all <hgnc_id> fields
	/genes/<hgnc_id>	Returns all data associated with a given <hgnc_id>
```

Running <code>curl http://127.0.0.1:5000/data -X POST</code>:

```
[vm] $ curl http://127.0.0.1:5000/data -X POST

