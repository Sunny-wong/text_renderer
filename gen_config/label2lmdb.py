import pandas as pd
import json


train_label_path = './config/output/train/labels.json'
with open(train_label_path, 'r') as load_f:
    load_dict = json.load(load_f)
    
df = pd.DataFrame(load_dict)
df.index =pd.Series(df.index) + '.jpg'
df
# new_index.to_list()
df['labels'].to_csv('./config/output/train/train_labels.txt', sep='\t', header=False)

test_label_path = './config/output/test/labels.json'
with open(test_label_path, 'r') as load_f:
    load_dict = json.load(load_f)
    
df = pd.DataFrame(load_dict)
df.index =pd.Series(df.index) + '.jpg'
df
# new_index.to_list()
df['labels'].to_csv('./config/output/test/test_labels.txt', sep='\t', header=False)