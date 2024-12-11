import time
import random
energy = random.randint(50,100)
money = random.randint(100,1000)
def out_red(text):
    print("\033[31m{}".format(text))
out_red("Попередження! Якщо ваша енергія впаде менше ніж на 20 - ви помрете")

class Student:
    def __init__(self, energy, money):
        global eat
        for i in range(5):
            if energy > 20:
                print("Ваша енергія: ", energy)
                print("Ваш стан рахунку: ", money)
                if energy >= 40:
                   if money < 400:
                      a = int(input("Ви повинні піти на роботу, введіть 1 - щоб працювати в офісі(-20 від енергії та + 350 до грошей), введіть 2 щоб  працювати на заводі(-50 від енергії та +600 до грошей) :  "))
                      if a == 1 and energy > 20:
                         print("Ви будете працювати 5 секунд, зачекайте будьласка")
                         time.sleep(5)
                         energy -= 20
                         money += 350
                         print("Тепер ваш рахунок становить ", money, ", а енергія ", energy)
                      elif a == 2 and energy > 50:
                        print("Ви будете працювати 10 секунд, зачекайте будьласка")
                        time.sleep(10)
                        energy -= 50
                        money += 600
                        print("Тепер ваш рахунок становить ", money, ", а енергія ", energy)
                   else:
                       print("У вас достатньо грошей на проживання")
                       time.sleep(3)
                else:
                    print("Ви повинні поїсти щоб не вмерти від перевтоми")
                    time.sleep(2)
                    eat = int(input("Щоб з'їсти банан(енергія +30, вартість 50)  уведіть  1, щоб з'їсти бургер(енергія "
                                    "+65, вартість 100) уведіть 2, щоб з'їсти піцу(енергія +50, вартість 120) введіть 3 :"))

                    if  eat == 1 and money >= 50:
                       energy += 30
                       money -= 50
                       print("Ви з'їли банан, тепер ваша енергія: ", energy, ", а стан рахунку: ", money)
                    elif eat == 2 and money >= 100:
                       energy += 65
                       money -= 100
                       print("Ви з'їли бургер, тепер ваша енергія: ", energy, ", а стан рахунку: ", money)
                    elif eat == 3 and money >= 120:
                       energy += 50
                       money -= 120
                       print("Ви з'їли піцу, тепер ваша енергія: ", energy, ", а стан рахунку: ", money)
                    else:
                       print("Недостатньо грошей для вибраного прийому їжі")
                print("Пришйов час для оплати рахунків, з вас буде знято 300 коштів")
                money -= 300
                print("Тепер ваш рахунок становить ", money)
                time.sleep(5)
            else:
                print("Ви померли")
                break

            




Ilya = Student(energy, money)


