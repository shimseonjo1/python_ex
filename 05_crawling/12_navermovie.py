from bs4 import BeautifulSoup
import urllib.request
import re

#v페이지가 있는 사이트에서 가져오기
list_records=[]
for i in range(1,11):
    params=urllib.parse.urlencode({'page':i})
    url="https://movie.naver.com/movie/point/af/list.naver?{params}"
    response = urllib.request.urlopen(url)

    soup=BeautifulSoup(response,'html.parser')
    table=soup.find('table',class_='list_netizen')

    for i,r in enumerate(table.select('tbody tr')):
    #     print(i)
    #     print(r)
        for j,c in  enumerate(r.find_all('td')):
    #         print(j)
    #         print(c)
            if j==0:
                record=int(c.text.strip())
                print('글번호:',record)
            elif j==1:
                record1=str(c.select_one('td.title a').text.strip())
                print('제목:',record1)
                record2=c.select_one('em').text
                print('점수:',record2)
                record3=c.text
                record3=record3.replace(record1,'')
                record3=record3.replace('신고','')
                record3=re.sub('별점 - 총 10점 중[0-9]{1,2}','',record3).strip()
                print('감상평:',record3)
        try:
            movie_dic={'제목':record1,'점수':int(record2),'감상평':record3}
            list_records.append(movie_dic)
        except:
            pass

print(list_records)