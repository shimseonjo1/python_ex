class Person:
    def __init__(self, name, age, gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print('저의 이름은', self.name, '이고요, 제 나이는 ', self.age, '살입니다.')


class Animal:
    def talk(self):
        print('talk')


class Employee(Person, Animal):
    def __init__(self, name, age, gender, salary, hire_date) -> None:
        super().__init__(name, age, gender)
        self.salary = salary
        self.hire_date = hire_date

    def do_work(self):
        print('열심히 일을 한다')

    def about_me(self):
        print('제 급여는 ', self.salary, '원이고, 제 입사일은 ', self.hire_date, '입니다.')
        super().about_me()


a1 = Person('김철수', 22, '남자')
a2 = Employee('홍길동', 33, '남자', 2300, '2023/01/01')
a1.about_me()
a2.about_me()
a2.talk()
