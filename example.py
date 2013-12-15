#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
    example for dbpedia by crawler data
"""
import dbpediaArea as pedia
import json

area = pedia.DbpediaArea()
data = json.loads(area.getDataByArea("China","json"))
print data["coordinate"]
