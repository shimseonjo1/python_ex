import json

def save(card):
    while True:
        name = input('이름을 입력하세요 >>>')
        check = 0
        for item in card:
            if item['name'] == name:
                check = 1
        if check == 0:
            break
        print('중복되는 이름이 있습니다.')
        
    address = input('주소를 입력하세요 >>>')
    tel = input('전화번호를 입력하세요 >>>')
    email = input('이메일을 입력하세요 >>>')
    card.append({'name':name,'address':address,'tel':tel,'email':email})   
    print(card)
    
def update(card):
    name = input('수정할 데이터 이름 >>>')
    idx = -1
    for i, item in enumerate(card):
        if item['name'] == name:
            idx = i

            while True:
                update = input('수정할 정보 - address,tel,email,exit(종료) >>> ')
                if update in ('address','tel','email'):
                    card[idx][update] = input(f'{update} 수정내용 >>> ')
                elif update == 'exit':
                    break

            print(card[idx])
            break
    if idx == -1:
        print('등록되지 않은 데이터 입니다.')

def delete(card):
    name = input('삭제할 이름 입력 >>> ')
    delok = 0
    for i, item in enumerate(card):
        if item['name'] == name :
            print(item,'삭제!!')
            del card[i]
            delok = 1
            break
    if delok == 0:
        print('등록되지 않은 데이터 입니다.')    

def cardlist(card):
    for item in card:
        print(f'''
----------------------------------
  이    름 : {item['name']}
  주    소 : {item['address']}
  전화번호 : {item['tel']}
  이 메 일 : {item['email']} ''')

def search(card):
    name = input('검색할 이름 >>>')
    idx = -1
    for i, item in enumerate(card):
        if item['name'] == name:
            idx = i
            print(item)
            break
    if idx == -1:
        print('등록되지 않은 데이터 입니다.')

def datasave(card):
    with open('01_basic/namecard.data','w') as f:
        json.dump(card,f,indent=2)

def dataload(card):
    with open('01_basic/namecard.data','r') as f:
        card = json.load(f)
    return card