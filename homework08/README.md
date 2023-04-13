# "In The Kubernetes"

The Human Genome Organization (HUGO) is a non-profit organization that runs the HUGO Gene Noomenclature Committee (HGNC) in approving "a unique and meaningful name for every gene".

The homework07 directory consists of nine files.

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

Make a directory with <code>mkdir data</code> for the Redis database to mount a volume. Then, run the Flask application by using the <code>docker-compose.yaml</code> file with the command, <code>docker-compose up -d</code>.

## Kubernetes:

In order for the Flask container to deploy to a Kubernetes cluster,

1) Clone the repository to a system with access to the Kubernetes API, using <code>git clone git@github.com:Amandawlee/my-coe332-hws.git</code>, and head into the directory with the command, <code>cd my-coe332-hws/homework07/</code>.

2) From the built Docker image (from the instructions above), replace the Docker username in the line <code>image: awl/gene-api:1.0</code> to your username.

3) Set up the PVC to save the Redis data from the Flask app with the command <code>kubectl apply -f awl-test-redis-pvc.yml</code>.

4) Create a Deployment for the Redis database with the command <code>kubectl apply -f awl-test-redis-deployment.yml</code>.

5) Start the service with the command <code>kubectl apply -f awl-test-redis-service.yml</code>. Get the IP address for this service with the command <code>kubectl get services</code> and copy the IP address for the Redis service. In the <code>awl-test-flask-deployment.yml</code> file, change the line that says <code>value: 10.233.15.94</code> to the copied IP address.

6) Set up the Flask Deployment with the command <code>kubectl apply -f awl646-test-flask-deployment.yml</code>.

7) In order to get a persistent IP address for the Flask application, use the command <code>kubectl apply -f awl646-test-flask-service.yml</code>. Then, run <code>kubectl get services</code> to use the IP address to run routes for the Flask application. Replace <code>127.0.0.1</code> with the IP address from your Flask service (from the Example Outputs).

## Example Output:

To query the Flask application, inserting the following on the command line (depending on what information you would like to see):

```
$ curl http://127.0.0.1:5000...
	/data -X POST 		Loads HGNC data to a Redis database
	/data -X GET		Returns HCNC data set as a json-formatted list from Redis database
	/data -X DELETE		Deletes HGNC data from Redis database
	/genes			Returns a json-formatted list of all <hgnc_id> fields
	/genes/<hgnc_id>	Returns all data associated with a given <hgnc_id>
	/image -X POST		Reads some portion of data out of the database, runs some matplotlib code to create a simple plot of that data, and then writes the plot back into the database (db = 1)
	/image -X GET		Returns the image to the user (if present in the database)
	/image -X DELETE	Deletes the image from the database
```

Running <code>curl http://127.0.0.1:5000/data -X GET</code>:

```
[vm] $ curl http://127.0.0.1:5000/data -X GET
HGNC data has been loaded to a Redis database.
```

Running <code>curl http://127.0.0.1:5000/data -X GET</code>:

```
[vm] $ curl http://127.0.0.1:5000/data -X GET
{
.
.
.
{
    "_version_": 1761599377614307329,
    "agr": "HGNC:13703",
    "alias_symbol": [
      "MAK16L"
    ],
    "ccds_id": [
      "CCDS6089"
    ],
    "date_approved_reserved": "2000-10-19",
    "date_modified": "2023-01-20",
    "date_name_changed": "2015-07-03",
    "date_symbol_changed": "2008-06-04",
    "ena": [
      "AF251062"
    ],
    "ensembl_gene_id": "ENSG00000198042",
    "entrez_id": "84549",
    "gene_group": [
      "RNA binding motif containing"
    ],
    "gene_group_id": [
      725
    ],
    "hgnc_id": "HGNC:13703",
    "location": "8p12",
    "location_sortable": "08p12",
    "locus_group": "protein-coding gene",
    "locus_type": "gene with protein product",
    "mane_select": [
      "ENST00000360128.11",
      "NM_032509.4"
    ],
    "mgd_id": [
      "MGI:1915170"
    ],
    "name": "MAK16 homolog",
    "orphanet": 470626,
    "prev_name": [
      "RNA binding motif protein 13",
      "MAK16 homolog (S. cerevisiae)"
    ],
    "prev_symbol": [
      "RBM13"
    ],
    "pubmed_id": [
      29245012,
      29557065
    ],
    "refseq_accession": [
      "NM_032509"
    ],
    "rgd_id": [
      "RGD:1311297"
    ],
    "status": "Approved",
    "symbol": "MAK16",
    "ucsc_id": "uc003xjj.4",
    "uniprot_ids": [
      "Q9BXY0"
    ],
    "uuid": "e4a49609-b7dd-4be6-ba75-0cac2eda85ad",
    "vega_id": "OTTHUMG00000163957"
  }
]
```

