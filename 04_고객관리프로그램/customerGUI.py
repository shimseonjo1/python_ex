from tkinter import *

class mainwin():
    def __init__(self) -> None:
       self.display()      
    
    def display(self):
        self.root = Tk()
        self.root.title('프로그램')
        self.button = Button(self.root,text='버튼입니다. 누르면 함수가 실행됩니다.',command=self.event)
        self.button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
        self.root.mainloop()   

    def event(self):
        self.button['text'] = '버튼 누름!'
        
mainwin()