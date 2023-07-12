import pandas as pd
import json
with open(r'json.js', 'r') as f:
    data = json.load(f)
# Hiển thị toàn bộ cột và dòng
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)



def flatten(data, key=None, *, seperator="."):
    if isinstance(data, list):
        for item in data:
            yield from flatten(item, key)
    elif isinstance(data, dict):

        for k, v in data.items():
            if key:
                new_key = key + seperator + k
                yield from flatten(v, new_key)
            else:
                yield from flatten(v, k)
    else:
        yield key, data
array_tuple = list(flatten(data))
with open(r'text.txt', 'w') as f:
    for item in array_tuple:
        for k, v in enumerate(array_tuple):
            f.write(v[0])
print(array_tuple)
