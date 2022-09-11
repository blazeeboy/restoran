# Программа для Ресторана
# Использовать при создании: Tkinter для интерфейса, Файлы для сохранения,
# Классы.
# Описание!
# Придумать свой ресторан. (имя, описание)
# У ресторана есть склад с продуктами. (курица, капуста, сыр...)
# У ресторана есть блюда, каждое из которых состоит из определенных
# ингредиентов.
# (бургер: 200 гр мяса, 10 гр сыра, 2 куска хлеба)
# Есть баланс ресторана, 12+ блюд, 8+ ингредиентов, 8+ столиков.
# На каждый из столов официант может добавлять заказы.
# В конце может распечатать чек для столика.
# Можно закупать продукты для склада из магазина.
# Требования!
# Красивый интерфейс. (шрифты, расположение кнопок и т.д)
# Окна: Столики, Склад, Магазин.
# При добавлении заказа меняется сумма у столика.
# При распечатке чека стол обнуляется, и деньги поступают на баланс.
# Невозможно заказать блюдо, если нет одного из ингредиентов.
# Возможность показа склада и баланса.
# У каждого блюда и продукта есть картинка.
# Сохранять склад и баланс в файле.
# Отдельно написать небольшое описание ресторана.
# Будет учитываться чистота кода и правильность работы программы.
# При возникновении дополнительных вопросов обратитесь к учителю.
# Дополнительное (по желанию)
# Добавить отдельные аккаунты для официантов. (логин, регистрация)
# При оплате больше нужной, оставшиеся деньги идут на счет официанта.

import tkinter as tk
from tkinter import *
gui = tk.Tk()
gui.title("Программа для ресторана")
gui.geometry("1920x1080")
gui.configure(bg="grey")
gui.resizable(False, False)

text = "The Symposium Restaurant is located on the ground floor of the Kirov Hotel. " \
       "We invite everyone to the \nrestaurant - only here you can taste \ndelicious dishes of European and Greek cuisine. \nThe restaurant is open daily from 12:00 to 24:00.""" \
       "\nThe bar is open every day from 12:00 to 24:00."\
       "The cozy interior and exquisite \ncuisine will make your lunch or dinner \nunforgettable. We welcome our guests and \nalways strive to pleasantly surprise them."\
       "\nThe restaurant's menu and wine list are \nthought out to the smallest detail, and our \nwaiters will help you choose a dish for \nevery taste and advise suitable \ndrinks when ordering."\
       "\nWe use only fresh products and work with trusted \npartners - because it is high-quality and fresh \ningredients that allow you to create real culinary masterpieces"\
       "\nFor visitors who prefer modern European cuisine, we offer \nsalads, hot dishes and snacks."\
       "\nFor gourmets, we have unusual dishes, the cooking \nprocess of which requires a lot of time \nand the highest skill."\
       "\nWell, we are always ready to pamper dessert lovers with \nfresh cheesecakes, cheesecakes, tiramisu, panacota \nand homemade sweets."\
       "\nFor those who want to remember the happiest and sunniest days of \ntheir holidays, we have added a Greek cuisine page to the \nmenu, as well as seafood dishes."\
       "\nYou definitely need to visit our restaurant and try everything."
polka = tk.PhotoImage(file="polka.png")
def create_window():
    window = tk.Toplevel(gui)
    window.geometry("1300x1000")
    window.title("Инфо")
    l1 = tk.Label(window, text=f"Description\n{text}", font=("Cruel", 20))
    l1.place(x=0, y=20)


info = tk.PhotoImage(file="info.png")

btn1 = tk.Button(image=info, bg="grey", command=create_window)
btn1.place(height=100, width=100, x=0, y=950)



l2 = tk.Label(
    background="blue",
    height="1",
    width="300",
)
l2.place(x=0,y=105)

sklad = tk.PhotoImage(file="sklad.png")

money = 10000
bulki = 0
kurici = 0
masyo = 0
ogurci = 0
pomidori = 0
sousi = 0
sira = 0
kartoshki = 0

def buy_bulka():
    money -= 200
    bulki += 1
