from bs4 import BeautifulSoup
from urllib import request
import re
data = []
for i in range(1,10):
    url = f'https://movie.naver.com/movie/point/af/list.naver?page={i}'
    response = request.urlopen(url)
    soup = BeautifulSoup(response,'html.parser')
    # print(soup)
    table = soup.find('table',class_='list_netizen')
    for i,r in enumerate(table.select('tbody tr')):
        # print(i)
        # print(r)
        for j,c in enumerate(r.find_all('td')):
            # print(j)
            # print(c)
            movie_dic={}
            if j == 0:
                print('글번호: ',c.string.strip())
                # movie_dic['글번호'] = int(c.string.strip())
            elif j == 1:
                # print('제목 : ',c.select_one('a').string.strip())
                movie_dic['제목'] = c.select_one('a').string.strip()
                # print('평점 : ',c.select_one('em').string)
                movie_dic['평점'] = c.select_one('em').string
                review = c.text
                review = review.replace(movie_dic['제목'],'')
                review = review.replace('신고','')
                movie_dic['영화평'] = re.sub('별점 - 총 10점 중[0-9]{1,2}','',review).strip()
                # print('영화평 : ', movie_dic['영화평'])
            data.append(movie_dic)
print(data)
