import elasticsearch_helper

es = elasticsearch_helper.make_from_env()

from elasticsearch_helper import index_helper

index_helper.delete_index(es, 'taro')
index_helper.make_index(es, 'taro', 'taro-doc',
    full_name='non_analyzed',
    created_at="date",
    age='integer',
    first_name='analyzed',
    last_name='analyzed')

from elasticsearch_helper import bulk_helper
import datetime

with bulk_helper.bulk(es) as putter:
    for _ in range(2090):
        putter('taro', None, 'taro-doc', {
            "first_name": "taro" + str(_),
            "last_name": "yamada",
            "full_name": "yamada taro" + str(_),
            "age": _,
            "created_at": datetime.datetime.now(),
        })

