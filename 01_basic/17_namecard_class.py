import namecard as nc
import pickle

cardbook = None

with open('01_basic/cardbook.pickle','rb') as f:
    cardbook = pickle.load(f)

while True:
    menu = input('''
------------------------------------------------------------------------
1.CardBook 생성 2.Card추가 3.Card삭제 4.Card내용 보기 5.전체목록 보기 6.종료 
>>> ''')
    if menu == '1':
        if cardbook == None:
            cardbook = nc.CardBook(input('타이틀을 입력하세요 >>>'))
        else:
            print('생성된 cardbook이 존재합니다.')
    elif menu == '2':
        if cardbook == None:
            print('cardbook 생성한 후 추가 가능합니다.')
        else:
            name = input('name >>> ')
            address = input('address >>> ')
            tel = input('tel >>> ')
            email = input('email >>> ')
            card = nc.Card(name,address,tel,email)
            cardbook.add_card(card)
    elif menu == '3':
        if cardbook == None:
            print('cardbook 생성한 후 가능합니다.')
        else:
            print(list(cardbook.cards.keys()))
            page = int(input('page number >>> '))
            card = cardbook.remove_card(page)
            print(card, '-> 삭제')

    elif menu == '4':
        if cardbook == None:
            print('cardbook 생성한 후 가능합니다.')
        else:
            print(list(cardbook.cards.keys()))
            page = int(input('page number >>> '))
            card = cardbook.cards[page]
            print(card)
    elif menu == '5':
        if cardbook == None:
            print('cardbook 생성한 후 가능합니다.')
        else:
            cardbook.list_cards()

    elif menu == '6':
        print('프로그램 종료')
        break


with open('01_basic/cardbook.pickle','wb') as f:
    pickle.dump(cardbook,f)