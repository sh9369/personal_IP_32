#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests , re, json,time
from store_json import store_json


def bitnodes():
    requests.adapters.DEFAULT_RETRIES = 5
    http = requests.get('https://bitnodes.earn.com/api/v1/snapshots/latest/')
    neir = http.text
    neir_json = json.loads(neir)
    result = neir_json['nodes'].keys()
    ip_dict = {}
    for ip_port in result:
        ip = ip_port.split(':')[0]
        ip_dict[ip] ={
            'type':'mining pool',
            'source':'bitnodes.earn.com/api/v1/snapshots/latest/',
            'level':'CRITICAL',
            'fp':'unknown',
            'status':'unknown',
            'date': timestamp_datetime(neir_json['nodes'][ip_port][2])
        }
    return ip_dict

def timestamp_datetime(value):
    format = '%Y-%m-%d'
    # value为传入的值为时间�?整形)，如�?332888820
    value = time.localtime(value)
    ## 经过localtime转换后变�?    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    # 最后再经过strftime函数转换为正常日期格式�?    
    dt = time.strftime(format, value)
    return dt

if __name__=="__main__":
    dict = bitnodes()
    print len(dict.keys())
    store_json(dict,'bitnodes')