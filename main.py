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


column_names = []
data_dict = {}
for item in array_tuple:
    column_name, value = item[0], item[1]
    if column_name not in data_dict:
        data_dict[column_name] = []
        column_names.append(column_name)
    data_dict[column_name].append(value)
# Lấy max length de chinh lai dict cho aray bang nhau het
max_length = max(len(value) for value in data_dict.values())
for key in data_dict:
    data_dict[key] += [None] * (max_length - len(data_dict[key]))

df = pd.DataFrame(data_dict, columns=column_names)
ten_tep = input("")
with open(f'{ten_tep}.txt', 'w') as f:
    f.write(df.to_string(index =False))
print(array_tuple)
print(df.to_string(index =False))
