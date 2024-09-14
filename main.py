"""
Домашнее задание №2.
Дата: 11.09.2024.
Название: Задача ООП наследование.
"""

class Animal:
    def __init__(self, name, age, gender, weight):
        # Инициализация основных атрибутов животного.
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def make_sound(self):
        return f"{self.name} издаёт звук"

    def eat(self):
        return f"{self.name} ест"

    def display_info(self):
        return (f"Имя: {self.name}\n"
                f"Возраст: {self.age}\n"
                f"Пол: {self.gender}\n"
                f"Вес: {self.weight} кг")


class Mammal(Animal):
    def __init__(self, name, age, gender, weight, hair_color):
        super().__init__(name, age, gender, weight)
        self.hair_color = hair_color

    def nurse(self):
        return f"{self.name} кормит детёнышей молоком."

    def eat(self):
        return f"{self.name} ест мясо или растения."

    def display_info(self):
        return (super().display_info() +
                f"\nЦвет шерсти: {self.hair_color}")


class Bird(Animal):
    def __init__(self, name, age, gender, weight, wing_span):
        super().__init__(name, age, gender, weight)
        self.wing_span = wing_span

    def fly(self):
        return f"{self.name} летает."

    def eat(self):
        return f"{self.name} ест мясо, растения, семена или насекомых."

    def display_info(self):
        return (super().display_info() +
                f"\nРазмах крыльев: {self.wing_span} см")


class Reptile(Animal):
    def __init__(self, name, age, gender, weight, scale_type):
        super().__init__(name, age, gender, weight)
        self.scale_type = scale_type

    def shed_skin(self):
        return f"{self.name} сбрасывает кожу."

    def eat(self):
        return f"{self.name} ест насекомых или мелких животных."

    def display_info(self):
        return (super().display_info() +
                f"\nТип чешуи: {self.scale_type}")


# Специфические реализации для каждого животного.
class SnowLeopard(Mammal):
    def make_sound(self):
        return f"{self.name} рычит."


class LipizzanerHorse(Mammal):
    def make_sound(self):
        return f"{self.name} ржёт."


class MuteSwan(Bird):
    def make_sound(self):
        return f"{self.name} трубит."


class GoldenEagle(Bird):
    def make_sound(self):
        return f"{self.name} кричит."


class CrocodileSkink(Reptile):
    def make_sound(self):
        return f"{self.name} пищит."


class Rattlesnake(Reptile):
    def make_sound(self):
        return f"{self.name} гремит."


snow_leopard = SnowLeopard(
    "Снежный барс", 4, "самец", 45, "светлая, дымчато-серая с "
    "кольцеобразными и сплошными тёмными пятнами"
)
lipizzaner_horse = LipizzanerHorse("Лошадь", 6, "самка", 600, "белая")

mute_swan = MuteSwan("Лебедь-шипун", 6, "самка", 11, 240)
golden_eagle = GoldenEagle("Беркут", 5, "самка", 7, 240)

crocodile_skink = CrocodileSkink(
    "Крокодиловый сцинк", 3, "самка", 0.15, "Чешуя крокодилового сцинка "
    "довольно крупная и грубая, с характерными наростами и шипами, "
    "напоминающими чешую крокодила. Эта чешуя служит защитным элементом, "
    "обеспечивая дополнительную прочность и защиту."
)
rattlesnake = Rattlesnake(
    "Гремучая змея", 3, "самка", 1, "Чешуя гремучих змей состоит из гладких, "
    "плоских чешуек, которые имеют роговые наросты и шипы на спине. Эти "
    "чешуйки образуют характерный узор и текстуру, которые помогают в "
    "маскировке и защите. Также на хвосте гремучих змей находится особый "
    "роговой «гремучий» элемент, который издает характерный звук при "
    "встряхивании."
)

# Функция, которая вызывает make_sound, eat, и методы для типа животного.
def display_all_info(animals):
    for animal in animals:
        print("=" * 40)  # Разделительная линия.
        print(animal.display_info())
        print(animal.make_sound())
        print(animal.eat())

        # Проверка на наличие специфических методов.
        if isinstance(animal, Mammal):
            print(animal.nurse())
        if isinstance(animal, Bird):
            print(animal.fly())
        if isinstance(animal, Reptile):
            print(animal.shed_skin())

        print("=" * 40)  # Разделительная линия.
        print()  #Печать пустой строки для разделения информации.


zoo_animals = [
    snow_leopard, lipizzaner_horse, mute_swan, golden_eagle,
    crocodile_skink, rattlesnake
]
display_all_info(zoo_animals)