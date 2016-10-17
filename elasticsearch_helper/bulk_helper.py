import contextlib

from elasticsearch import helpers


@contextlib.contextmanager
def bulk(es):

    def _(index, id, type, data):
        _.cache.append({
            '_index': index,
            '_id': id,
            '_type': type,
            '_source': data})
        if len(_.cache) > 1000:
            _flush()

    def _flush():
        helpers.bulk(es, _.cache)
        _.cache = []

    _.cache = []
    yield _

    _flush()
