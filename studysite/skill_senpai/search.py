from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
import models

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search

connections.create_connection()

class LectureIndex(DocType):
	title = Text()
	short_description = Text()
	description = Text()

	class Meta:
		index = 'lecture-index'
# TODO implement other fields for more sophisticated search

def bulk_indexing():
	LectureIndex.init(index='lecture-index')
	es = Elasticsearch()
	bulk(client=es, actions=(b.indexing() for b in models.Lecture.objects.all().iterator()))


def search(title):
	s = Search().filter('term', title=title)
	response = s.execute()
	return response