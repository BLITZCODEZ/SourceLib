#!/usr/bin/python

import SourceLib
import asyncore
import subprocess

from datetime import datetime

query = SourceLib.SourceQuery.SourceQuery('127.0.0.1', 27016)

info = query.info()
#print info
print(info['numplayers'])



