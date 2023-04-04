url = 'https://music.bugs.co.kr/chart'
response = request.urlopen(url)
soup = BeautifulSoup(response,'lxml')

title_list = []
artist_list = []

title = soup.select('p.title > a')
# print(title)
for item in title:
    # print(item.string)
    title_list.append(item.string)

artist = soup.select('p.artist')
print(len(artist))
for item in artist:
    # print(item)
    # print(item.text)
    # print(item.text.strip())
    # print('--------------')
    artist_list.append(item.text.strip())
    
print(len(title_list),len(artist_list))

artist_list_final = []
for item in artist_list:
    # print(item.replace('\n\n\r\n',','))
    # print(item.replace('\n\n\r\n',',').split(',')[0])
    artist_list_final.append(item.replace('\n\n\r\n',',').split(',')[0])
    
result = list(zip(title_list,artist_list_final))
print(result)
