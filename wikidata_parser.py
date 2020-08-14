import numpy as np
import pandas as pd
#import scipy.stats as stats
import json
import seaborn as sns
import qwikidata
import random
import matplotlib.pyplot as plt
from qwikidata.json_dump import WikidataJsonDump
from qwikidata.linked_data_interface import get_entity_dict_from_api
from qwikidata.sparql import (get_subclasses_of_item,
                              return_sparql_query_results)
from collections import Counter
import ast
from qwikidata.linked_data_interface import LdiResponseNotOk
from qwikidata.entity import WikidataItem, WikidataProperty, WikidataLexeme
import sqlite3
from urllib3.exceptions import MaxRetryError
import threading
import time
import timeit
import traceback
import plotly.graph_objects as go
import tldextract
from urllib.parse import urlparse
import ssl
import languages_and_countries
from samplesize import sampleSize
import importlib

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

import logging
logging.basicConfig(
    filename='process.log',
    filemode='a+',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')