def buy_kurica():
    spisok["Куриц"] += 100
def buy_masyo():
    spisok["Мясо"] += 100
def buy_ogurci():
    spisok["Огурцов"] += 1
def buy_pomidori():
    spisok["Помидоров"] += 1
def buy_sousi():
    spisok["Соусов"] += 1
def buy_siri():
    spisok["Сыра"] += 1
def buy_kartoshka():
    spisok["Картошки"] += 100


spisok = {"Булка": 1, "Куриц": 100, "Мясо": 100,"Огурцов": 1,"Помидоров": 1, "Соусов": 1, "Сыра": 1, "Картошки": 100}





def create_sklad():
    sklad_1 = tk.Toplevel(gui)
    sklad_1.geometry("800x600")
    sklad_1.title("Склад")
    l4 = tk.Label(sklad_1, image=polka)
    l4.place(x=0, y=0)
    l5 = tk.Label(sklad_1, text=f"Булок: {bulki}") #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l5.place(x=70,y=166, height=40)
    l6 = tk.Label(sklad_1, text=f"Куриц: {kurici} гр.") #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l6.place(x=190,y=166, height=40)
    l7 = tk.Label(sklad_1, text=f"Мяса: {masyo} гр.") #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l7.place(x=300,y=166, height=40)
    l8 = tk.Label(sklad_1, text=f"Огурцов: {ogurci}") #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l8.place(x=70,y=350, height=40)
    l9 = tk.Label(sklad_1, text=f"Помидоров: {pomidori}") #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l9.place(x=190,y=350, height=40)
    l10 = tk.Label(sklad_1, text=f"Соусов: {sousi}") #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l10.place(x=300,y=350, height=40)
    l11 = tk.Label(sklad_1, text=f"Сыра: {sira}") #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l11.place(x=520,y=500, height=40)
    l12 = tk.Label(sklad_1, text=f"Картошки: {kartoshki} гр.") #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l12.place(x=620,y=500, height=40)
shop = tk.PhotoImage(file="shop.png")
btn2 = tk.Button(
    background="white",  # фоновый цвет кнопки
    foreground="black",  # цвет текста
    height="100",
    width="100",
    image=sklad,
    command=create_sklad
    )
btn2.place(x=0,y=0)
magazin = tk.PhotoImage(file="magazin.png")

def create_shop():
    shop_1 = tk.Toplevel(gui)
    shop_1.geometry("1500x1000")
    shop_1.title("Магазин")
    l13 = tk.Label(shop_1, image=magazin)
    l13.place(x=0, y=0)
    l14 = tk.Button(shop_1, text="Булка: 1", command=buy_bulka) #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l14.place(x=70,y=166, height=40)
    l15 = tk.Button(shop_1, text="Курица: 100 гр.", command=buy_kurica) #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l15.place(x=190,y=166, height=40)
    l16 = tk.Button(shop_1, text="Мясо: 100 гр.", command=buy_masyo) #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l16.place(x=300,y=166, height=40)
    l17 = tk.Button(shop_1, text="Огурцы: 1", command=buy_ogurci) #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l17.place(x=70,y=350, height=40)
    l18 = tk.Button(shop_1, text="Помидоры: 1", command=buy_pomidori) #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l18.place(x=190,y=350, height=40)
    l19 = tk.Button(shop_1, text="Соус: 1", command=buy_sousi) #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l19.place(x=300,y=350, height=40)
    l20 = tk.Button(shop_1, text="Сыр: 1", command=buy_siri) #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l20.place(x=520,y=500, height=40)
    l21 = tk.Button(shop_1, text="Картошка: 100 гр.", command=buy_kartoshka) #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l21.place(x=620,y=500, height=40)
    l22 = tk.Label(shop_1, text=f"Баланс {money}") #булки,курицы,мясо,огурцы,помидоры,соусы,сыр,картошки,
    l22.place(x=800,y=500, height=40)
    l22.config()

btn3 = tk.Button(
    height="100",
    width="115",
    image=shop,
    command=create_shop
    )
btn3.place(x=120,y=0)






























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































gui.mainloop()
