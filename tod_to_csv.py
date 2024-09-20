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
    
    for date in sub_d.keys():
        day_d = sub_d[date]
        
        for opt in day_d.keys():
            data.append([uid, date, opt, day_d[opt]['TurnsTaken'], day_d[opt]['TimeSpent']])
            
df = pd.DataFrame(data=data, columns=['uid', 'date', 'option', 'turns', 'time'])
df.to_csv(f'{json_fp[:-5]}.csv', index=False)
print('JSON successfully converted')