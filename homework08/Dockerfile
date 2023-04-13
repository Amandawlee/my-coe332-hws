FROM python:3.8.10

ENV REDIS_IP redis-db

RUN pip install Flask==2.2.2
RUN pip install requests==2.22.0
RUN pip install redis==4.5.1
RUN pip install matplotlib
RUN pip install numpy

ADD ./gene_api.py /gene_api.py

CMD ["python3", "gene_api.py"]
