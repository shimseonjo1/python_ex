class Card:
    def __init__(self,name,address,tel,email):
        self.name = name
        self.address = address
        self.tel = tel
        self.email = email

    def write_card(self,name,address,tel,email):
        self.name = name
        self.address = address
        self.tel = tel
        self.email = email

    def remove_all(self):
        self.name = ''
        self.address = ''
        self.tel = ''
        self.email = ''

    def __str__(self):
        return f'name :{self.name}, address:{self.address}, tel:{self.tel}, email:{self.email}'


class CardBook:
    def __init__(self,title):
        self.title = title
        self.page_number = 1
        self.cards = {}

    def add_card(self,card,page=0):
        if self.page_number < 300:
            if page == 0:
                self.cards[self.page_number] = card
                self.page_number += 1
            else:
                self.cards[page] = card
                self.page_number += 1
        else:
            print('페이지가 모두 채워졌습니다.')

    def remove_card(self, page_number):
        if page_number in self.cards.keys():
            return self.cards.pop(page_number)
        else:
            print('해당 페이지는 존재하지 않습니다.')

    def get_number_of_pages(self):
        return len(self.cards.keys())

    def list_cards(self,key=None,reverse=False):
        if key == None:
            for page in self.cards:
                print(self.cards[page])
        else:
            sorted_dict = sorted(self.cards.items(), key = eval(f'lambda item: item[1].{key}'), reverse = reverse)
            for page,card in sorted_dict:
                print(card)


