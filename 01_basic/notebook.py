class Note:
    def __init__(self,contents=None):
        self.contents = contents

    def write_contents(self,contents):
        self.contents = contents

    def remove_all(self):
        self.contents = ''

    def __str__(self):
        if self.contents == None:
            self.contents = '없음'
        return self.contents


class NoteBook:
    def __init__(self,title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self,note,page=0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page:note}
                self.page_number += 1
        else:
            print('페이지가 모두 채워졌습니다.')

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print('해당 페이지는 존재하지 않습니다.')

    def get_number_of_pages(self):
        return len(self.notes.keys())

