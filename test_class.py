class User:
    def __init__(self, username, email, password):
        self.username = username
        self.emai = email
        self.password = password

    def get_username(self):
        return self.username

    def get_email(self):
        return self.emai

u = User('bob', 'bob@example.com', 'foobar')
a = User('egor', 'keklol@yahoo.com', 'natali')
print(u.emai)
print(u.get_email())
print(User.get_email(a))


class Second:
    color = "red"
    form = "circle"

    def changecolor(self, newcolor):
        self.color = newcolor

    def changeform(self, newform):
        self.form = newform


obj1 = Second()
obj2 = Second()

print(obj1.color, obj1.form)  # вывод на экран "red circle"
print(obj2.color, obj2.form)  # вывод на экран "red circle"

obj1.changecolor("green")  # изменение цвета первого объекта
obj2.changecolor("blue")  # изменение цвет второго объекта
obj2.changeform("oval")  # изменение формы второго объекта

print(obj1.color, obj1.form)  # вывод на экран "green circle"
print(obj2.color, obj2.form)  # вывод на экран "blue oval"

text=str()
for i in range(3):
    text+=chr(65)
print(text)

print(-13%12)