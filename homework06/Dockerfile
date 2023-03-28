FROM python:3.8.10

RUN pip install Flask==2.2.2
RUN pip install requests==2.22.0
RUN pip install redis==4.5.1

ADD ./gene_api.py /gene_api.py

CMD ["python", "/gene_api.py"]
