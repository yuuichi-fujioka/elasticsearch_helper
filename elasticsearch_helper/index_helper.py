class _Mapping(object):

    def __init__(self):
        self._properties = {}

    def non_analyzed(self, name):
        self._properties[name] = {
            "type": "string",
            "index": "not_analyzed"
        }

    def analyzed(self, name):
        self._properties[name] = {
            "type": "string",
        }

    def integer(self, name):
        self._properties[name] = {
            "type": "integer",
        }

    def long(self, name):
        self._properties[name] = {
            "type": "long",
        }

    def date(self, name):
        self._properties[name] = {
            "type": "date",
        }


def make_index(es, name, doc_type, **name_type_map):

    m = _Mapping()
    for k, v in name_type_map.items():
        getattr(m, v)(k)

    if not es.indices.exists(name):
        es.indices.create(index=name)
    es.indices.put_mapping(index=name, doc_type=doc_type, body={
        doc_type: {
            'properties': m._properties
        }
    })


def delete_index(es, name):

    if es.indices.exists(name):
        es.indices.delete(index=name)
