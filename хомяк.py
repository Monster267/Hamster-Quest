print("найдите хомяка в кустах ! Как найдете затапайте его.")
while True:
    print("давайте сделаем вашего хомяка")
    name = input("введи имя своего хомяка")
    gender = input("какой пол вашего хомяка")
    color = input("какой цвет вашего хомяка")
    print("ваш выбор")
    print("имя", name)
    print("пол хомяка", gender)
    print("окраска хомяка", color)
    start_game = input("Вы хотите начать игру с этим персонажем? (да/нет)")
    if start_game == "да":
        print("начнём игру!")
        break
    else:
        print("создадим персонажа заново!")
        continue
print("-" * 50)
while True:
print("в оказались в мире хомяков. перед вами есть три пути: полянка , кусты и клетка")
print("куда вы направитесь?")
place = input("напиши название места: ")
if place.lower() == "полянка":
    print("ты попал к хомякам. пройдёшь к ним")
    field = input("да или нет? ")
    if field == "да":
        print("на полянкке вас встретят потные хомяки")
    elif field =="нет":
        print("тогда вас задушат и помоют маслом")
if place.lower() == "кусты":
    print("ищи хомяка")
    green = input("ты нашёл хомяка?")
    if green == "если да то ты должен в клетке его затапать"
    print("тапай хомяка")
else:
     print("такого места нет!")
