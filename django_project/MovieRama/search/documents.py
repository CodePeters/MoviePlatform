
from movie_catalog.models import Movie 


from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class MovieDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'movie'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Movie # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'title',
          
            'description',
            'id',
        ]