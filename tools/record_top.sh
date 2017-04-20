#!/bin/bash

NOW=$(date --iso-8601=seconds)
DT=$(date --iso-8601)
top -b -n 1 | awk 'NR>7{print "'$NOW' " $0}' | tee -a top_stat.txt |  es_stream top-${DT} top-doc datetime=date pid=integer user=string pr=float ni=float virt=long res=long shr=long stat=non_analyzed cpu=float mem=float time=string
