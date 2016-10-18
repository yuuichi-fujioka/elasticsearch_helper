#!/bin/bash

ps aux | awk 'NR>1{print $0}' | es_stream hoge hoge-doc user=string pid=integer cpu=float mem=float vsz=long rss=long tty=non_analyzed stat=non_analyzed start=string time=string
