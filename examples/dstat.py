#!/usr/bin/env python

import elasticsearch_helper

es = elasticsearch_helper.make_from_env()

from elasticsearch_helper import index_helper

index_helper.delete_index(es, 'taro')
index_helper.make_index(es, 'taro', 'taro-doc',
    system_time="date")

from elasticsearch_helper import bulk_helper
import datetime
import csv
import itertools
import pytz       # pip instal pytz

JST = pytz.timezone('Asia/Tokyo')


def _parse(name, value):
    if "system_time":
        return datetime.datetime.strptime(
            "2017-"+valeu,
            '%Y-%d-%m %H:%M:%S').replace(tzinfo=JST)
    else:
        return float(value)

with bulk_helper.bulk(es) as putter:
    with open('dstat.log', 'r') as f:
        reader = csv.reader(f)
        while next(reader):
            pass  # skip to blank line
        header1 = next(reader)
        for i, v in itertools.izip(xrange(len(header1)), header1):
            if not v:
                header1[i] = label
            else:
                label = v
        
        header2 = next(reader)
        header = ["_".join((k,v)) for k, v in itertools.izip(header1, header2)]
        for data in reader:
            d = {k: _parse(k, v) for k, v in itertools.izip(header, data)}
            putter('taro', None, 'taro-doc', d)
