import notebook as nb
import pickle

'''
노트북은 하나만 생성할 수 있다.

1.노트북 생성 2.노트추가 3.노트삭제 4.노트내용 보기 5.종료
'''
notebook = None

with open('01_basic/notebook.pickle','rb') as f:
    notebook = pickle.load(f)

while True:
    menu = input('''
-------------------------------------------------------
1.노트북 생성 2.노트추가 3.노트삭제 4.노트내용 보기 5.종료 
>>> ''')
    if menu == '1':
        if notebook == None:
            notebook = nb.NoteBook(input('타이틀을 입력하세요 >>>'))
        else:
            print('생성된 노트북이 존재합니다.')
    elif menu == '2':
        if notebook == None:
            print('노트북 생성한 후 추가 가능합니다.')
        else:
            contents = input('노트내용 >>> ')
            note = nb.Note(contents)
            notebook.add_note(note)
    elif menu == '3':
        if notebook == None:
            print('노트북 생성한 후 가능합니다.')
        else:
            print(list(notebook.notes.keys()))
            page = int(input('page number >>> '))
            note = notebook.remove_note(page)
            print(note, '-> 삭제')

    elif menu == '4':
        if notebook == None:
            print('노트북 생성한 후 가능합니다.')
        else:
            print(list(notebook.notes.keys()))
            page = int(input('page number >>> '))
            note = notebook.notes[page]
            print(note)

    elif menu == '5':
        print('프로그램 종료')
        break


with open('01_basic/notebook.pickle','wb') as f:
    pickle.dump(notebook,f)