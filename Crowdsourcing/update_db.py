import pandas as pd
import json
import mturk
import time
import pymongo
import sys
from datetime import datetime

""" 
    Run this with 'python update_db.py x y z' where:
    x is 0 if using the sandbox, 1 if using the marketplace;
    y is the amount of seconds to wait between loops;
    z is 0 if not approving assignments as they come, 1 otherwise
    
"""

with open('./config/mongodb_credentials.json','r') as f:
    mongodb_credentials = json.load(f)

create_hits_in_production = (sys.argv[1] == '1')
time_between_updates = sys.argv[2]
to_approve = (sys.argv[3] == '1')
# Change the string in MongoClient to a connection string to a Mongodb base/cluster of your choice

db_client = pymongo.MongoClient(mongodb_credentials["connection_string"])

db = db_client['wikidata']
hit_result_collection = db.hit_results if create_hits_in_production else db.hit_results_sandbox

mt = mturk.MTurk()
mt.launch_client(create_hits_in_production)

fails = 0
while True:
    ''' Update all hits in the database with correct results '''
    hit_result_collection_list = list(hit_result_collection.find({'hit.HITStatus': {'$not': {'$eq': 'Disposed'}}}))
    for hit in hit_result_collection_list:
        try:
            hit_result_collection.update_one(
                {'_id': hit['_id']},
                {
                    "$set": {
                        "hit": mt.client.get_hit(HITId = hit['_id'])['HIT'],
                        'answers': mt.get_hit_answers(hit['_id'], approve=to_approve)
                    }
                })
        except Exception as e:
            print(e)
            fails = fails + 1
            if fails > 4:
                sys.exit(-1)
            continue
    print('{}: Updated db has {} non-disposed entries'.format(datetime.now(),len(hit_result_collection_list)))
    time.sleep(int(time_between_updates))
