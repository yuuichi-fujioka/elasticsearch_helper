#!/bin/bash

NOW=$(date --iso-8601=seconds)
DT=$(date --iso-8601)
ps aux | awk 'NR>1{print "'$NOW' " $0}' | tee -a process_stat.txt |  es_stream process-${DT} process-doc datetime=date user=string pid=integer cpu=float mem=float vsz=long rss=long tty=non_analyzed stat=non_analyzed start=string time=string
