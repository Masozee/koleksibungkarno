from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models

connections.create_connection()

class PerupaIndex(DocType):
    Nama = Text()
    Panggilan = Date()
    Alamat = Text()
    text = Text()

    class Meta:
        index = 'perupaindex'


def bulk_indexing():
    PerupaIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.perupa.objects.all().iterator()))