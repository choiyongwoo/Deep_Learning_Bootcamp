#감성 사전 작성
from eunjeon import Mecab

data_dict={}
with open('SentiWord_Dict.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        striped_line= line.strip()
        if not striped_line:
            continue
        try:
            key,value= line.strip().split('\t')
            data_dict[key]=value

        except ValueError:
            key, value= line.strip().split(' ')
            data_dict[key]=value

keys= data_dict.keys()
print(data_dict)


m= Mecab()
for key in keys:
    print(m.pos(key))









    







