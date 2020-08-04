import pandas as pd


xinhua_data_path= './gen_config/data/xinhuazidian_word.json'
xinhua_data = pd.read_json(xinhua_data_path)

# gen text
xinhua_txt_path = "./gen_config/data/xinhua_text.txt"
xinhua_data[['explanation', 'more']].to_csv(xinhua_txt_path, sep=' ', header=False, index=False)
print(type(xinhua_data[['explanation', 'more']]))

# gen key文件
xinhua_label_path = './gen_config/data/xinhua_key.txt'
xinhua_key_data = open(xinhua_txt_path, encoding='utf8').read()

xinhua_key_data= pd.DataFrame({'data': pd.Series(list(xinhua_key_data)).unique()})
xinhua_key_data.drop(index=(xinhua_key_data.loc[(xinhua_key_data['data']== '\n')].index))
xinhua_key_data = xinhua_key_data.replace('\n', ' ')
xinhua_key_data.to_csv(xinhua_label_path, header=False, index=False)

# 生成key中第一行和第118行有几个引号需要手工处理下 
