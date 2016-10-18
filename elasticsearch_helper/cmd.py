import os
import datetime
import itertools
import socket
import sys

from dateutil import parser
import elasticsearch_helper as helper
from elasticsearch_helper import bulk_helper
from elasticsearch_helper import index_helper


class Mapping(object):
    def __init__(self, key, type):
        self.key = key
        self.type = type

    def parse(self, value):
        if self.type == 'integer':
            return int(value)
        if self.type == 'long':
            return long(value)
        if self.type == 'float':
            return float(value)
        if self.type == 'date':
            return parser.parse(value)
        return value


def _parse_mapping_args(argv):
    mappings = []
    for kv in argv:
        if kv != 'skip':
            key, _, type = kv.partition('=')
            mappings.append(Mapping(key, type))
        else:
            mappings.append(Mapping('', 'skip'))
    return mappings


def stream():
    index_name = sys.argv[1]
    doc_type = sys.argv[2]
    mappings = _parse_mapping_args(sys.argv[3:])

    types = set([m.type for m in mappings if m != 'skip'])

    es = helper.make_from_env()
    index_mapping = {m.key: m.type for m in mappings if m.type != 'skip'}
    index_mapping['host'] = 'non_analyzed'
    if 'date' not in types:
        index_mapping['@time'] = 'date'
    index_helper.make_index(
        es, index_name, doc_type, **index_mapping)

    hostname = os.environ.get('ES_HOSTNAME', socket.gethostname())
    parameter_len = len(mappings)
    with bulk_helper.bulk(es) as putter:
        try:
            while True:
                line = raw_input()
                values = line.split(None, parameter_len)
                data = {
                    m.key if m and m.key else "data": m.parse(v) if m else v
                    for m, v in itertools.izip_longest(mappings, values)
                    if not m or m.type != "skip"}
                if 'date' not in types:
                    data['@time'] = datetime.datetime.utcnow()
                data['host'] = hostname
                putter(index_name, None, doc_type, data)
        except Exception:
            pass


def del_index():
    es = helper.make_from_env()
    for name in sys.argv:
        index_helper.delete_index(es, name)
