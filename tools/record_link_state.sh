#!/bin/bash

NOW=$(date --iso-8601=seconds)
ip link show | grep mtu | sed "s/^[^ ]\+ \+//g" | sed "s/:.*state / /g" | sed "s/ mode.*//g" | awk '{print "'$NOW' " $0}'| es_stream link link-doc datetime=date  interface=non_analyzed state=non_analyzed 
