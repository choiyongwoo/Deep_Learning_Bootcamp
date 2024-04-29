import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

def get_current_datetime_str():
    # 현재 날짜와 시간을 가져옴
    now = datetime.now()
    # 원하는 형식(년월일시분)으로 날짜와 시간을 포맷팅
    formatted_now = now.strftime("%Y%m%d%H%M")
    return formatted_now

artids=[]
comment_list= []

date_url= 'https://imnews.imbc.com/news/2024/politics/cal_data.js?202403271350'
date_header= {
    'referer':'https://imnews.imbc.com/news/2024/politics/6582936_36426.html',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
}
resp= requests.get(date_url)
jsn= json.loads(resp.content.decode('utf-8-sig'))
for date in jsn['DateList']:
    print(date)
    article_url= 'https://imnews.imbc.com/news/2024/politics/'+date['CurrentID']+'_36428.js?'+get_current_datetime_str()
    #print(article_url)
    resp= requests.get(article_url)
    article_jsn= json.loads(resp.content.decode('utf-8-sig'))

    for i in article_jsn['Data'][0]['List']:
        artids.append(i['AId'])

    for id in artids:
        
        url= 'https://imnewsapi.imnews.imbc.com/cmt/cmtList'
        headers= {
            'referer':'https://imnews.imbc.com/news/2024/politics/article/6583388_36431.html?utm_source=dable',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0'
        }
        params= {
                'callback':'cmtList_202403261617',
                'ArtId':f'{id}',
                'Page':'1',
                'PageSize':'5',
                'OrderType':'1'
            }
        resp= requests.get(url, headers=headers, params=params)
        jsn= json.loads(resp.text[21:-1])
        
        total_cmt= jsn['TotalCnt']
        count=0


        
        for i in range(1,100000):
            count+=1
            params= {
                'callback':'cmtList_202403261617',
                'ArtId':f'{id}',
                'Page':f'{i}',
                'PageSize':'5',
                'OrderType':'1'
            }
            if count>total_cmt:
                break
            resp= requests.get(url, headers=headers, params=params)
            jsn= json.loads(resp.text[21:-1])
            for j in jsn['List']:
                comment_list.append(j['CmtCont'])
        
    
print(len(comment_list))