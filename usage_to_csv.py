import json
import pandas as pd
import sys
from datetime import datetime

json_fp = sys.argv[1]

with open(json_fp) as f:
    d = json.load(f)

data = []

for uid in d.keys():
    sub_d = d[uid]
    
    for page in sub_d.keys():
        taps = sub_d[page]['taps']
        try:
            time = sub_d[page]['time']
        except:
            time = None
        data.append([uid, page, taps, time])
            
df = pd.DataFrame(data=data, columns=['uid', 'page', 'taps', 'time'])
df.to_csv(f'{json_fp[:-5]}.csv', index=False)
print('JSON successfully converted')