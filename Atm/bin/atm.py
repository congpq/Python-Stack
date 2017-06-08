#!/usr/bin/env python
# -*- coding:utf-8 -*-

#程序的执行文件是atm.py
#程序的主入口是

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

from conf import settings
from core import main


main.login()
