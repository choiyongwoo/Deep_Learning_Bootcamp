#txt 단어추가
#추가할 텍스트 읽고
with open('C:/Users/USER/text_mining_project/text_mining_project/compound_text.txt','r',encoding='utf-8') as f:
    file_data= f.readlines()

#csv 읽어온 뒤
with open("C:/mecab/user-dic/nnp.csv", 'r', encoding='utf-8') as f:
    csv_data= f.readlines()

#읽을 단어 추가
csv_set = set(csv_data)
# 읽은 단어 추가, 단 중복되지 않는 경우에만 추가
for line in file_data:
    if line not in csv_set:  # 중복 확인
        csv_data.append(line)
#csv에 쓰기
with open("C:/mecab/user-dic/nnp.csv", 'w', encoding='utf-8', newline='') as f: 
    for line in csv_data: 
        f.write(line)