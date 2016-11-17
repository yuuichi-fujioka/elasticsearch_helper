#!/bin/bash

NOW=$(date --iso-8601=seconds)
ps aux | awk 'NR>1{print "'$NOW' " $0}' | es_stream process process-doc datetime=date user=string pid=integer cpu=float mem=float vsz=long rss=long tty=non_analyzed stat=non_analyzed start=string time=string