Running <code>curl http://127.0.0.1:5000/data -X DELETE</code>:

```
[vm] $ curl http://127.0.0.1:5000/data -X DELETE
HGNC data has ben deleted from Redis database.
```

Running <code>curl http://127.0.0.1:5000/genes</code>:

```
[vm] $ curl http://127.0.0.1:5000/genes
[
.
.
.
  "HGNC:1766",
  "HGNC:16063",
  "HGNC:20024",
  "HGNC:17677",
  "HGNC:51443",
  "HGNC:32025",
  "HGNC:16350",
  "HGNC:15265",
  "HGNC:52950",
  "HGNC:24592",
  "HGNC:15822",
  "HGNC:24352",
  "HGNC:54766",
  "HGNC:26633"
.
.
.
]
```

Running <code>curl http://127.0.0.1:5000/genes</code>:

```
[vm] $ curl http://127.0.0.1:5000/genes
{
  "_version_": 1761544682705256448,
  "agr": "HGNC:1766",
  "ccds_id": [
    "CCDS82259",
    "CCDS11993"
  ],
  "date_approved_reserved": "1997-02-10",
  "date_modified": "2023-01-20",
  "date_name_changed": "2016-01-15",
  "ena": [
    "AB035301"
  ],
  "ensembl_gene_id": "ENSG00000081138",
  "entrez_id": "1005",
  "gene_group": [
    "Type II classical cadherins"
  ],
  "gene_group_id": [
    1186
  ],
  "hgnc_id": "HGNC:1766",
  "location": "18q22.1",
  "location_sortable": "18q22.1",
  "locus_group": "protein-coding gene",
  "locus_type": "gene with protein product",
  "mane_select": [
    "ENST00000397968.4",
    "NM_004361.5"
  ],
  "mgd_id": [
    "MGI:2442792"
  ],
  "name": "cadherin 7",
  "omim_id": [
    "605806"
  ],
  "prev_name": [
    "cadherin 7, type 2"
  ],
  "pubmed_id": [
    9615235
  ],
  "refseq_accession": [
    "NM_033646"
  ],
  "rgd_id": [
    "RGD:1306856"
  ],
  "status": "Approved",
  "symbol": "CDH7",
  "ucsc_id": "uc002lkb.4",
  "uniprot_ids": [
    "Q9ULB5"
  ],
  "uuid": "59ea51cf-2caf-4b9e-9624-58c5e6d917ca",
  "vega_id": "OTTHUMG00000132800"
}
```

Running <code>curl http://127.0.0.1:5000/image -X POST</code>:

```
[vm] $ curl http://127.0.0.1:5000/data -X POST
The HGNC ID data plot image has been loaded to Redis.
```

Running <code>curl http://127.0.0.1:5000/image -X GET</code>:

```
[vm] $ curl http://127.0.0.1:5000/data -X GET

```

Running <code>curl http://127.0.0.1:5000/image -X POST</code>:

```
[vm] $ curl http://127.0.0.1:5000/data -X POST
The HGNC ID data plot image has been deleted from Redis.
```

